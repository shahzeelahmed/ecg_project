


import numpy as np
import matplotlib.pyplot as plt

def amplitude(signal, sampleRate):
    # Find local maximum peaks
    maxPeaks = (signal[1:-1] > signal[:-2]) & (signal[1:-1] > signal[2:])
    maxPeaks = np.pad(maxPeaks, (1, 1), 'constant', constant_values=(False, False))

    # Find local minimum peaks
    minPeaks = (signal[1:-1] < signal[:-2]) & (signal[1:-1] < signal[2:])
    minPeaks = np.pad(minPeaks, (1, 1), 'constant', constant_values=(False, False))

    # Find the index of the highest peak
    maxIndex = np.argmax(signal)

    # Find the index of the lowest peak
    minIndex = np.argmin(signal)

    # Adjust the highest peak by adding 1 and the lowest peak by subtracting 1
    adjustedSignal = signal.copy()
    adjustedSignal[maxIndex] += 1
    adjustedSignal[minIndex] -= 1

    # Convert amplitude from millimeters to voltage (10 mm = 1 mV)
    adjustedSignal = adjustedSignal / 10

    # Time scale in milliseconds
    timeScale = np.arange(len(signal)) / sampleRate

    # Plot the adjusted signal
    plt.figure()
    plt.plot(timeScale, adjustedSignal)
    plt.grid(True)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (mV)')
    plt.title('Adjusted Signal')
    plt.show()

    return adjustedSignal, timeScale


