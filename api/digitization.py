import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import thinning
import main

# Constants
# ld = 0.00635  # Amplitude adjustment factor (commented out in your code)
ld = 0.0483  # Assuming 600dpi mm (dots per inch)
target1R = 0

# Assuming 'k' is already defined as in your previous code

# Find the indices where k equals target1R
matches1 = main.k == target1R
x1, y1 = np.where(matches1)

# Create a data matrix
DATA = np.column_stack((y1, x1))

# Remove duplicate rows based on the first column (y1)
temp = np.unique(DATA, axis=0)

temp2 = np.zeros_like(temp)
temp2[0] = temp[0]

jj = 1
for ii in range(1, len(temp)):
    if temp[ii, 0] == temp[ii - 1, 0]:
        continue
    if ii < len(temp) - 1 and temp[ii, 0] == temp[ii + 1, 0]:
        temp2[jj, 0] = temp[ii, 0]
        temp2[jj, 1] = max(temp[ii, 1], temp[ii + 1, 1])
    else:
        temp2[jj, 0] = temp[ii, 0]
        temp2[jj, 1] = temp[ii, 1]
    jj += 1

Sample_Crop = temp2[:, 1] * ld
MAX = np.max(Sample_Crop)
MIN = np.min(Sample_Crop)
media = np.median(Sample_Crop)
Sample_Crop = Sample_Crop - media
TG = MAX - MIN
fs = 23

# Plot the Sample_Crop data
plt.figure()
plt.plot(np.arange(len(Sample_Crop)) / fs, Sample_Crop)
plt.grid(True)
plt.xlabel('Period (mm)')
plt.ylabel('Amplitude (mm)')
plt.show()

# Find peaks in Sample_Crop
peak_indices, _ = find_peaks(Sample_Crop, height=np.mean(Sample_Crop), distance=60)

# Save Sample_Crop to a CSV file
np.savetxt('test.dat', Sample_Crop, delimiter=',')

# Plot peaks
plt.figure()
plt.plot(Sample_Crop)
plt.plot(peak_indices, Sample_Crop[peak_indices], 'ro')
plt.xlabel('Sample_Crop Index')
plt.ylabel('Amplitude (mm)')
plt.show()

# You'll need to implement or import the 'scale' and 'amplitude' functions, as they are not provided in the code.
# sf2(Sample_Crop)  # Uncomment if 'sf2' function is defined
# D = np.loadtxt('Book1.csv', delimiter=',')  # Uncomment if reading data from a CSV file
