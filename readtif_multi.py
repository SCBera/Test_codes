# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:02:20 2018

@author: admin
"""
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import glob
#import sys

#files = glob.glob(Dir+filetype)
#print(files)
def get_dir(dir_):
    dir_ = dir_ + "\\"
    return dir_

def dir_out(dir_in):
    try:
        os.makedirs(dir_ + '_out/', exist_ok=True)
        dir_out = (dir_ + '_out/')
        return dir_out
    except:
        print("Ploblem with making new directory!")


# This gets the lists of files in the directory given (excluding the first file)
def get_filelist(dir_, filetype='*.tif'):
    files = glob.glob(dir_ + filetype)
    del files[0] # deletes first file form the list
    files_mod = files
    return files_mod

def read_stack(file):
    image = io.imread(file)
    return image

def read_slice_t(image, t):
    slice_t = image[t]
    return slice_t

def get_max(stack):
    stack_max = np.max(stack, axis = 0)
    return stack_max

def get_mean(stack):
    stack_mean = np.mean(stack, axis = 0)
    return stack_mean

def save_tif(dir_out, list_of_files, slice_t, result, mode):
    try:
        io.imsave(f"{dir_out}{mode}_of_slice-{slice_t + 1}_from_{len(list_of_files)}-files.tif", result)
    except:
        print("Existing image file is not accessible!")

def save_csv(dir_out, list_of_files, result):
    try:
        np.savetxt(f"{dir_out}Results_from_{len(list_of_files)}-files.csv",
                   result.T, delimiter=",", header='Time, Avrg_int, SD, SE')
    except:
        print("Existing csv file is not accessible!")

def plot_save_fig(dir_out, filelists, results):
    try:
        fig = plt.figure()
        plt.errorbar(results[0], results[1], yerr = results[2], fmt='rs-', linewidth=2, markersize=5, figure = fig)
        plt.title('Avrg_int_with_time, SD', fontsize=12)
        plt.xlabel('Time (min)', fontsize=12)
        plt.ylabel('Average Int, (Gray value)', fontsize=12)
        plt.savefig(f"{dir_out}Avrg_int_with_std_from_{len(filelists)}-files.png")
        plt.show()
        plt.close()

        fig = plt.figure()
        plt.errorbar(results[0], results[1], yerr = results[3], fmt='rs-', linewidth=2, markersize=5, figure = fig)
        plt.title('Avrg_int_with_time, SEM', fontsize=12)
        plt.xlabel('Time (min)', fontsize=12)
        plt.ylabel('Average Int, (Gray value)', fontsize=12)
        plt.savefig(f"{dir_out}Avrg_int_with_SE_from_{len(filelists)}-files.png")
        plt.show()
        plt.close()

    except:
        print("Problem with saving figure!")




if __name__ == "__main__":
    dir_ = get_dir(input("Directory>"))
    t = input("Time point/interval>")
    list_of_files = get_filelist(dir_)
    img = read_stack(list_of_files[0])
    new_stack = np.zeros((len(list_of_files), img.shape[1], img.shape[2]), img.dtype)
    list_of_mean = []
    list_of_sd = []
    list_of_sem = []
    t_points = []
    dir_out = dir_out(dir_)

    for slice_t in range(0, img.shape[0]):
        t_points.append(slice_t * float(t))
        for n in range(0, len(list_of_files)):
            img = read_stack(list_of_files[n])
            if img.shape[0] < 3:
                continue
            frame = read_slice_t(img, slice_t)
            # making a new set of stacks for each time point
            new_stack[n, :, :]= frame
            # saving the newly made stack
#            save_tif(dir_out, list_of_files, slice_t, new_stack)

        list_of_mean.append(new_stack.mean())
        list_of_sd.append(new_stack.std())
        list_of_sem.append(new_stack.mean()/math.sqrt(len(list_of_files)))

        mean_of_stacks = np.mean(new_stack, axis = 0)

        max_of_stacks = np.max(new_stack, axis = 0)
        # saving the mean of the stacks
        save_tif(dir_out, list_of_files, slice_t, max_of_stacks, 'Max')
#        save_tif(dir_out, list_of_files, slice_t, mean_of_stacks, 'Mean')
        result_csv = np.array([t_points, list_of_mean, list_of_sd, list_of_sem])

        print(new_stack.mean(), t_points)
    save_csv(dir_out, list_of_files, result_csv)
    plot_save_fig(dir_out, list_of_files, result_csv)





















