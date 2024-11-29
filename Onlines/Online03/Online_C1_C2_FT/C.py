import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 1, 1000)
y = 2*np.sin(14*np.pi*x) - np.sin(2*np.pi*x)*(4*np.sin(2*np.pi*x)*np.sin(14*np.pi*x)-1)


def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    
    # Store the fourier transform results for each frequency. Handle the real and imaginary parts separately
    # use trapezoidal integration to calculate the real and imaginary parts of the FT
    for k,frequency in enumerate(frequencies):
        real = signal*np.cos(2*np.pi*frequency*sampled_times)
        imag = -signal*np.sin(2*np.pi*frequency*sampled_times)
        ft_result_real[k] = np.trapz(real,sampled_times)
        ft_result_imag[k] = np.trapz(imag,sampled_times)
    
    return ft_result_real, ft_result_imag


def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    # Reconstruct the signal by summing over all frequencies for each time in sampled_times.
    # use trapezoidal integration to calculate the real part
    # You have to return only the real part of the reconstructed signal
    for i, time in enumerate(sampled_times):
        real_part = ft_signal[0]*np.cos(2*np.pi*frequencies*time) - ft_signal[1]*np.sin(2*np.pi*frequencies*time)
        reconstructed_signal[i] = np.trapz(real_part, frequencies)
   
    
    return reconstructed_signal


plt.figure(figsize=(12, 4))
plt.plot(x, y, label="Original y ")
plt.title("Original Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

frequencies = np.linspace(-10, 10, 1000)
ft_data = fourier_transform(y,frequencies , x)
magnitude_spectrum = np.sqrt(ft_data[0]**2 + ft_data[1]**2)



plt.figure(figsize=(12, 6))
plt.plot(frequencies, magnitude_spectrum, label="Frequency Spectrum")
plt.title(f"Frequency Spectrum of y = x^2 (Range: {frequencies[0]} to {frequencies[-1]})")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(alpha=0.5)
plt.legend()
plt.show()



def find_peaks(magnitude_spectrum, frequencies,ft_data):
   filtered_ft_data= np.zeros((2, len(frequencies)))
   threshold = 0.5*np.max(magnitude_spectrum)
   print(np.max(magnitude_spectrum))
   print(magnitude_spectrum)
   print(threshold)
   peaks = []
   peak_frequencies = []
   for i in range(1, len(magnitude_spectrum)-1):
        if ((magnitude_spectrum[i] > magnitude_spectrum[i-1]) and (magnitude_spectrum[i] > magnitude_spectrum[i+1]) and (magnitude_spectrum[i] >= threshold)):
            peaks.append(magnitude_spectrum[i])
            peak_frequencies.append(frequencies[i])
            filtered_ft_data[0][i] = ft_data[0][i]
            filtered_ft_data[1][i] = ft_data[1][i]

   return np.array(peaks),np.array(peak_frequencies), filtered_ft_data
            

           
  
peaks, peak_frequencies, filtered_ft_data = find_peaks(magnitude_spectrum, frequencies, ft_data)
print(peaks)
print(peak_frequencies)


index = peak_frequencies>0
positive_freq = peak_frequencies[index]
print(positive_freq)

def f_1(t):
    return np.sin(2*np.pi*positive_freq[0]*t)

def f_2(t):
    return np.sin(2*np.pi*positive_freq[1]*t)

def f_3(t):
    return np.sin(2*np.pi*positive_freq[2]*t)

plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(filtered_ft_data[0]**2 + filtered_ft_data[1]**2))
plt.title("Filtered Frequency Spectrum (Unwanted Frequencies Removed)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()



reconstructed_y = f_1(x) + f_2(x) + f_3(x)


plt.figure(figsize=(12, 6))
plt.plot(x, y, label="Original y", color="blue")
plt.plot(x, reconstructed_y, label="Frequency Spectrum", linestyle="--", color="red")
plt.title(f"Frequency Spectrum of y = x^2 (Range: {frequencies[0]} to {frequencies[-1]})")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(alpha=0.5)
plt.legend()
plt.show()








