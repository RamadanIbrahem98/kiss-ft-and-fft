from CPP import CPP
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error



a = CPP('./library.so')

dft_N = np.arange(1, 5000, 100)
dft_times = []
for x in dft_N:
    dft, timing = a.get_dft(x)
    dft_times.append(timing)

fft_N = np.arange(1, 5_00_000, 80_000)
fft_times = []
for x in fft_N:
    fft, timing = a.get_fft(x)
    fft_times.append(timing)

dft, timing = a.get_dft(1024)
fft, timing = a.get_fft(1024)


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, constrained_layout=True, sharey=False)
ax1.plot(dft_N, dft_times)
ax1.set_title('DFT Time Complixity')
ax1.set_xlabel('Length of input Array (N)')
ax1.set_ylabel('time (ms)')

ax2.plot(fft_N, fft_times)
ax2.set_title('FFT Time Complixity')
ax2.set_xlabel('Length of input Array (N)')
ax2.set_ylabel('time (ms)')

ax3.plot(fft, dft)
ax3.set_title('FFT vs DFT Output')
ax3.set_xlabel('FFT')
ax3.set_ylabel('DFT')

x = mean_squared_error(fft, dft)
fig.suptitle(f'Difference Between DFT and FFT Complixty\nMean Squared Error is: {x}', fontsize=16)
plt.show()
