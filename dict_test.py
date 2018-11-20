
peaks = [10, 15, 30, 50]

peaks_int = [0.5, 0.9, 1.2, 0.1]

dict_peak = {}
for (peak_int, peak) in zip(peaks_int, peaks):
        dict_peak[peak_int] = [peak]
vals =dict_peak.keys()
max_val = max(list(vals))
print(max_val, dict_peak[max_val])