from flask import Flask, render_template, redirect, url_for, jsonify
from concurrent.futures import ThreadPoolExecutor
import time
import cv2
import os
import signal
from main import get_top_emotion, capture_image, get_image_url, get_img_url, delete_image, get_gif

app = Flask(__name__)

executor = ThreadPoolExecutor()

stop_loop = True
global top_emotion
top_emotion = "No emotion detected"
global old_emotion
old_emotion = top_emotion
global flag
flag = 0
global condition
condition = 0

def update_emotion_and_image():
    global top_emotion
    global condition
    global old_emotion
    global flag
    while not stop_loop:
        # Code to update the top_emotion and image_path variables
        # ...

        # Update the top_emotion
        path = os.path.join('static','captured_image.jpg')
        capture_image(path)
        image = cv2.imread('static/captured_image.jpg')
        top_emotion = get_top_emotion(image)
        #setting flag value
        if old_emotion == top_emotion:
            flag = 0
        else:
            flag = 1
        # Checking conditions for displaying image
        if top_emotion == 'angry':
            condition = 1
        elif top_emotion == 'disgust':
            condition = 2
        elif top_emotion == 'fear':
            condition = 3
        elif top_emotion == 'happy':
            condition = 4
        elif top_emotion == 'neutral':
            condition = 5
        elif top_emotion == 'sad':
            condition = 6
        elif top_emotion == 'surprise':
            condition = 7
        else :
            top_emotion = "No emotion detected"
            condition = 0

        time.sleep(15)  # Wait for 2 seconds before updating again

# Route to display the template
@app.route('/')
def index():
    return render_template('index.html')#, top_emotion=top_emotion, condition=condition)#, image_path=image_path)

@app.route('/start', methods = ['POST', 'GET'])
def start():
    return redirect(url_for('start_page'))

@app.route('/start_page', methods = ['GET', 'POST'])
def start_page() :
    global stop_loop
    stop_loop = False
    # update_emotion_and_image()

    #Start Background Task
    executor.submit(update_emotion_and_image)

    # print('Executor worked fine')
    return render_template('main.html', top_emotion=top_emotion, condition=condition)

@app.route('/pause', methods = ['POST', 'GET'])
def pause():
    global stop_loop
    stop_loop = True
    return redirect(url_for('pause_page'))
    # return 'Paused Sucessfully'

@app.route('/pause_page')
def pause_page():
    return render_template('pause.html', top_emotion=top_emotion, condition=condition)

@app.route('/play', methods = ['POST', 'GET'])
def play():
    return redirect(url_for('start_page'))

@app.route('/stop', methods = ['POST', 'GET'])
def stop():
    global stop_loop
    stop_loop = True
    #return 'Stopped sucessfully'
    return redirect(url_for('stop_page'))

@app.route('/stop_page')
def stop_page():
    return render_template('stop.html', message='Stopped Successfully...')

@app.route('/home', methods = ['POST', 'GET'])
def home():
    global stop_loop
    stop_loop = True
    global top_emotion
    top_emotion = 'No emotion detected'
    delete_image()
    return redirect(url_for('home_page'))

@app.route('/home_page')
def home_page():
    return render_template('index.html')

@app.route('/get_content', methods=['GET'])
def get_content():
    global top_emotion
    global condition
    # Get the image URL and top emotion from your backend logic or database
    image_url = get_image_url(condition)
    img_url = get_img_url()

    # Create a dictionary containing the image URL and top emotion
    response = {'image_url': image_url, 'top_emotion': top_emotion, 'img_url': img_url}
    print(response)
    # Return the response as JSON
    return jsonify(response)

@app.route('/gif', methods=['GET'])
def gif():
    image_url = get_gif()
    response = {'image_url': image_url,}
    print(response)
    # Return the response as JSON
    return jsonify(response)

@app.route('/quit', methods=['POST'])
def shutdown():
    delete_image()
    # Trigger server shutdown
    os.kill(os.getpid(), signal.SIGINT)
    return redirect(url_for('/kill')) + 'Server shutting down...'

if __name__ == '__main__':
    app.run()