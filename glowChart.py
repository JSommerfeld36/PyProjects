#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:24:40 2023

@author: joelsommerfeld
"""

import matplotlib.pyplot as plt
import mplcyberpunk
import pandas as pd

df = pd.read_csv('/Users/joelsommerfeld/Downloads/AR TEST/Results/BarPink_spattemp copy.csv')

def splitSerToArr(ser):
    return [ser.index, ser.to_numpy()]

xs = range(57)

series1 = df['Left']
series2 = df['Right']
s1 = pd.Series(series1, index=xs)
s2 = pd.Series(series2, index=xs)

plt.style.use("cyberpunk")
plt.plot( *splitSerToArr(s1.dropna()), linestyle='-', marker='o')
plt.plot( *splitSerToArr(s2.dropna()), linestyle='-', marker='o')
#plt.legend(['Right Leg', 'Left Leg'])
#plt.title('Stride Time Intervals')
plt.ylabel('Stride Time (s)', fontsize = 15 )
plt.xlabel('Stride Number', fontsize = 15 )
mplcyberpunk.make_lines_glow()
plt.axis('off')
plt.grid(b=None)
plt.show()




import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk

Fs = 8000
f = 5
sample = 12000
x = np.arange(sample)

y = 2 * np.sin(1 * np.pi * f * x / Fs) # blue
z = 1.4 * np.sin(0.4 * np.pi * 7 * x / Fs) # pink
s = 0.6 * np.sin(4 * np.pi * 3 * x / Fs) # yellow
b = np.cos(2 * 0.4 * 3 * x / 2500) # green
c = 0.2 * np.cos(2 * 0.4 * 9 * x / 2500) # red


plt.style.use("cyberpunk")
plt.plot(y)
plt.plot(z)
plt.plot(s)
plt.plot(b)
plt.plot(c)
mplcyberpunk.make_lines_glow()
plt.axis('off')
plt.grid(b=None)
plt.show()


# import electrocardiogram
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
  
# import numpy
import numpy as np
  
# define electrocardiogram as ecg model
ecg = electrocardiogram()
  
# frequency is 360
frequency = 360
  
# calculating time data with ecg size along with frequency
time_data = np.arange(ecg.size) / frequency
  
import mplcyberpunk

# plotting time and ecg model
plt.style.use("cyberpunk")
plt.plot(time_data, ecg)
plt.xlim(10, 13.5)
plt.ylim(-1.2, 1.5)
mplcyberpunk.make_lines_glow()
plt.axis('off')
plt.grid(b=None)
# display
plt.show()


import matplotlib.pyplot as plt
import mplcyberpunk
import pandas as pd
from scipy import signal
import numpy as np

df = pd.read_csv('/Users/joelsommerfeld/Downloads/S019_Zephyr_Breathing_2018-01-23-06-43-09-PST (1).csv')

breath = df[41931: 42904]
raw_dat = breath['BreathingWaveform']


fs = 25
fc = 2  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(5, w, 'low')
filtered = signal.filtfilt(b, a, raw_dat)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False)
ax1.plot(raw_dat)
ax1.set_title("Raw Signal")

ax2.plot(filtered)
ax2.set_title('Filtered Data')
plt.tight_layout()
plt.show()


plt.style.use("cyberpunk")
plt.plot(filtered)
plt.ylim(7255800, 7276800)
mplcyberpunk.make_lines_glow()
plt.axis('off')
plt.grid(b=None)
plt.show()


# I want the walking yellow and green - done
# I want the breathing blue
# I want the heart red - done
# I want the brain pink, purple,  

