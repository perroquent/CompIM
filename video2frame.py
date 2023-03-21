import cv2 as cv
from utils import extract_image_names_recursive
import os

def video2frame():
    # get video name
    print("Give the name of the video ")
    video_name= input()
    print("Thanks")
    frame_rate = 10 # 10 frames per second
    output_folder = "./videos/" + video_name

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    video_path = "./videos/" + video_name + ".mp4"
    #  get video
    cap = cv.VideoCapture(video_path)

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_skip = int(round(fps/frame_rate))


    frame_count = 0
    # loop on the video 

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            if frame_count % frame_skip == 0:
                frame_path = os.path.join(output_folder, "frame_{0}.jpg".format(frame_count))

                cv.imwrite(frame_path, frame)



            # Press C on keyboard to exit
            if cv.waitKey(25) & 0xFF == ord('c'):
                break

        else: 
            break

        frame_count +=1
    cap.release() 

video2frame()


def frame2videos():
    print("Give the style name")
    style= input()
    print("Give the frame name")
    video_name = input()
    print("Thanks")

    frame_name_list = extract_image_names_recursive("./videos")


    video_path = "./videos/" + style + '_' + video_name + ".mp4"
    first_image = cv.imread(frame_name_list[0])
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(video_path, fourcc, fps =10, frameSize=first_image.shape[:2])

    for name in frame_name_list:

        frame = cv.imread(name)
        out.write(frame)

    out.release()

frame2videos() 