
import numpy as np
stack = np.array([[10, 15, 30], [2,3,4]])

"""
#finds the minimum difference between two adjucent elements progresively
print(min([abs(x-y)for x, y in zip(peaks[:-1],peaks[1:])]))
#finds the minimum difference between two pair of elements
print(min([abs(x-y)for x,y in zip(peaks[::2],peaks[1::2])]))

dict_peak = {}
for slice_ in stack:
        print (slice_)
        for t in range(len(slice_)):
                if t in dict_peak:
                        print(slice_[t])
                        # dict_peak[t].append(slice_[t])
                        dict_peak[t].append(100)
                else:
                        dict_peak[t] = slice_[t]
                        print(type(dict_peak[t]))
                        
print(dict_peak)

"""
dict1 = {'0':[10], '1':[20]}
dict2 = {'0':[11], '1':[22]}
for n in dict1:
        dict1[n].append(dict2[n])
        
mn = np.array(dict1['0']).mean()
print(dict1, mn)