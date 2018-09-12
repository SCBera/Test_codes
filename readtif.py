from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os

dir = input('Dir>')


##Dir = input('Dir>')
##FileName = input('filename>')
stack_pos = input('stack_pos>')
number_of_files = input('How many files to read>')

listfiles = []
for img_files in os.listdir(dir): # gets the file names
    if img_files.endswith(".tif") and len(listfiles) < int(number_of_files):
        listfiles.append(img_files) # lists all the file names

print(len(listfiles))
print(listfiles)

img = io.imread(dir + listfiles[1])
io.imshow(img[int(stack_pos)])

stack = np.zeros((number_of_files,img.shape[1],img.shape[2],np.uint8)

for n in range(0,len(listfiles)):
    stack[n,:,:,:]= io.imread(dir+listfiles[n])

io.imshow(stack[0])

path_results = '..Part_A_Results/'
io.imsave(path_results+'Stack_1.tif',stack)

#new_stack = []
#
#
#
##for image in os.listdir(dir):
##    if image.endswith('tif'):
##        images = image
##        #images.append(image)
#
#im = io.imread(Dir + FileName + '.tif')
#im = io.imread('D:/Codes/test.tif')
#print(im.shape) # prints the z, y, x dimention of the image file
##print(im.shape[0]) # shape[i] where i=0 for Z, i=1 for y and i=2 for x
#im_new = (im[int(stack_pos)]) # gets the np array of the image of index i
##io.imshow(im_new) # shows the image
##io.imsave(f"{Dir} {FileName}_slice_{stack_pos}.tif", im_new)
##io.imsave(f"{Dir} {FileName}_slice_{stack_pos}_stack.tif", new_stack)
#

#
#plt.imshow(im_new, cmap='gray')
#plt.show()  # And window will appear
##plt.savefig(dir + 'output.tif')