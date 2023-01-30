import cv2

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

left_eye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

right_eye = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')


webcam = cv2.v