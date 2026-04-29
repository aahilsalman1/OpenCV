import cv2
import os
import numpy as np
from PIL import Image
os.chdir('C:\\Users\\dell\\OneDrive\\Attachments\\Python\\OpenCV\\images')
path = 'C:\\Users\\dell\\OneDrive\\Attachments\\Python\\OpenCV\\images'
average_height = 0
average_width = 0
total_height = 0
total_width = 0
image_number = len(os.listdir('.'))

for image in os.listdir('.'):
    current_image = Image.open(os.path.join(path,image))
    width,height = current_image.size
    total_height = total_height + height
    total_width = total_width + width

average_height = total_height//image_number
average_width = total_width//image_number

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)
        imgResized = img.resize((average_width, average_height), Image.Resampling.LANCZOS)
        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], "is resized")

video_name = "My Video.avi"
images = []
for image in os.listdir('.'):
    images.append(image)
print(images)

frame = cv2.imread(os.path.join(".", images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 1, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(".", image)))
cv2.destroyAllWindows()
video.release()





    

