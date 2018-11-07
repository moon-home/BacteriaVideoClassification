## VidConvert.py
This file converts a folder of videos into a folder of videos with a new format.

## VidConverter_py2.7ffmpeg4.0.yml
This is the environment file for setting up the verisions of python and ffmpeg for running `VidConvert.py` to convert a folder of videos into a folder of videos with new format.

## Img2Vid.ipynb
This file converts a folder of images into a video.

## BigVid2LitVid.ipynb
This file cut all long videos (e.g. 10min) from a folder into smaller videos (e.g. 5s). Smaller videos are put into the same folder as long videos.

**step 1**: download BigVid2LitVid.ipynb and cutter.py to the same directory where your folder of long videos is located

**step 2**: change variables "big_folder" and "dur" in BigVid2LitVid.ipynb to the name of your folder of long videos and length of short videos

**step 3**: run BigVid2LitVid.ipynb

**result**: short videos are generated in the same folder of your long videos

## cutter.py
Called in BigVid2LitVid.ipynb
