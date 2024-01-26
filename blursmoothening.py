import cv2

img =cv2.imread("img7.jpg")
#dst=cv2.GaussianBlur(src,(kernel),borderType)
gaussianImg=cv2.GaussianBlur(img,(41,41),50)
gaussianImg1=cv2.GaussianBlur(img,(21,21),50)
cv2.imshow("original ",img)
cv2.imshow("gaussianImg",gaussianImg)
cv2.imshow("gaussianImg1",gaussianImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()