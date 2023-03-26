# Pytorch_MST
Unofficial Pytorch(1.0+) implementation of ICCV 2019 paper ["Multimodal Style Transfer via Graph Cuts"](https://arxiv.org/abs/1904.04443).

Original tensorflow implementations from the authon will be found [here](https://github.com/yulunzhang/MST).

This repository provides a pre-trained model for you to generate your own image given content image and style image. Also, you can download the training dataset or prepare your own dataset to train the model from scratch.

If you have any question, please feel free to contact me. (Language in English/Japanese/Chinese will be ok!)

## Notice
I propose a structure-emphasized multimodal style transfer(SEMST), feel free to use it [here](https://github.com/irasin/Structure-emphasized-Multimodal-Style-Transfer).

## Requirements

- Python 3.7+
- PyTorch 1.0+
- TorchVision
- Pillow
- PyMaxflow

Anaconda environment recommended here!

(optional)

- GPU environment 

# README group 1 subject 3

Santarelli Quentin
Belet Antoine

This is the final result of our project.
Our work is based on the pythorch work for Multimodal Style Transfer via Graph Cuts.
All information can be seen above.

We choosed to try style transfer on videos to see if the algorithm kept the structure of the images in a continuous way.
We worked in a static way, frames by frames, on videos.

We also think that working dynamicaly would be very interesting but we didn't tackeled this topic at all.


Here is how the wode works:

The code was running on VS Code.

The main.sh run 4 commands in order:
1. It execute clean_forlder.py file that clean "test_result" and "test_content" folders
2. It execute video2frame.py file. You have to change the path in the main.sh to the one on your computer to make it work.
3. It execute test.py file with 2 folders as argument, "test_style" and "test_content".
4. It execute frame2video.py file. You have to change the path in the main.sh to the one on your computer to make it work.

## To run tests

First, you have to select a picture of your choice in the "style" folder and put it in the "test_style" folder. Be careful when you upload your own style images as its dimensions can make the program fail when you execute "test.py".
Also be aware that it is better to select only one picture in "test_style" as the algorithm iterate with the number of styles on every frame of the video in input.

Then you have to put a video with .mp4 format in the "videos" folder.
It's better if the video is short (10 sec), otherwise it will take a lot of time.

By then you should have one picture in "test_style" and your video in "videos".
You should now to run the commands in the main.sh file on your terminal.

There is few steps to follow:
1. It will ask you for the name of your video. You should only give the name without the extension (Example if your video is called jojo.mp4, only write "jojo" in the terminal)
2. Then you will have to input the frame rate (frames/second) you would like to slice your video into. It will cut frames (up to 9999) of your video and put them in the "test_content" folder.
3. The test.py will run and apply the style of the picture in the "test_style" folder to the images in the "test_content" folder and put the result in the "test_result" folder.
4. You have to give the name of the style and of the content. 
5. You'll have to give the frame rate of the output video.

In the end you should obtain you video called "style_content_framerate.mp4" in the "video_result" folder.


# Original README 

## test

1. Clone this repository 

   ```bash
   git clone https://github.com/irasin/Pytorch_MST
   cd Pytorch_MST
   ```

2. Prepare your content image and style image. I provide some in the `content` and `style` and you can try to use them easily.

3. Download the pretrained model [here](https://drive.google.com/file/d/16mhOUIo8HKDv9NhlI1GyKvpqST8P9fGw/view?usp=sharing)

4. Generate the output image. A transferred output image w/&w/o style image and a NST_demo_like image will be generated.

   ```python
   python test.py -c content_image_path -s style_image_path
   ```

   ```
    usage: test.py [-h] [--content CONTENT] [--style STYLE]
                [--output_name OUTPUT_NAME] [--n_cluster N_CLUSTER]
                [--alpha ALPHA] [--lam LAM] [--max_cycles MAX_CYCLES]
                [--gpu GPU] [--model_state_path MODEL_STATE_PATH]
   ```

   If output_name is not given, it will use the combination of content image name and style image name.


------

## train

1. Download [COCO](http://cocodataset.org/#download) (as content dataset)and [Wikiart](https://www.kaggle.com/c/painter-by-numbers) (as style dataset) and unzip them, rename them as `content` and `style`  respectively (recommended).

2. Modify the argument in the` train.py` such as the path of directory, epoch, learning_rate or you can add your own training code.

3. Train the model using gpu.

4. ```python
   python train.py
   ```

   ```
    usage: train.py [-h] [--batch_size BATCH_SIZE] [--epoch EPOCH] [--gpu GPU]
                    [--learning_rate LEARNING_RATE]
                    [--snapshot_interval SNAPSHOT_INTERVAL]
                    [--n_cluster N_CLUSTER] [--alpha ALPHA] [--lam LAM]
                    [--max_cycles MAX_CYCLES] [--gamma GAMMA]
                    [--train_content_dir TRAIN_CONTENT_DIR]
                    [--train_style_dir TRAIN_STYLE_DIR]
                    [--test_content_dir TEST_CONTENT_DIR]
                    [--test_style_dir TEST_STYLE_DIR] [--save_dir SAVE_DIR]
                    [--reuse REUSE]
   ```



# Result

Some results of content image will be shown here.

![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_contrast_of_forms_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_scene_de_rue_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_picasso_self_portrait_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_candy_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_brushstrokers_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_asheville_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_antimonocromatismo_demo.jpg)
![image](https://github.com/irasin/Pytorch_MST/blob/master/result/avril_876_demo.jpg)

