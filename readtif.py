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

dir = input('Dir>')
Dir = dir.replace('\\', '/')
# print(dir)
# print(Dir)

stack_pos = input('stack_position>')
number_of_files = input('How many files to read>')

listfiles = []
for img_files in os.listdir(dir):  # gets the file names
    if img_files.endswith(".tif") and len(listfiles) < int(number_of_files):
        listfiles.append(img_files)  # lists all the file names
    # elif len(listfiles) < int(number_of_files) and not img_files.endswith(".tif"):
    #     print("There is no tif image!")
    # else:
    #     print("There is no tif image or file input shoud be more than zero!")


# print(len(listfiles))
#print(listfiles)

img = io.imread(Dir+listfiles[0])
#im_new = (img[int(stack_pos)])  # gets the np array of the image of index i
#print(im_new)
# io.imshow(img[int(stack_pos)])

stack = np.zeros((int(number_of_files), img.shape[1], img.shape[2]), np.uint16)
#stack = np.zeros((int(number_of_files), img.shape[1], img.shape[2]), np.float32)


for n in range(0, len(listfiles)):
    img = io.imread(Dir+listfiles[n])
    new_img = (img[int(stack_pos)])
    #print(new_img)
    stack[n, :, :] = new_img


print('stack shape:', stack.shape) #prints the z, y, x dimention of the image file
#print('stack size:', stack.size) # multiplication of z, y and x values
im_max= np.max(stack, axis=0)
plt.imshow(im_max)

#img_stack = io.imread(stack)
#im_new_stack = (img_stack[0])
#print(stack[0])

# path_results = '..Part_A_Results/'
#io.imsave(f"{Dir}Stack_of_slice_{stack_pos}_first_{number_of_files}_files.tif", stack)
io.imsave(f"{Dir}Max_stack_of_slice_{stack_pos}_first_{number_of_files}_files.tif", im_max)



#im = io.imread(Dir + FileName + '.tif')
#im = io.imread('D:/Codes/test.tif')
#print(img.shape) # prints the z, y, x dimention of the image file
#print(im_new.shape) # prints the z, y, x dimention of the image file
#print(im.shape[0]) # shape[i] where i=0 for Z, i=1 for y and i=2 for x

#io.imshow(im_new) # shows the image
#io.imsave(f"{Dir} {listfiles[1]}_slice_{stack_pos}.tif", im_new)
#io.imsave(f"{Dir} {FileName}_slice_{stack_pos}_stack.tif", new_stack)
#

#
#plt.imshow(im_new, cmap='gray')
# plt.show()  # And window will appear
##plt.savefig(dir + 'output.tif')
