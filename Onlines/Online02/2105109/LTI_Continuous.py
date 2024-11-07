import numpy as np
import math
import os
import matplotlib.pyplot as plt
from ContinuousSignal import ContinuousSignal
img_root_path = '.'
if not os.path.exists(img_root_path):
    os.makedirs(img_root_path)

image_path = './Continuous/'

class LTI_Continuous:
    def __init__(self,impulse_response=None) -> None:
        self.impulse_response=impulse_response
        
        
    def linear_combination_of_impulse(self,input_signal,delta):
        def signal_function(t):
          return np.where((t >= 0) & (t <= delta), 1 / delta, 0)
        sig=ContinuousSignal(signal_function)
        signals = [] 
        values=[]
        upper_limit = math.ceil(3 / delta)
        lower_limit = math.floor(-3 / delta)
        
        for k in range(lower_limit,upper_limit):
            signal=sig.shift(k*delta)
            values.append(input_signal.func(k*delta)*delta)
            signals.append(signal)
        return [signals,values]
    def plotting_linear_combinations(self,signals,values,delta):
          len1=len(signals)
          len2=len1//2
          sum_signal=ContinuousSignal(lambda t:np.where(((t>-100)&(t<100)),0,0))

          subplot_col = 3
          subplot_row = math.ceil((len1+1)/subplot_col)
          plt.figure(figsize=(12,12))

          for k in range(0,len1):
                signal=signals[k].multiply_const_factor(values[k])
                plt.subplot(subplot_row, subplot_col, k+1)
                signal.plot(title=f'δ(t - ({k-len2}*{delta}))x({k-len2}*{delta}){delta}',saveTo=os.path.join(img_root_path, f'fig{k - len2}.png'), ax=plt.gca())

                sum_signal=sum_signal.add(signal)
                          
          plt.subplot(subplot_row, subplot_col, len1+1)
          sum_signal.plot(saveTo=os.path.join(img_root_path, 'fig(input_continous_signal).png'),ax=plt.gca())
          plt.tight_layout()
          image_name = 'fig-6'
          plt.savefig(image_path+image_name)
          #plt.show()
    def plotting_output_approx(self,signals,values,delta):
            len1=len(signals)
            len2=len1//2
            sum_signal=ContinuousSignal(lambda t:np.where(((t>-100)&(t<100)),0,0))
            subplot_col = 3
            subplot_row = math.ceil((len1+1)/subplot_col)
            plt.figure(figsize=(12,12))
            for k in range(0,len1):
                signal=signals[k].multiply_const_factor(values[k])
                plt.subplot(subplot_row, subplot_col, k+1)
                signal.plot(title=f'h(t - ({k-len2}*{delta}))x({k-len2}*{delta}){delta}',saveTo=f'{img_root_path}/fig{k-len2}.png',ax=plt.gca())
                sum_signal=sum_signal.add(signal)
                # print(k)
            plt.subplot(subplot_row, subplot_col, len1+1)    
            sum_signal.plot(saveTo=f'{img_root_path}/fig(comb_output).png',ax=plt.gca())        
            plt.tight_layout()
            
            image_name = 'fig-8'
            plt.savefig(image_path+image_name)
            
            #plt.show()
    def Testing_approx(self,signals,values,delta):
            delta_values = [0.5, 0.1, 0.05, 0.01]
            len1=len(signals)
            len2=len1//2
            sum_signal=ContinuousSignal(lambda t:np.where(((t>-100)&(t<100)),0,0))
            subplot_col = 3
            subplot_row = math.ceil((len1+1)/subplot_col)
            plt.figure(figsize=(12,12))
            for k in range(0,len1):
                signal=signals[k].multiply_const_factor(values[k])
                plt.subplot(subplot_row, subplot_col, k+1)
                signal.plot(title=f'h(t - ({k-len2}*{delta}))x({k-len2}*{delta}){delta}',saveTo=f'{img_root_path}/fig{k-len2}.png',ax=plt.gca())
                sum_signal=sum_signal.add(signal)
                print(k)
            plt.subplot(subplot_row, subplot_col, len1+1)    
            sum_signal.plot(saveTo=f'{img_root_path}/fig(comb_output).png',ax=plt.gca())        
            plt.tight_layout()
            
            image_name = 'fig-8'
            plt.savefig(image_path+image_name)
        
    
    
    # def plotting_linear_combination(self,results):
    #     Reconstructed_signal=ContinuousSignal(lambda t: 0)
    #     for idx, (value, signal) in enumerate(results):
    #         temp = signal.multiply_const_factor(value)
    #         Reconstructed_signal=Reconstructed_signal.add(temp)
    #         temp.plot(f'\u03B4(t-({idx-6}\u0394))\u00D7({idx-6}\u0394)\u0394')
    #     Reconstructed_signal.plot('Reconstructed Plot')
        
    def Reconstruting_Signal(self, input_signal, delta):
        def impulse_approximation(t):
            
            return np.where((t >= 0) & (t < delta), 1 / delta, 0)
        
        
        Reconstructed_signal = ContinuousSignal(lambda t: 0)
        
        
        impulse = ContinuousSignal(impulse_approximation)
        num_points = 1000
        t_values = np.linspace(-3, 3, num_points)
        
        
        for k in range(-6, 7):
            
            shifted_impulse = impulse.shift(k * delta)
            scaled_impulse = shifted_impulse.multiply_const_factor(input_signal.func(k * delta) * delta)
            Reconstructed_signal = Reconstructed_signal.add(scaled_impulse)
        
        
        plt.figure(figsize=(8, 4))
        plt.plot(t_values, input_signal.func(t_values), label='Original Signal', color='blue')
        plt.plot(t_values, Reconstructed_signal.func(t_values), label=f'Reconstructed Signal (Δ={delta})', color='orange')
        plt.title(f'Reconstructed Signal with Δ = {delta}')
        plt.xlabel('t (Time)')
        plt.ylabel('x(t)')
        plt.legend()
        plt.grid(True)
        # plt.show()
    def resconstructing_signal(self, input_signal):
        All_deltas = [0.5, 0.1, 0.05, 0.01]  
        subplot_col = 2
        subplot_row = 2
        plt.figure(figsize=(12,12))
        i=1
        for delta in All_deltas:
            a = ContinuousSignal(lambda t: np.where(np.logical_and(t >= 0, t < delta), 1 / delta, 0))
            sum_signal = ContinuousSignal(lambda t: np.where((t > -100) & (t < 100), 0, 0))
            upper_limit = math.ceil(3 / delta)
            lower_limit = math.floor(-3 / delta)
            for k in range(lower_limit, upper_limit):
                signal1 = a.shift(k * delta)
                coeff = input_signal.func(k * delta) * delta
                int_sig = signal1.multiply_const_factor(coeff)
                sum_signal = sum_signal.add(int_sig)
            ax=plt.subplot(subplot_row, subplot_col, i)
            sum_signal.plot(title=f'delta={delta}', saveTo=os.path.join(img_root_path, f'fig{delta}.png'),ax=plt.gca())
            input_signal.plot(saveTo=os.path.join(img_root_path, f'fig{delta}.png'),ax=plt.gca())
            ax.set_title(f'\u0394={delta}')
            i=i+1
        plt.tight_layout()
        image_name = 'fig-7'
        plt.savefig(image_path+image_name)
        #plt.show()
    def output_show(self,input_signal,y_t_sig,delta):
        def signal_function(t):
          return np.where((t >= 0) & (t <= delta), 1 / delta, 0)
        Reconstructed_signal=ContinuousSignal(lambda t: 0)
        sig=ContinuousSignal(signal_function)
        intemp=ContinuousSignal(signal_function)
        upper=math.ceil(3/delta)
        lower=math.ceil(-3/delta)
        for k in range(-6,7):
            
            signal=self.impulse_response.shift((k*delta))
            ans_sig=signal.multiply_const_factor((input_signal.func(k*delta)*delta))
            if k==-6 :
                intemp=ans_sig
            else :
                intemp=intemp.add(ans_sig)
            Reconstructed_signal=Reconstructed_signal.add(ans_sig)
        t_values = np.linspace(-6 , 6 , 1000)  
        img_root_path='./Continuous'
        title=f'\u0394={delta}'
        title=title.replace('.', '_')
        saveTo=f'{img_root_path}/{title}'
        plt.figure(figsize=(10, 5))
        plt.plot(t_values, intemp.func(t_values), label='y_approx(t)', color='blue')
        plt.plot(t_values, y_t_sig.func(t_values), label='y(t)=(1-e^(-t)u(t))', color='orange')
        plt.title(f'Δ={delta}')
        # img_root_path='./Continuous'
        # saveTo=f'{img_root_path}/{f'Δ={delta}'}'
        plt.xlabel('Time (t)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid()
        plt.savefig(saveTo)
        # plt.show()
    def output_approx(self,input_signal,delta):
        def signal_function(t):
          return np.where((t >= 0) & (t <= delta), 1 / delta, 0)
        # unit_impulse=ContinuousSignal(signal_function)
       
        # sig=ContinuousSignal(signal_function)
        out_sig=ContinuousSignal(signal_function)
        output_signals=[]
        values=[]
        
        # Reconstructed_signal.plot()
        upper=math.ceil(3/delta)
        lower=math.floor(-3/delta)
        
        for k in range(lower,upper):
            
            sig=self.impulse_response.shift((k*delta))
            ans_sig=sig.multiply_const_factor((input_signal.func(k*delta)*delta))
            if k==lower :
                out_sig=ans_sig
            else :
                out_sig=out_sig.add(ans_sig)
            output_signals.append(sig)
            values.append(input_signal.func(k*delta)*delta)
            # Reconstructed_signal=Reconstructed_signal.add(ans_sig)
            # intemp.plot((-6,6),'Reconstructed Signal')
            # signal.plot((-6,6),f'\u03B4(t-({k}\u0394))\u00D7({k}\u0394)\u0394')
        # intemp.plot('Output=Sum')
        return [output_signals,values,out_sig]
    # def plotting_output_approx(self,outputs,output_sig):
    #     for idx, (value, signal) in enumerate(outputs):
    #         temp = signal.multiply_const_factor(value)
    #         # Reconstructed_signal=Reconstructed_signal.add(temp)
    #         temp.plot(f'h(t-({idx-6}\u0394))*x({idx-6}\u0394)\u0394')
    #     output_sig.plot('Output=Sum')
    def show_approximations(self, input_signal,input_signal2):
        delta_values = [0.5, 0.1, 0.05, 0.01]  
        subplot_col = 2
        subplot_row = 2
        plt.figure(figsize=(12,12))
        i=1
        for delta in delta_values:
            sum_signal = ContinuousSignal(lambda t: np.zeros_like(t))
            impulse_response_signal = ContinuousSignal(self.impulse_response)
            # print('plotting impulse response')
            # impulse_response_signal.plot()

            upper_limit = math.ceil(3 / delta)
            lower_limit = math.floor(-3 / delta)
            
            for k in range(lower_limit, upper_limit):
                signal1 = impulse_response_signal.shift(k * delta)
                # print('signal printing after shift')
                # print(type(signal1))
                # signal1.plot()
                coeff = input_signal.func(k * delta) * delta
                int_sig = signal1.multiply_const_factor(coeff)
                # print('signal printing after multiplying constant')
                # int_sig.plot()
                sum_signal = sum_signal.add(signal1.multiply_const_factor(coeff))
                # sum_signal.plot()
                # print('printing sum signal')
                
            
            ax=plt.subplot(subplot_row, subplot_col, i)
            print(delta)
            sum_signal.plot(title=f'delta={delta}', saveTo=os.path.join(img_root_path, f'fig{delta}.png'),ax=plt.gca())
            
            input_signal2.plot(t_range=(-3,3),saveTo=f'{img_root_path}/fig{delta}.png',ax=plt.gca())
            ax.set_title(f'Signal Approximation for delta={delta}')
            i=i+1
        
        plt.tight_layout()
        image_name = 'fig-9'
        plt.savefig(image_path+image_name)
        # plt.show() 
    def output_approx_varying(self,input_signal,delta):
        all_deltas=[0.5,0.1,0.05,0.01]
        # for i in range(len(all_deltas))
        def signal_function(t):
          return np.where((t >= 0) & (t <= delta), 1 / delta, 0)
        # unit_impulse=ContinuousSignal(signal_function)
        Reconstructed_signal=ContinuousSignal(lambda t: 0)
        sig=ContinuousSignal(signal_function)
        intemp=ContinuousSignal(signal_function)
        
        output_signals=[]
        
        # Reconstructed_signal.plot()
        values=[]
        for k in range(-6,7):
            values.append(k*delta)
            
        
        for k in range(-6,7):
            
            signal=self.impulse_response.shift(values[k+6])
            ans_sig=signal.multiply_const_factor((input_signal.func(values[k+6])*delta))
            if k==-6 :
                intemp=ans_sig
            else :
                intemp=intemp.add(ans_sig)
            output_signals.append(ans_sig)
            # Reconstructed_signal=Reconstructed_signal.add(ans_sig)
            # intemp.plot((-6,6),'Reconstructed Signal')
            # signal.plot((-6,6),f'\u03B4(t-({k}\u0394))\u00D7({k}\u0394)\u0394')
        intemp.plot('Output=Sum')
def signal_function(t):
        return np.where(t >= 0, np.exp(-1*t), 0)
# def signal_functions(t):

#          return np.where((t >= 0) & (t <= 0.5), 1 / 0.5, 0)
def unit_step_functions(t):

         return np.where(t >= 0, 1, 0)
# unit_impulse=ContinuousSignal(signal_functions)
# unit_impulse.plot()
    # Create a ContinuousSignal instance
# _signal = ContinuousSignal(signal_function)
# signal=LTI_Continuous(ContinuousSignal(unit_step_functions))

# results=signal.linear_combination_of_impulse(_signal,0.5)
# #linear combination part
# # signal.plotting_linear_combination(results)




#output approx part
# [outputs,output_sig]=signal.output_approx(_signal,0.5)
# signal.plotting_output_approx(outputs,output_sig)



    # temp.plot(f'\u03B4(t-({idx-6}\u0394))\u00D7({idx-6}\u0394)\u0394')
# Reconstructed_signal.plot('Reconstructed Plot')
# Plotting for different delta
# signal=LTI_Continuous(ContinuousSignal(unit_step_functions))
# signal.Reconstruting_Signal(_signal,0.5)
# signal.Reconstruting_Signal(_signal,0.1)
# signal.Reconstruting_Signal(_signal,0.05)
# signal.Reconstruting_Signal(_signal,0.01)

# for idx, sig in enumerate(signals):
#     sig.plot(f'\u03B4(t-({idx-6}\u0394))\u00D7({idx-6}\u0394)\u0394')
# Reconstruct.plot('Reconstructed Signal')
# signal.Reconstruting_Signal(_signal,0.1)
# signal.Reconstruting_Signal(_signal,0.05)
# signal.Reconstruting_Signal(_signal,0.01)
# [output_signal,sum_signal]=signal.output_approx(ContinuousSignal(signal_function),0.5)
# for idx, sig in enumerate(output_signal):
#     sig.plot(f'h(t-({idx-6}\u0394))*x({idx-6}\u0394)\u0394')


            
        