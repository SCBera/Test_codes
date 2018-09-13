"""
This code extracts corresponding slices from a series of images stacks and make a
separate stack from it.
Inputs requires:
files derectory that must end with '\', position of the slice/stack need
be extracted, number of files to be read.
The code is mostly adopted from:http://www.bioimgtutorials.com/2016/08/03/creating-a-z-stack-in-python/
Runs in 64bit environment with Python3 (64bit), scikit image, numpy
Author: Subhas Ch Bera
Year: September 2018
"""
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os

import glob

#files = glob.glob(Dir+filetype)
#print(files)

dir = input('Dir>')
Dir = dir.replace('\\', '/')
# print(dir)
# print(Dir)

slice_pos = input('slice_position>')
nfiles = input('How many files to read>')

def get_filelist(Dir, filetype='*.tif'):
    files = glob.glob(Dir+filetype)
    del files[0]
    files_mod = files
    return files_mod

filelists = get_filelist(Dir)
#print(len(filelists))
#print(filelists[0])

def get_max_all(filelists):
    img = io.imread(filelists[0])
    #print('image_shape:', img.shape)
    stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), np.uint16)
    for slice in img.shape[0]:
        for n in range(0, len(filelists)):
            img = io.imread(filelists[n])
            new_img = (img[int(slice)]) #counting starts from 0 in python
            print(f"reading file no.{n+1}")
            stack[n, :, :] = new_img
        im_max= np.max(stack, axis=0)
        os.makedirs(Dir+'Processed/', exist_ok=True)
        io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice}_first_{len(filelists)}_files.tif", im_max)

    return im_max


def get_max_limited(filelists, slice_pos, nfiles):
    img = io.imread(filelists[0])
    #print('image_shape:', img.shape)
    stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), np.uint16)
    if slice_pos.lower != 'all' and nfiles.lower == 'all':
        for n in range(0, len(filelists)):
            img = io.imread(filelists[n])
            new_img = (img[int(slice_pos)-1]) #counting starts from 0 in python
            print(f"reading file no.{n+1}")
            stack[n, :, :] = new_img
        im_max= np.max(stack, axis=0)
        os.makedirs(Dir+'Processed/', exist_ok=True)
        io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_first_{len(filelists)}_files.tif", im_max)

    elif slice_pos.lower != 'all' and nfiles.lower != 'all':
        for n in range(0, int(nfiles)):
            img = io.imread(filelists[n])
            new_img = (img[int(slice_pos)-1]) #counting starts from 0 in python
            print(f"reading file no.{n+1}")
            stack[n, :, :] = new_img
        im_max= np.max(stack, axis=0)
        os.makedirs(Dir+'Processed/', exist_ok=True)
        io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_first_{nfiles}_files.tif", im_max)

    return im_max

if slice_pos.lower == 'all' and nfiles.lower == 'all':
    result = get_max_all(filelists)
    plt.imshow(result, cmap='gray')
    plt.show()
else:
    result = get_max_limited(filelists, slice_pos, nfiles)
    plt.imshow(result, cmap='gray')
    plt.show()


#img = io.imread(filelists[0])
#print('dtype:', img.dtype)
#print('image_shape:', img.shape)