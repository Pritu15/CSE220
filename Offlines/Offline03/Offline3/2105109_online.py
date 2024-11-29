import numpy as np
import matplotlib.pyplot as plt

# Define the interval and function and generate appropriate x values and y values
x_values = np.linspace(-5, 5, 1000)
# y_values = np.where((x_values >= -2) & (x_values <= 2), x_values**2, 0)
# Triangular wave
# y_values = np.piecewise(
#     x_values,
#     [x_values < -2, (x_values >= -2) & (x_values < 0), (x_values >= 0) & (x_values <= 2), x_values > 2],
#     [0, lambda x: (x + 2) / 2, lambda x: (2 - x) / 2, 0]
# )

#Sawtooth
y_values = np.piecewise(
    x_values,
    [x_values < -3, (x_values >= -3) & (x_values <= -1),(x_values >= -1) & (x_values <= 0),(x_values >=0) & (x_values <= 1),(x_values >=1) & (x_values <= 3) ,x_values > 3],
    [0, lambda x: (-4/x),lambda x: x + 5,lambda x: -x + 5,lambda x: 4/x, 0]
)


#Rectangular
# y_values = np.piecewise(
#     x_values,
#     [x_values < -2, (x_values >= -2) & (x_values <= 2), x_values > 2],
#     [0, 1, 0]
# )

plt.plot(x_values,y_values)

# Plot the original function
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2")
plt.title("Original Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



# Define the sampled times and frequencies
sampled_times = x_values
frequencies = np.linspace(-10, 10, 1000)

# Fourier Transform 
def fourier_transform(signal, frequencies, sampled_times):
    num_freqs = len(frequencies)
    ft_result_real = np.zeros(num_freqs)
    ft_result_imag = np.zeros(num_freqs)
    for i, freq in enumerate(frequencies):
        cos_term = np.cos(-2 * np.pi * freq * sampled_times)
        sin_term = np.sin(-2 * np.pi * freq * sampled_times)

        ft_result_real[i] = np.trapz(signal * cos_term, sampled_times)
        ft_result_imag[i] = np.trapz(signal * sin_term, sampled_times)
    
    # Store the fourier transform results for each frequency. Handle the real and imaginary parts separately
    # use trapezoidal integration to calculate the real and imaginary parts of the FT

    return ft_result_real, ft_result_imag

# Apply FT to the sampled data
ft_data = fourier_transform(y_values, frequencies, sampled_times)
#  plot the FT data
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
plt.title("Frequency Spectrum of y = x^2")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()


# Inverse Fourier Transform 
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
    ft_real, ft_imag = ft_signal
    n = len(sampled_times)
    reconstructed_signal = np.zeros(n)
    for i, t in enumerate(sampled_times):
        # Compute the real part of the reconstructed signal
        cos_term = np.cos(2 * np.pi * frequencies * t)
        sin_term = np.sin(2 * np.pi * frequencies * t)
        real_part = ft_real * cos_term - ft_imag * sin_term
        reconstructed_signal[i] = np.trapz(real_part, frequencies)
    # Reconstruct the signal by summing over all frequencies for each time in sampled_times.
    # use trapezoidal integration to calculate the real part
    # You have to return only the real part of the reconstructed signal
    
    return reconstructed_signal

def persevals_Theorem (frequencies,sampled_times):
    y_values =np.abs( np.piecewise(
    x_values,
    [x_values < -3, (x_values >= -3) & (x_values <= -1),(x_values >= -1) & (x_values <= 0),(x_values >=0) & (x_values <= 1),(x_values >=1) & (x_values <= 3) ,x_values > 3],
    [0, lambda x: (-4/x),lambda x: x + 5,lambda x: -x + 5,lambda x: 4/x, 0]
    )**2)
    ft_data1 = np.trapz(y_values, sampled_times)
    y_values = np.piecewise(
    x_values,
    [x_values < -3, (x_values >= -3) & (x_values <= -1),(x_values >= -1) & (x_values <= 0),(x_values >=0) & (x_values <= 1),(x_values >=1) & (x_values <= 3) ,x_values > 3],
    [0, lambda x: (-4/x),lambda x: x + 5,lambda x: -x + 5,lambda x: 4/x, 0])
    ft_data2=fourier_transform(y_values,frequencies,sampled_times)
    ft_data4=ft_data2[0]**2 + ft_data2[1]**2
    ft_data3=np.trapz(ft_data4,frequencies)
    print(ft_data1)
    print(ft_data3)
    
    flag=0

    if ft_data3!=ft_data1:
            
           print("NOT Maintaining Theorem")
        
    else :
        print("Parseval's Theorem Maintaing")
        
        
persevals_Theorem(frequencies,sampled_times)
    
    
    

# Reconstruct the signal from the FT data
reconstructed_y_values = inverse_fourier_transform(ft_data, frequencies, sampled_times)
# Plot the original and reconstructed functions for comparison
plt.figure(figsize=(12, 4))
plt.plot(x_values, y_values, label="Original y = x^2", color="blue")
plt.plot(sampled_times, reconstructed_y_values, label="Reconstructed y = x^2", color="red", linestyle="--")
plt.title("Original vs Reconstructed Function (y = x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
