import numpy as np
import matplotlib.pyplot as plt


class DiscreteSignal:
    def __init__(self,INF) -> None:
        self.INF=INF
        self.values = np.zeros((2*INF)+1)
    def set_value_at_time(self,time,value):
        self.values[time+self.INF]=value
    def shift_signal(self,shift):
        shifted_array = np.zeros((2*self.INF)+1)
        if shift>0 :
            shifted_array[shift:] = self.values[:-shift]
        elif shift<0 :
           
           shifted_array[:shift] = self.values[-shift:]
        else :
            shifted_array=self.values
        signal=DiscreteSignal(self.INF)
        signal.values=shifted_array
        return signal
    def add(self,other):
        len1 = self.INF
        len2 = other.INF
        if len1 > len2:
            add_arr1 = self.values
            add_arr2 = np.pad(other.values, pad_width=len1 - len2, mode='constant', constant_values=0)
        else:
            add_arr1 = np.pad(self.values, pad_width=len2 - len1, mode='constant', constant_values=0)
            add_arr2 = other.values
        add_arr = np.add(add_arr1, add_arr2)
        t = max(self.INF, other.INF)
        signal=DiscreteSignal(t)
        signal.values=add_arr
        return signal
    def multiply(self,other):
        len1 = self.INF
        len2 = other.INF
        if len1 > len2:
            multiply_arr1 = self.values
            multiply_arr2 = np.pad(other.values, pad_width=len1 - len2, mode='constant', constant_values=0)
        else:
            multiply_arr1 = np.pad(self.values, pad_width=len2 - len1, mode='constant', constant_values=0)
            multiply_arr2 = other.values
        add_arr = np.multiply(multiply_arr1, multiply_arr2)
        t = max(self.INF, other.INF)
        signal=DiscreteSignal(t)
        signal.values=add_arr
        return signal
    def multiply_const_factor(self,scaler):
        
        signal=DiscreteSignal(self.INF)
        signal.values=self.values*scaler
        return signal
    def plot(
            self, 
            title='Discrete Signal', 
            y_range=(-1, 3), 
            figsize=(8, 3),
            x_label='n(time index)',
            y_label='x[n]',
            saveTo=None,
            INF=None,
            ax=None
      ):    
            INF=self.INF
            if( ax is not None ) :
                  t = np.linspace(-INF,INF,1000)
                  ax.stem(np.arange(-INF, INF + 1, 1), self.values)
                  ax.set_title(title)
                  #print("Hello")
                  return
            INF = self.INF
            plt.figure(figsize=figsize)
            plt.xticks(np.arange(-INF, INF + 1, 1))

    # Corrected y_range calculation using self.values instead of signal
            y_range = (y_range[0], max(np.max(self.values), y_range[1]) + 1)
    
            plt.ylim(*y_range)
            plt.stem(np.arange(-INF, INF + 1, 1), self.values)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.grid(True)
            if saveTo is not None:
                  plt.savefig(saveTo)
            # plt.show()
            
            
            
            
        
# signal1 = DiscreteSignal(INF=4)
# signal2 = DiscreteSignal(INF=10)
# # signal2.plot()

# # Set some values
# signal1.set_value_at_time(0, 1)
# signal2.set_value_at_time(0, 3)

# # Add the two signals
# result_signal = signal1.multiply_const_factor(3)

# # Print the result values
# print(result_signal.values)
# result_signal.plot()