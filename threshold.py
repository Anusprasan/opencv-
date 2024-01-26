import cv2
img=cv2.imread("img9.jpg")
greyImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dst=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]
thresholdImg=cv2.threshold(greyImg,180,255,cv2.THRESH_BINARY)[1]
cv2.imshow("original",img)
cv2.imshow("greyImg",greyImg)
cv2.imshow("threshold.jpg",thresholdImg)
cv2.waitKey(0)

# 0 - Black
# 180 -
# 255- White