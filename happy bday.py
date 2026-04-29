import cv2
img = cv2.imread("cake.jpg")
color = (0, 255, 0)
thickness = -1
start_point = (50, 350)
end_point = (450, 480)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
text_color = (255, 0, 0)
text_thickness = 2
text_position = (80, 430)

rectangle_img = cv2.rectangle(img, start_point, end_point, color, thickness)
updated_img = cv2.putText(img, "Happy Birthday!", text_position, font, font_scale, text_color, text_thickness)
cv2.imshow("image", updated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()