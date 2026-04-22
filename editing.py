import cv2
import numpy 
start_point = (0,0)
end_point = (500,500) 
thickness = 3
color = (0,0,255)
image1 = cv2.imread("pika.jpg")
image2 = cv2.imread("tj.jpg")

line_image = cv2.line(image1,start_point,end_point,color,thickness)
cv2.imshow("Lined Image",line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
                                                                      
rec_image = cv2.rectangle(image2,start_point,end_point,color,thickness)
cv2.imshow("Rectangle Image",rec_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

rect_image = cv2.rectangle(image2,(100,100),(120,120),color,-1)
cv2.imshow("Rectangle Image",rect_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

radius = 50
center_cos = (100,100)
circular_img = cv2.circle(image2,center_cos,radius,color,thickness)
cv2.imshow("Circular Image",circular_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

circ_img = cv2.circle(image2,center_cos,radius,color,-1)
cv2.imshow("Circular Image",circ_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

font = cv2.FONT_HERSHEY_PLAIN
origin = (100,100)
font_scale = 1
color = (0,0,0)
thickness = 3
font_img = cv2.putText(image2,"Tom and Jerry",origin,font,font_scale,color,thickness,cv2.LINE_AA)
cv2.imshow("Text Image",font_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
