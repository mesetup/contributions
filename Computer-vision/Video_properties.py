import cv2
import datetime

#reading the camera
cap = cv2.VideoCapture(0)
#for output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))

#Capturing the frame contiously using looping
while True:
    ret, frame = cap.read()
    #for creating rectangle
    frame = cv2.rectangle(frame, (384,0), (510, 118), (0,255,0), -1)
    #for creating circle
    frame = cv2.circle(frame,(447,63), 63, (255,0,0), -1)
    #show current date and time
    date_time = str(datetime.datetime.now())
    frame = cv2.putText(frame, date_time, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)
    #for putting text on frame
    text = 'test video'
    frame = cv2.putText(frame,text, (10,300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_AA)
    if ret == True:
        out.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
          break
cap.release()
out.release()
cv2.destroyAllWindows()