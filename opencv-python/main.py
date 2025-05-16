import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*"XVID")
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
outer = cv.VideoWriter("detect.avi", fourcc, 20.0, (frame_width,frame_height))

if not cap.isOpened():
    print("Imposible to open the camera")
    exit()

faces_scade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        print('erreur')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faces_scade.detectMultiScale(gray,1.03,5)
    
    for (x,y,w,h) in faces:
        img = cv.rectangle(frame, (x,y),(x + w,y + h),(0,255,0),2)
        rol_gray = gray[y:y+h, x:x+w]
        rol_color = img[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(rol_gray,1.03,1)
        
        for (ex,ey,ew,eh) in eyes:
            img = cv.rectangle(rol_color, (ex,ey),(ex + ew, ey + eh),(255,0,200),3)

    if cv.waitKey(1) == ord("g"):
        break
        
    outer.write(frame)
    cv.imshow('image detection', frame)

cap.release()
outer.release()
cv.destroyAllWindows()


