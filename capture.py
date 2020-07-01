import cv2, time

cap = cv2.VideoCapture(0)
frameCount = 1
while True: 
    ret, frame = cap.read()
    print(ret)
    print(frame.sum()) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera", gray)
    frameCount = frameCount + 1
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

print(frameCount)