from skimage import io
import matplotlib.pyplot as plt
#import numpy as np
#import os

#Dir = input('Dir>')
#FileName = input('filename>')
stack_pos = input('stack_pos>')

new_stack = []
#
#for image in os.listdir(dir):
#    if image.endswith('tif'):
#        images = image
#        #images.append(image)

#im = io.imread(Dir + FileName + '.tif')
im = io.imread('D:/Codes/test.tif')
print(im.shape) # prints the z, y, x dimention of the image file
print(im.shape[0]) # shape[i] where i=0 for Z, i=1 for y and i=2 for x
im_new = (im[int(stack_pos)]) # gets the np array of the image of index i
new_stack.append(im_new)
#io.imshow(im_new) # shows the image
#io.imsave(f"{Dir} {FileName}_slice_{stack_pos}.tif", im_new)
#io.imsave(f"{Dir} {FileName}_slice_{stack_pos}_stack.tif", new_stack)

plt.imshow(im_new, cmap='gray')
plt.show()  # And window will appear
#plt.savefig(dir + 'output.tif')