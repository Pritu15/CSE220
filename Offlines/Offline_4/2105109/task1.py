import numpy as np
import matplotlib.pyplot as plt
n=50
samples = np.arange(n) 
sampling_rate=100
wave_velocity=8000



#use this function to generate signal_A and signal_B with a random shift
def generate_signals(frequency=5):

    noise_freqs = [15, 30, 45]  # Default noise frequencies in Hz

    amplitudes = [0.5, 0.3, 0.1]  # Default noise amplitudes
    noise_freqs2 = [10, 20, 40] 
    amplitudes2 = [0.3, 0.2, 0.1]
    
     # Discrete sample indices
    dt = 1 / sampling_rate  # Sampling interval in seconds
    time = samples * dt  # Time points corresponding to each sample

    # Original clean signal (sinusoidal)
    original_signal = np.sin(2 * np.pi * frequency * time)

    # Adding noise
    noise_for_sigal_A = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                for noise_freq, amplitude in zip(noise_freqs, amplitudes))
    noise_for_sigal_B = sum(amplitude * np.sin(2 * np.pi * noise_freq * time)
                for noise_freq, amplitude in zip(noise_freqs2, amplitudes2))
    signal_A = original_signal + noise_for_sigal_A 
    noisy_signal_B = signal_A + noise_for_sigal_B

    # Applying random shift
    shift_samples = np.random.randint(-n // 2, n // 2)  # Random shift
    print(f"Shift Samples: {shift_samples}")
    signal_B = np.roll(noisy_signal_B, shift_samples)
    
    return signal_A, signal_B

#implement other functions and logic
def DFT(signal):
    length=signal.size
    result=np.zeros(length,dtype=complex)
    for k in range(length):
        for n in range(length):
            result[k]+=signal[n]*np.exp(-1j*np.pi*k*2*n/length)
    return result
def IDFT(signal):
    length=signal.size
    result=np.zeros(length,dtype=complex)
    for n in range(length):
        for k in range(length):
            result[n]+=signal[k]*np.exp(1j*np.pi*k*2*n/length)
        result[n]=result[n]/length
    return result
def Cross_Correlation_Calculation(signalA,signalB):
    resultA=DFT(signalA)
    resultB=DFT(signalB)
    conjugateB=np.conj(resultB)
    cross_co_omega=resultA*conjugateB
    result=IDFT(cross_co_omega)
    return np.real(result)
def Sample_Lag_Detection(signal):
    max_index=np.argmax(signal)
    
    if (max_index >= n//2):
        max_index = max_index - len(signal)
        
    return max_index
def  Distance_Estimation(lag):
    answer=lag*wave_velocity/sampling_rate
    return answer
def plot_original_signal(signal, title, color):
    
    plt.figure(figsize=(5, 6))
    plt.stem(samples, signal, linefmt=color, markerfmt=color, basefmt=" ")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.show()
    print("Distance is: ")
    print(Distance_Estimation(Sample_Lag_Detection(signal)))

def plot_magnitude_spectrum(dft_signal, title, color):
    """
    Plot the magnitude spectrum of a signal in the frequency domain.

    Parameters:
    dft_signal (array-like): The DFT-transformed signal.
    title (str): The title of the plot.
    color (str): The color for the stem plot.

    Returns:
    None
    """
    magnitudes = np.abs(dft_signal)
    plt.figure(figsize=(8, 6))
    plt.stem(np.arange(n), magnitudes, linefmt=color, markerfmt=color, basefmt=" ")
    plt.xlabel("Frequency Bin")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.show()


def plot_cross_correlation_discrete(signal, title="Cross-Correlation (Discrete)", color="blue"):
    """
    Plot the cross-correlation signal as a discrete stem plot.

    Parameters:
    signal (array-like): The cross-correlation signal to be plotted.
    title (str): The title of the plot.
    color (str): The color for the stem plot.

    Returns:
    None
    """
    lags = np.arange(-len(signal) // 2, len(signal) // 2)
    plt.figure(figsize=(8, 6))
    plt.stem(lags, np.roll(signal,len(signal)//2), linefmt=color, markerfmt=color, basefmt=" ")
    plt.xlabel("Lag (samples)")
    plt.ylabel("Correlation")
    plt.title(title)
    plt.grid()
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.show()


#*********************MAIN******************************

signalA, signalB = generate_signals()

plot_original_signal(signalA, "Signal A (Station A)", "blue")

DFT_Signal_A = DFT(signalA)
plot_magnitude_spectrum(DFT_Signal_A, "Magnitude Spectrum of Signal A", "blue")

plot_original_signal(signalB, "Signal B (Station B)", "red")

DFT_Signal_B = DFT(signalB)
plot_magnitude_spectrum(DFT_Signal_B, "Magnitude Spectrum of Signal B", "red")

# Cross-correlation and plot

cross_co = Cross_Correlation_Calculation(signalA, signalB)
plot_cross_correlation_discrete(cross_co)
print("Lag value: ")
print(Sample_Lag_Detection(cross_co))


