import numpy as np
import matplotlib.pyplot as plt
import re

class ContinuousSignal:
    def __init__(self, func=None) -> None:
        if func is None:
            func = lambda t: np.zeros_like(t)
        self.func = func
    
    def evaluate(self, t):
        return self.func(t)
    
    def adil (self,func):
        self.func = func
      
        
    
    def shift(self, shiftamount):
        def shifted_func(t):
            return self.func(t - shiftamount)
        return ContinuousSignal(lambda t: self.func(t - shiftamount))
    
    def add(self, other):
        def add_func(t):
            return self.func(t) + other.func(t)
        return ContinuousSignal(add_func)
    
    def multiply(self, other):
        def multiply_func(t):
            return self.func(t) * other.func(t)
        return ContinuousSignal(multiply_func)
    
    def multiply_const_factor(self, scaler):
        def multiply_const_func(t):
            return scaler * self.func(t)
        return ContinuousSignal(multiply_const_func)
    
    def plot(self, t_range=(-5,5), title="Continuous Signal",saveTo=None, ax=None):
            
            if( ax is not None ) :
                  t = np.linspace(*t_range, 1000)
                  ax.plot(t,self.func(t))
                  ax.set_title(title)
                  #print("Hello")
                  return

            t = np.linspace(*t_range, 1000)
            plt.plot(t, self.evaluate(t))
            plt.title(title)
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.grid(True)
            #plt.show()
            if saveTo is not None:
                plt.savefig(saveTo)
            plt.show()
        
        
        # Show the plot
        # plt.show()

# Example usage:
# Define a unit impulse function
# def signal_functions(t):
#     return np.where((t >= 0) & (t <= 0.5), 1 / 0.5, 0)

# unit_impulse = ContinuousSignal()
# signal = unit_impulse  # Set signal directly to unit_impulse
# signal.plot()
