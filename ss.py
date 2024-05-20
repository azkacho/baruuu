import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

# signal with samping rate of 2000Hz – freq_max = 1000Hz
# Nyquist's theorem requires sampling freq > 2x the signal's max freq

t = np.linspace(0, 1.0, 2001)
sig_5hz = np.sin(2 * np.pi * 5 * t)  # sin(2π⋅f⋅t) 5 gelombang dalam 1 detik
sig_50hz = np.sin(2 * np.pi * 50 * t)
sig_250hz = np.sin(2 * np.pi * 250 * t)

sig_5hz_50hz_250hz = sig_5hz + sig_50hz  + sig_250hz

plt.plot(sig_5hz_50hz_250hz)
plt.show

# these are parameters to make the filters
numtaps = 101       # jumlah ordo
lpf_cutoff = 7      # the lowpass filter with fc= 7 Hz (yang diiteruskan hanya dibawah 7 Hz)
hpf_cutoff = 100    # the highpass filter with fc= 100 Hz
bp_cutoff1 = 40     # the bandpass filter with fc= 40 Hz - 100 Hz
bp_cutoff2 = 100

# calculate the lowpass coeffs using window method
from scipy.signal import firwin
lowpass_coef = firwin(numtaps, lpf_cutoff, fs=1000, pass_zero=True) 
# True defaultnya untuk membuat lpf atau bandstop
# False untuk membuat hpf atau band pass
plt.plot(lowpass_coef)
plt.show()

# convolve the signal with the lowpass coeffs
from scipy.signal import convolve
lowpass_output = convolve(sig_5hz_50hz_250hz, lowpass_coef, mode='same')
plt.plot(lowpass_output)
plt.show()


# calculate the highpass coeffs using window method
from scipy.signal import firwin
highpass_coef = firwin(numtaps, hpf_cutoff, fs=sampling_rate, pass_zero=False)
plt.plot(highpass_coef)
plt.show()

# convolve the signal with highpass coeffs
from scipy.signal import convolve
highpass_output = convolve(sig_5hz_50hz_250hz, highpass_coef, mode='same')
plt.plot(highpass_output)
plt.show()


# calculate the bandpass coeffs using window method
from scipy.signal import firwin
bandpass_coef = firwin(numtaps, [bp_cutoff1, bp_cutoff2], fs=sampling_rate, pass_zero=False)
plt.plot(bandpass_coef)
plt.show()

# convolve the signal with bandpass coeffs
from scipy.signal import convolve
bandpass_output = convolve(sig_5hz_50hz_250hz, bandpass_coef, mode='same')
plt.plot(bandpass_output)
plt.show()


# calculate the bandstop coeffs using window method
from scipy.signal import firwin
bs_cutoff1 = 40  # batas bawah frekuensi potong untuk bandstop filter
bs_cutoff2 = 100  # batas atas frekuensi potong untuk bandstop filter
bandstop_coef = firwin(numtaps, [bs_cutoff1, bs_cutoff2], fs=sampling_rate, pass_zero=False)
plt.plot(bandstop_coef)
plt.show()

