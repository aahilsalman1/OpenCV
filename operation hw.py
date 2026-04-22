import cv2
import os
import numpy
img1 = cv2.imread("tree.jpg")
img2 = cv2.imread("strawberry.jpg")
resize1 = cv2.resize(img1,(500,500))
resize2 = cv2.resize(img2,(500,500))

subtracted_img = cv2.subtract(resize1,resize2)
cv2.imshow("Subtracted Image",subtracted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gaussian_img = cv2.GaussianBlur(resize2,(17,17),0)
cv2.imshow("Gaussian Blured Image",gaussian_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

bordered_img = cv2.copyMakeBorder(resize2,10,10,10,10,cv2.BORDER_CONSTANT,value = [0,0,255])
cv2.imshow("Bordered Image",bordered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()