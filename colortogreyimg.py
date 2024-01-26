import cv2
image= cv2.imread("img7.jpg")
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('original',image)
cv2.imshow('Grey',greyImage)
cv2.waitKey(0)