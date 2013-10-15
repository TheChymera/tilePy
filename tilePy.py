#!/usr/bin/env python
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
__author__ = 'Horea Christian'

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from PIL import Image
from os import listdir, path, makedirs

image_dir = path.dirname(path.dirname(path.realpath(__file__))) + '/faceRT/experiment/img/px6/'
sequence = pd.DataFrame.from_csv('/home/chymera/src/pystim/sequences/faceRT.csv')
output_dir = path.dirname(path.realpath(__file__)) + '/output/'

if not path.isdir(output_dir):
    makedirs(output_dir)

for idx, trial in sequence.iterrows():
    bg = Image.new('L', (1360,768), (122)) #size of the background, in pixels AND pixel color value
    top_img = Image.open(image_dir+trial['top face'],'r')
    top_img = top_img.resize((int(top_img.size[0]//10*7),int(top_img.size[1]//10*7)), Image.ANTIALIAS) # Use PIL to resize :(
    left_img = Image.open(image_dir+trial['left face'],'r')
    left_img = left_img.resize((int(left_img.size[0]//10*7),int(left_img.size[1]//10*7)), Image.ANTIALIAS) # Use PIL to resize :(
    right_img = Image.open(image_dir+trial['right face'],'r')
    right_img = right_img.resize((int(right_img.size[0]//10*7),int(right_img.size[1]//10*7)), Image.ANTIALIAS) # Use PIL to resize :(
    bg.paste(top_img,(565,89)) #coordinates of the top left corner where the image is pasted
    bg.paste(left_img,(269,385)) #idem
    bg.paste(right_img,(861,385)) #idem
    bg.save(path.splitext(output_dir+trial['top face'])[0]+'_em'+str(trial['emotion intensity'])+'_composite'+'.bmp')
    #~imgplot = plt.imshow(bg, cmap = cm.Greys_r, vmin=0, vmax=255, interpolation='nearest')
    #~plt.show()
