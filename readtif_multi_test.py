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









# This function gives out of the MAX projection of all the individual slices
# from all the files in the above list of files
def get_max_all(filelists):
    img = io.imread(filelists[0])
    mean = []
    mean_all_tm_points = []
    std_all_tm_points = []
    se_all = []
    tm_points =[]
    #print('image_shape:', img.shape[0])
    if len(img.shape) < 3:
        print('\nImage is not a stack! Please choose a stack of images.')
        result = img
        return result
    else:
        stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), img.dtype)
        stack1 = np.zeros((len(filelists), img.shape[1], img.shape[2]), dtype=np.uint32)
        for slice in range(0, img.shape[0]):
            slice_tm = slice*tm_int
            tm_points.append(slice_tm)
            for n in range(0, len(filelists)):
                img = io.imread(filelists[n])
                new_img = (img[int(slice)]) #counting starts from 0 in python
                filename = ((filelists[n])[(len(filelists[0])-20):])
                print(f"Reading slice-{slice+1} of file ..{filename}")
                stack[n, :, :] = new_img
                stack1[n, :, :] = new_img
                img_mean = new_img.mean()  # gets the mean intensity of slice
                mean.append(img_mean)
            im_max = np.max(stack, axis = 0)
            im_mean = np.mean(stack1, axis = 0)
            mean_all = np.array([mean]) # making numpy array of all the means
            mean_all_tm_points.append(mean_all.mean())
            std_all_tm_points.append(mean_all.std())
            se_all.append((mean_all.std()/math.sqrt(len(filelists))))

        results = np.array([tm_points, mean_all_tm_points, std_all_tm_points, se_all])
        try:
            os.makedirs(Dir+'Processed/', exist_ok=True)
            np.savetxt(f"{Dir}Processed/Results_from_{len(filelists)}-files.csv",
                       results.T, delimiter=",", header='Time, Avrg_int, Std, SE')
            io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice+1}_from_{len(filelists)}-files.tif", im_max)
            io.imsave(f"{Dir+'Processed/'}Mean_stack_of_slice-{slice+1}_from_{len(filelists)}-files.tif", im_mean)
        except:
            print("Existing results file is not accessible!")

        return im_max

# This function gives out of the MAX projection of selective slices
# from selective/all the files in the above list of files
def get_max_limited(filelists, slice_pos, nfiles):
    img = io.imread(filelists[0])
    #print('image_shape:', img.shape)
    if len(img.shape) < 3:
        print('\nImage is not a stack! Please choose a stack of images.')
        result = img
        return result
    else:
        stack = np.zeros((len(filelists), img.shape[1], img.shape[2]), img.dtype)
        if slice_pos.lower() != 'all' and nfiles.lower() == 'all':
            for n in range(0, len(filelists)):
                img = io.imread(filelists[n])
                new_img = (img[int(slice_pos)-1]) #counting starts from 0 in python
                print(f"reading file no.{n+1}")
                stack[n, :, :] = new_img
            im_max= np.max(stack, axis=0)
            os.makedirs(Dir+'Processed/', exist_ok=True)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_{len(filelists)}_files.tif", stack)
            io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice_pos}_from_{len(filelists)}-files.tif", im_max)

        elif slice_pos.lower() != 'all' and nfiles.lower() != 'all':
            for n in range(0, int(nfiles)):
                img = io.imread(filelists[n])
                new_img = (img[int(slice_pos)-1]) #counting starts from 0 in python
                print(f"reading file no.{n+1}")
                stack[n, :, :] = new_img
            im_max= np.max(stack, axis=0)
            os.makedirs(Dir+'Processed/', exist_ok=True)
            io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice-{slice_pos}_from_{nfiles}-files.tif", im_max)
            #io.imsave(f"{Dir+'Processed/'}Max_stack_of_slice_{slice_pos}_{nfiles}_files.tif", stack)

    return im_max

if __name__ == "__main__":
    # This will run if no argument is prodived or the argument is not '-a'
    if len(sys.argv) < 2 or sys.argv[1] != '-a':
        Dir = (input('Directory>') + '\\')
    #    Dir = dir.replace('\\', '/')
        filelists = get_filelist(Dir)
        slice_pos = input('slice_position>')
        nfiles = input('How many files to read>')
        result = get_max_limited(filelists, slice_pos, nfiles)
    #    plt.imshow(result, cmap='gray')
    #    plt.show()
    elif sys.argv[1] == '-a':
        Dir = (input('Directory>') + '\\')
        tm_int = int(input('Time interval between frames>'))
        filelists = get_filelist(Dir)
        results = get_max_all(filelists)

        fig = plt.figure()
        plt.errorbar(results[0], results[1], yerr = results[2], fmt='rs-', linewidth=2, markersize=5, figure = fig)
        plt.title('Avrg_int_with_time', fontsize=12)
        plt.xlabel('Time (min)', fontsize=12)
        plt.ylabel('Average Int, (Gray value)', fontsize=12)
        plt.savefig(f"{Dir}Processed/Avrg_int_with_std_from_{len(filelists)}-files.png")
        plt.show()

        fig = plt.figure()
        plt.errorbar(results[0], results[1], yerr = results[3], fmt='rs-', linewidth=2, markersize=5, figure = fig)
        plt.title('Avrg_int_with_time', fontsize=12)
        plt.xlabel('Time (min)', fontsize=12)
        plt.ylabel('Average Int, (Gray value)', fontsize=12)
        plt.savefig(f"{Dir}Processed/Avrg_int_with_SE_from_{len(filelists)}-files.png")
        plt.show()

        #fig.close()
        plt.close("all")

