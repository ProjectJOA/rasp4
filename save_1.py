import datetime
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False
video = None
while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)

  now = datetime.datetime.now().strftime("%d_%H-%M-%S")
  key = cv2.waitKey(33)

  if key == 24: # CTRL+X
    print("recording~~!!")
    record = True
    video = cv2.VideoWriter("C:/data/" + str(now) +".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
  elif key == 26: # CTRL+Z
    print("stop!!")
    record = False
    video.release()
  
  if record == True:
    video.write(frame)
  
  if cv2.waitKey(1) == 27: #ESC
    video.release()
    break

cv2.destroyAllWindows()