# # from fer import FER
# # import cv2
# # emotion_detector = FER(mtcnn=True)
# # facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# # img = cv2.imread('captured_image.jpg')

# # emotion = emotion_detector.detect_emotions(img)
# # print(emotion)
# from main import get_top_emotion, capture_image
# import cv2
# import os
# import time

# global stop_loop
# stop_loop = False
# def update_emotion_and_image():
#     global top_emotion
#     global condition
#     #i = 0
#     while not stop_loop:
#         # Code to update the top_emotion and image_path variables
#         # ...

#         # Update the top_emotion
#         path = os.path.join('static','captured_image.jpg')
#         capture_image(path)
#         image = cv2.imread('static/captured_image.jpg')
#         top_emotion = get_top_emotion(image)
#         # Checking conditions for displaying image
#         if top_emotion == 'angry':
#             condition = 1
#         elif top_emotion == 'disgust':
#             condition = 2
#         elif top_emotion == 'fear':
#             condition = 3
#         elif top_emotion == 'happy':
#             condition = 4
#         elif top_emotion == 'neutral':
#             condition = 5
#         elif top_emotion == 'sad':
#             condition = 6
#         elif top_emotion == 'surprise':
#             condition = 7
#         else :
#             top_emotion = "No emotion detected"
#             condition = 0
        
#         # Update the image_path
#         #image_path = "static/captured_image.jpg"
#         print(top_emotion)

#         time.sleep(2)  # Wait for 2 seconds before updating again

# update_emotion_and_image()
import os

def delete_image():
    image_path = os.path.join(os.path.dirname(__file__), 'static', 'captured_image.jpg')
    try:
        os.remove(image_path)
        print("Image deleted successfully.")
    except OSError as e:
        print(f"Error occurred while deleting the image: {e}")

delete_image()