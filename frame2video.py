import cv2
import os

# Define the folder path containing the input images
input_folder = "test_result"

print("Give the name of the style ")
style_name= input()

print("Give the name of the video ")
video_name= input()

# Define the frame rate of the output video (in frames per second)
print("Enter the framerate you choosed")
frame_rate = int(input())

# Define the output video file path
output_path = f".\\video_result\\{style_name}_{video_name}_{frame_rate}_frames.mp4"



# Get the dimensions of the first image in the folder (assuming all images have the same dimensions)
test_image = cv2.imread(os.path.join(input_folder, os.listdir(input_folder)[0]))
height, width, channels = test_image.shape

# Initialize the video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, (width, height))

# Loop through the input folder and add each image to the video writer object
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Read in the next image from the folder
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Write the image to the video writer object
        video_writer.write(image)

# Release the video writer object and close any open windows
video_writer.release()
cv2.destroyAllWindows()