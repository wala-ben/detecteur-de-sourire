import numpy as np
import cv2
#from controller import doorAutomate

faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade=cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30)
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]

        smile=smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.5,
            minNeighbors=15,
            minSize=(25,25)
        )
        for i in smile:
            if len(smile)>1:
               # doorAutomate(0)
                cv2.putText(img,"beautiful smile wala",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3,cv2.LINE_AA)
           # elif doorAutomate(1)
    cv2.imshow('video', img)
    q=cv2.waitKey(30) & 0xff
    if q==27: #press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()








from pyfirmata import Arduino,SERVO

 port='COM5'

 pin=10

 board=Arduino(port)

 board=degital[pin].mode=SERVO
 def rotateServo(pin,angle):
     board.digital[pin].write(angle)

 def doorAutomate(val):
     if val==0:
         rotateServo(pin,180)
     #elif value==1:
       # rotateServo(pin,40)
