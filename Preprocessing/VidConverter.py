import os




import os
from os import listdir
from os.path import isfile, join

source_path = './VidBatch'
out_path = './VidMP4'

onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]
for InputVidName in onlyfiles:
	converter = os.system("ffmpeg -i video.avi -codec copy test.mp4")