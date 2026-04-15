import cv2
import os
import numpy
img1 = cv2.imread("pika.jpg")
img2 = cv2.imread("tj.jpg")
resize1 = cv2.resize(img1,(500,500))
resize2 = cv2.resize(img2,(500,500))

subtracted_img = cv2.subtract(resize1,resize2)
cv2.imshow("Subtracted Image",subtracted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

added_img = cv2.add(resize1,resize2)
cv2.imshow("Added Image",added_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

multiplied_img = cv2.multiply(resize1,resize2)
cv2.imshow("Multiplied Image",multiplied_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

divided_img = cv2.divide(resize1,resize2)
cv2.imshow("Divided Image",divided_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gaussian_img = cv2.GaussianBlur(resize1,(17,17),0)
cv2.imshow("Gaussian Blured Image",gaussian_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

median_img = cv2.medianBlur(resize1,15)
cv2.imshow("Median Blured Image",median_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral_img = cv2.bilateralFilter(resize1,5,75,75)
cv2.imshow("Bilateral Blured Image",bilateral_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

bordered_img = cv2.copyMakeBorder(resize1,10,10,10,10,cv2.BORDER_CONSTANT,value = [255,255,255])
cv2.imshow("Bordered Image",bordered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflected_img = cv2.copyMakeBorder(resize1,10,10,10,10,cv2.BORDER_REFLECT, value = [0,0,255] )
cv2.imshow("Reflected Border",reflected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()