from fer import FER
import cv2
from flask import url_for
import os

emotion_detector = FER(mtcnn=True)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_top_emotion(image):
    # Code to detect emotions and determine the top emotion
    emotions = emotion_detector.detect_emotions(image)

    if len(emotions) > 0:
        face = emotions[0]
        top_emotion = max(face['emotions'], key=face['emotions'].get)
        return top_emotion
    else:
        return "No faces with emotions detected in the image."

def capture_image(filename):
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    if ret:
        cv2.imwrite(filename, frame)
        print('Image captured successfully!')
    else:
        print('Failed to capture image.')

def get_image_url(condition):
    if condition == 1:
        img_url = url_for('static', filename = 'angry.JPG')
    elif condition == 2:
        img_url = url_for('static', filename = 'disgust.JPG')
    elif condition == 3:
        img_url = url_for('static', filename = 'fear.JPG')
    elif condition == 4:
        img_url = url_for('static', filename = 'happy.JPG')
    elif condition == 5:
        img_url = url_for('static', filename = 'neutral.JPG')
    elif condition == 6:
        img_url = url_for('static', filename = 'sad.JPG')
    elif condition == 7:
        img_url = url_for('static', filename = 'surprise.JPG')
    elif condition == 0:
        img_url = url_for('static', filename = 'no_emotion.JPG')

    return img_url

def get_img_url():
    img_url = url_for('static', filename = 'captured_image.jpg')
    return img_url

def get_gif():
    img_url = url_for('static', filename = 'emo_load.gif')
    return img_url

def delete_image():
    image_path = os.path.join(os.path.dirname(__file__), 'static', 'captured_image.jpg')
    try:
        os.remove(image_path)
        print("Image deleted successfully.")
    except OSError as e:
        print(f"Error occurred while deleting the image: {e}")
