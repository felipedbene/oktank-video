import cv2
import os

image_folder = '.'
video_name = 'video_sorted.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
video = cv2.VideoWriter(video_name, fourcc, 20.0, (width, height))

#video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    img = os.path.join(image_folder, image)
    print(img)
    video.write(cv2.imread(img))

cv2.destroyAllWindows()
video.release()