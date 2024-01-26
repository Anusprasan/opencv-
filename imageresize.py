import cv2
import imutils
img =cv2.imread("img7.jpg")
resizedImg=imutils.resize(img,width=100)
cv2.imshow('original Image',img)
cv2.imshow('resizedimage.jpg',resizedImg)
cv2.imwrite('resizedimage.jpg',resizedImg)
cv2.waitKey(10000)
