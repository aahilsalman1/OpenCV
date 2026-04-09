import cv2
import os
import numpy as np
image1 = cv2.imread("tj.jpg",cv2.IMREAD_COLOR)
cv2.imshow("My Original Image",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread("tj.jpg",0)
cv2.imshow("My Grayscale Image",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

save1 = cv2.imwrite("grayscale.jpg",image2)

image3 = cv2.imread("tj.jpg",1)
B,G,R = cv2.split(image3)
zero_array = np.zeros_like(B)
blue_img = cv2.merge([B,zero_array,zero_array])
green_img = cv2.merge([zero_array,G,zero_array])
red_img = cv2.merge([zero_array,zero_array,R])

cv2.imshow("Blue Saturated Image",blue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Green Saturated Image",green_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Red Saturated Image",red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()