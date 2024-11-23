import numpy as np
import matplotlib.pyplot as plt
Range = 10
def fourier_transform(signal, frequencies, sampled_times):
        num_freqs = len(frequencies)
        ft_result_real = np.zeros(num_freqs)
        ft_result_imag = np.zeros(num_freqs)
       
        # Change Here.................................................
        # for frequency in frequencies:
        for i in range(num_freqs):
            # Change Here.................................................

            # dx = (sampled_times[-1] - sampled_times[0])/1000
            dx = (Range - (-Range))/(len(sampled_times)-1)
            y_values_for_ft_real = signal * np.cos(2 * np.pi * frequencies[i] * sampled_times)
            ft_real = np.trapezoid(y_values_for_ft_real, sampled_times, dx)
            y_values_for_ft_img =(-1)* signal * np.sin(2 * np.pi * frequencies[i] * sampled_times)
            ft_img = np.trapezoid(y_values_for_ft_img, sampled_times, dx)
            ft_result_real[i] = ft_real
            ft_result_imag[i] = ft_img
            # Change Here.................................................

            # i += 1
            # Store the fourier transform results for each frequency. Handle the real and imaginary parts separately
        # use trapezoidal integration to calculate the real and imaginary parts of the FT

        return ft_result_real, ft_result_imag
def inverse_fourier_transform(ft_signal, frequencies, sampled_times):
        n = len(sampled_times)
        reconstructed_signal = np.zeros(n)
        
        # Reconstruct the signal by summing over all frequencies for each time in sampled_times.
        # use trapezoidal integration to calculate the real part
        # You have to return only the real part of the reconstructed signal
        for i in range(n):
            # for j in range(len(frequencies)):
            # Change Here.................................................

            df = (frequencies[-1] - frequencies[0])/(len(frequencies)-1)
            y_values_for_ift_real = (ft_signal[0] * np.cos(2 * np.pi * frequencies * sampled_times[i]) - ft_signal[1] * np.sin(2 * np.pi * frequencies * sampled_times[i]))
            reconstructed_signal[i] = np.trapezoid(y_values_for_ift_real, frequencies, df)
        return reconstructed_signal

def plot_ft(ft_data, frequencies):
     #  plot the FT data
    # label, title =  get_label_title(function_type)
   
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, np.sqrt(ft_data[0]**2 + ft_data[1]**2))
    # plt.title("Frequency Spectrum of "+title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    # plt.show()
    plt.legend()
    plt.savefig('frequency_spectrum.png')
def plot_reconstructed(x_values,y_values):
    plt.figure(figsize=(12, 4))
    plt.plot(x_values,y_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("reconstructed_freq_new.png") 
def main():
    x_values = np.linspace(-Range,Range,1000)
    y_values = 2*np.sin(14*np.pi*x_values) - np.sin(2*np.pi*x_values)*(4*np.sin(2*np.pi*x_values)*np.sin(14*np.pi*x_values) -1)
    plt.plot(x_values,y_values)
    plt.legend()
    plt.savefig("Original_function.png")
    frequencies = np.linspace(-Range,Range,200)
    Ft_data = fourier_transform(y_values,frequencies,x_values) 
    plot_ft(Ft_data,frequencies)
    # y_value1 = np.sin(-5*2*np.pi*x_values)
    y_value1 = np.zeros(len(x_values))
    y_value2 = np.sin(9*2*np.pi*x_values)
    y_value3 = np.sin(1*2*np.pi*x_values)
    y_value4 = np.sin(5*2*np.pi*x_values)
    y_value5 =  y_value1 + y_value2 + y_value3 + y_value4
    plot_reconstructed(x_values,y_value5)
    # reconstructed_y_values = inverse_fourier_transform(Ft_data,frequencies,x_values)
    # plt.plot(x_values,reconstructed_y_values)
    # plt.savefig("Reconstructed.png")
if __name__ == "__main__":
    main()