import cv2

#loading the cascaseClassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture the video
cap = cv2.VideoCapture(0)
while True:

    #capture frame by frame
    _, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   
    #detecting the faces and returns the boundary values of detected face
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 2)

    #displaying the resulting frame
    cv2.imshow('img',img)
    
    #setting the display time
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
