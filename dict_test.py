
peaks = [10, 15, 30, 50, 52, 70]

peaks_int = [0.5, 0.9, 1.2, 0.1, 1.3, 1.9]

#finds the minimum difference between two adjucent elements progresively
print(min([abs(x-y)for x, y in zip(peaks[:-1],peaks[1:])]))
#finds the minimum difference between two pair of elements
print(min([abs(x-y)for x,y in zip(peaks[::2],peaks[1::2])]))

dict_peak = {}
for (peak_int, peak) in zip(peaks_int, peaks):
        dict_peak[peak_int] = [peak]
vals =dict_peak.keys()
max_val = max(list(vals))
print(max_val, dict_peak[max_val])