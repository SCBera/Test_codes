"""
This code reads ".tif" files/stacks from given directory (excluding the first file).
Extracts slices from stacks and make a MAX projection of the slices.
Save it in a separate folder inside destination folder.


Inputs requires during run:
script -a for automatic mode then files derectory

script -(anything) for manual mode then files derectory that must end with '\' and
position of the slice/stack need be extracted, number of files to be read.

The code is mostly adopted from:http://www.bioimgtutorials.com/2016/08/03/creating-a-z-stack-in-python/
Runs in 64bit environment with Python3 (64bit), scikit image, numpy
Author: Subhas Ch Bera
Last updated: September 2018
"""
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import sys

#files = glob.glob(Dir+filetype)
#print(files)
# This gets the lists of files in the directory given with first file name removed
def get_filelist(Dir, filetype='*.tif'):
    files = glob.glob(Dir+filetype)
    del files[0] # deletes first file form the list
    files_mod = files
    return files_mod

# This function gives out of the MAX projection of all the individual slices
# from all the files in the above list of files
def get_max_all(filelists):
    img = io.imread(filelists[0])
    mean = []
    mean_all_tm_points = []
    std_all_tm_points = []
    tm_points =[]

    #print('image_shape:', img.shape[0])
    if len(img.shape) < 3:
        print('\nImage is not a stack! Please choose a stack of images.')
        result = img
        return result
    else:
        #stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), img.dtype)
        for slice in range(0, img.shape[0]):
            slice_tm = slice*tm_int
            for n in range(0, len(filelists)):
                img = io.imread(filelists[n])
                new_img = (img[slice])
                filename = ((filelists[n])[(len(filelists[0])-20):])
                print(f"Reading slice-{slice+1} of file '...{filename}'")
                img_mean = new_img.mean()  # gets the mean intensity of image
                mean.append(img_mean)                
            #os.makedirs(Dir+'Processed/', exist_ok=True)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice+1}_from_{len(filelists)}-files.tif", im_max)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice+1}_{len(filelists)}_files.tif", stack)
            mean_all = np.array([mean])
            tm_points.append(slice_tm)
            mean_all_tm_points.append(mean_all.mean())
            std_all_tm_points.append(mean_all.std())
        
        results = np.array([tm_points, mean_all_tm_points, std_all_tm_points])
        os.makedirs(Dir+'Processed/', exist_ok=True)
        np.savetxt(Dir+'Processed/' + 'results.csv', results, delimiter=",")

    return results

# This function gives out of the MAX projection of selective slices
# from selective/all the files in the above list of files
def get_max_limited(filelists, slice_pos, nfiles):
    img = io.imread(filelists[0])
    #stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), img.dtype)
    mean = []
    #print('image_shape:', img.shape)
    if len(img.shape) < 3:
        print('\nImage is not a stack! Please choose a stack of images.')
        result = img
        return result
    else:
        if slice_pos.lower() != 'all' and nfiles.lower() == 'all':
            for n in range(0, len(filelists)):
                img = io.imread(filelists[n])
                new_img = (img[int(slice_pos)-1])
                filename = ((filelists[n])[(len(filelists[0])-20):])
                print(f"Reading slice-{slice_pos} of file '...{filename}'")
                img_mean = new_img.mean()  # gets the mean intensity of image
                mean.append(img_mean)
            #os.makedirs(Dir+'Processed/', exist_ok=True)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_{len(filelists)}_files.tif", stack)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice_pos}_from_{len(filelists)}-files.tif", im_max)
            mean_all = np.array([mean])
            results = [mean_all.mean(), mean_all.std()]
        

        elif slice_pos.lower() != 'all' and nfiles.lower() != 'all':
            for n in range(0, int(nfiles)):
                img = io.imread(filelists[n])
                new_img = (img[int(slice_pos)-1]) #counting starts from 0 in python
                filename = ((filelists[n])[(len(filelists[0])-20):])
                print(f"Reading slice-{slice_pos} of file '...{filename}'")
                img_mean = new_img.mean()  # gets the mean intensity of image
                mean.append(img_mean)                
            #os.makedirs(Dir+'Processed/', exist_ok=True)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice_pos}_from_{nfiles}-files.tif", im_max)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_{nfiles}_files.tif", stack)
            mean_all = np.array([mean])
            results = [mean_all.mean(), mean_all.std()]
    return results

# This will run if no argument is prodived or the argument is not '-a'
if len(sys.argv) < 2 or sys.argv[1] != '-a':
    Dir = (input('Directory>') + '\\')
    filelists = get_filelist(Dir)
    slice_pos = input('slice_position>')
    nfiles = input('How many files to read>')
    results = get_max_limited(filelists, slice_pos, nfiles)
    print(results)
    #print(dir, Dir, '\n', filelists)
#    plt.imshow(result, cmap='gray')
#    plt.show()
elif sys.argv[1] == '-a':
    Dir = (input('Directory>') + '\\')
    tm_int = int(input('Time interval between frames>'))
    filelists = get_filelist(Dir)
    results = get_max_all(filelists)
    #Fig = plt.figure()
    plt.plot(results[0], results[1], 'o', markersize=3)
    plt.errorbar(results[0], results[1], yerr = results[2])
    plt.title('Avrg_int_with_time', fontsize=12)
    #plt.text(0.002,1.035, 'RB', fontsize=12)
    plt.xlabel('Time (min)', fontsize=12)
    plt.ylabel('Average Int, (Gray value)', fontsize=12)
    plt.show()
    plt.close("all")

    print(results[0])
    print(results[1])
    print(results[2])
