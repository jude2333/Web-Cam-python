import cv2
import numpy as np

url = "http://192.168.1.12:8080/video"
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Failed to open video capture object")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)

    if q == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
