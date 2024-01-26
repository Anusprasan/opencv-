import numpy as np
import cv2
img = cv2.imread("img5.jpg")
cv2.imshow('show',img)
cv2.imwrite('img6.png',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()