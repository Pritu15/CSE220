import numpy as np
import matplotlib.pyplot as plt
import time
n=50
samples = np.arange(n) 
sampling_rate=100
wave_velocity=8000



#use this function to generate signal_A and signal_B with a random shift
def generate_signals(n_power=4, frequency=5, sampling_rate=100):
    """
    Generate two random discrete signals of length n=2^k with added noise and a random shift.
    
    Parameters:
    n_power (int): The power k such that n=2^k determines the length of the signals.
    frequency (int): The frequency of the original sinusoidal signal in Hz.
    sampling_rate (int): The sampling rate in Hz.
    
    Returns:
    tuple: A tuple containing signal_A and signal_B with a random shift applied.
    """
    n = 2 ** n_power  # Calculate the signal length
    samples = np.arange(n)  # Discrete sample indices
    dt = 1 / sampling_rate  # Sampling interval in seconds
    time = samples * dt  # Time points corresponding to each sample

    # Define noise frequencies and amplitudes
    noise_freqs = [15, 30, 45]  # Noise frequencies for signal A
    amplitudes = [0.5, 0.3, 0.1]  # Noise amplitudes for signal A
    noise_freqs2 = [10, 20, 40]  # Noise frequencies for signal B
    amplitudes2 = [0.3, 0.2, 0.1]  # Noise amplitudes for signal B

    # Generate the original clean signal
    original_signal = np.sin(2 * np.pi * frequency * time)

    # Add noise to create signal A
    noise_for_signal_A = sum(
        amplitude * np.sin(2 * np.pi * noise_freq * time)
        for noise_freq, amplitude in zip(noise_freqs, amplitudes)
    )
    signal_A = original_signal + noise_for_signal_A

    # Add additional noise to create signal B
    noise_for_signal_B = sum(
        amplitude * np.sin(2 * np.pi * noise_freq * time)
        for noise_freq, amplitude in zip(noise_freqs2, amplitudes2)
    )
    noisy_signal_B = signal_A + noise_for_signal_B

    # Apply a random shift to signal B
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
    result=result/length
    return result
def FFT(signal):
    
    n = len(signal)
    if n <= 1:
        return signal
    
    
    even = FFT(signal[0::2]) 
    odd = FFT(signal[1::2]) 

    
    combined = np.zeros(n, dtype=complex)
    for k in range(n // 2):
        factor = np.exp(-2j * np.pi * k / n) 
        combined[k] = even[k] + factor * odd[k]  
        combined[k + n // 2] = even[k] - factor * odd[k]  

    return combined
def IFFT(signal):
    
    n = len(signal)
    if n <= 1:
        return signal
    
    
    even = FFT(signal[0::2]) 
    odd = FFT(signal[1::2]) 

    
    combined = np.zeros(n, dtype=complex)
    for k in range(n // 2):
        factor = np.exp(2j * np.pi * k / n) 
        combined[k] = even[k] + factor * odd[k]  
        combined[k + n // 2] = even[k] - factor * odd[k]  

    return combined
        
def Cross_Correlation_Calculation(signalA,signalB):
    resultA=DFT(signalA)
    resultB=DFT(signalB)
    conjugateB=np.conjugate(resultB)
    cross_co_omega=resultA*conjugateB
    result=IDFT(cross_co_omega)
    return cross_co_omega
def Sample_Lag_Detection(signal):
    max_index=np.argmax(signal)
    return max_index
def  Distance_Estimation(lag):
    answer=lag*wave_velocity/sampling_rate
    return answer
def plot_original_signal(signal, title, color):
    """
    Plot the original signal in the time domain.

    Parameters:
    signal (array-like): The signal to be plotted.
    title (str): The title of the plot.
    color (str): The color for the stem plot.

    Returns:
    None
    """
    plt.figure(figsize=(5, 6))
    plt.stem(samples, signal, linefmt=color, markerfmt=color, basefmt=" ")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.show()

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

def measure_runtime(func, signal, runs=10):
    """
    Measure the average runtime of a function over multiple runs.
    
    Parameters:
    func (function): The function to measure.
    signal (array-like): The input signal for the function.
    runs (int): Number of runs to calculate the average runtime.

    Returns:
    float: The average runtime in seconds.
    """
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        func(signal)
        total_time += time.time() - start_time
    return total_time / runs

def runtime_comparison():
    """
    Compare runtimes of DFT, FFT, IDFT, and IFFT for increasing input sizes.

    Returns:
    None
    """
    powers = range(1, 11)  # k ∈ {2, 3, ..., 10} -> n = 2, 4, ..., 1024
    dft_times, fft_times = [], []
    idft_times, ifft_times = [], []

    for power in powers:
        # Generate a signal of length n = 2^power
        signal_length = 2 ** power
        signal, _ = generate_signals(n_power=power)

        # Measure runtimes
        dft_times.append(measure_runtime(DFT, signal))
        fft_times.append(measure_runtime(FFT, signal))
        idft_times.append(measure_runtime(IDFT, signal))
        ifft_times.append(measure_runtime(IFFT, signal))

    signal_lengths = [2**p for p in powers]

    # Plot for DFT and FFT
    plt.figure(figsize=(10, 6))
    plt.plot(signal_lengths, dft_times, label="DFT", marker="o", color="blue")
    plt.plot(signal_lengths, fft_times, label="FFT", marker="o", color="green")
    plt.xlabel("Signal Length (n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Runtime Comparison: DFT vs FFT")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot for IDFT and IFFT
    plt.figure(figsize=(10, 6))
    plt.plot(signal_lengths, idft_times, label="IDFT", marker="o", color="red")
    plt.plot(signal_lengths, ifft_times, label="IFFT", marker="o", color="orange")
    plt.xlabel("Signal Length (n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Runtime Comparison: IDFT vs IFFT")
    plt.legend()
    plt.grid(True)
    plt.show()

runtime_comparison()


