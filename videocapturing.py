import cv2
vs = cv2.VideoCapture(0)
while True:
    a,img=vs.read()
    print(a)
    cv2.imshow("VideoStream",img)
    
    key=cv2.waitKey(1)
    print(key)
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()