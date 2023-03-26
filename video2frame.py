import cv2 as cv
import os

def video2frame():
    # get video name
    print("Give the name of the video ")
    video_name= input()
    print("Give the desired framerate")
    frame_rate = int(input())
    output_folder = "./test_content"

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
                frame_name = "frame_" + str(frame_count).zfill(4) + ".jpg"
                frame_path = os.path.join(output_folder, frame_name)

                cv.imwrite(frame_path, frame)
            
            
        
            # Press C on keyboard to exit
            if cv.waitKey(25) & 0xFF == ord('c'):
                break
        
        else: 
            break

        frame_count +=1
    cap.release() 

"""
def rename():
    dir = 'test_result'
    for f in os.listdir(dir):
        x = os.path.splitext(f)[0]
        prefix = x[:13]
        sufix = x[13:]
        print(prefix)
        print(sufix)
        frame_name = prefix + sufix.zfill(4) + ".jpg"
        os.rename(os.path.join(dir,f),os.path.join(dir,frame_name))

#rename()
"""
video2frame()