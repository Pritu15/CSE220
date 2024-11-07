from DiscreteSignal import DiscreteSignal
import math
import matplotlib.pyplot as plt
img_root_path='.'
image_path = './Discrete/'
class LTI_Discrete:
    def __init__(self,impulse_response=None) -> None:
        if impulse_response is None:
            impulse_response = DiscreteSignal(INF=5)
            impulse_response.set_value_at_time(0,1)
            
           
        self.impulse_response=impulse_response
    def linear_combination_of_impulses(self,input_signal:DiscreteSignal):
        len1=input_signal.INF
        unit_impulse=DiscreteSignal(len1)
        unit_impulse.set_value_at_time(0,1) 
        sum_signal=DiscreteSignal(len1)
        linears=[]
        for i in range(-len1,len1+1):
            signal=DiscreteSignal(len1)
            # title=title = f'\u03B4[n-({i})x[{i}]]'
            signal=signal.add(unit_impulse)
            signal=signal.shift_signal(i)
            linears.append([input_signal.values[i+len1],signal])
        return linears
    def plotting_linear_combination(self,linears):
        sum=DiscreteSignal(linears[0][1].INF)
        for idx, (value, signal) in enumerate(linears):
            temp = signal.multiply_const_factor(value)
            sum=sum.add(temp)
            # Reconstructed_signal=Reconstructed_signal.add(temp)
            temp.plot(f'\u03B4[n-({idx-signal.INF})x[{idx-signal.INF}]]')
        sum.plot('Sum')
    def plotting_linear_combinations(self,input_signal):
           ran = input_signal.INF
        
           final_output = DiscreteSignal(ran)
           subplot_col = 3
           subplot_row = math.ceil((2*ran+1)/subplot_col)
           plt.figure(figsize=(12,12))
        #    img_root_path='./Discrete'
           delta = DiscreteSignal(ran)  
           delta.set_value_at_time(0, 1)  
           fig_count=1
           j=1
           for i in range(-ran, ran + 1):
            
             shifted_signal = delta.shift_signal(i)
             scaled_shifted_signal = shifted_signal.multiply_const_factor(input_signal.values[i + ran])

            
             final_output = final_output.add(scaled_shifted_signal)
             plt.subplot(subplot_row, subplot_col, j)
             scaled_shifted_signal.plot(title=f'δ(n-({i}))x({i})',saveTo=f'{img_root_path}/δ(n-({i}))x({i}).png',INF=input_signal.INF,ax=plt.gca())
             
             fig_count=fig_count+1
             j=j+1
           plt.subplot(subplot_row, subplot_col, 2*ran + 2)  
           final_output.plot(saveTo=f'{img_root_path}/Sum.png',ax=plt.gca())
           plt.tight_layout()
           image_name = 'fig-2'
           plt.savefig(image_path+image_name)
           #plt.show()
    def output(self,input_signal:DiscreteSignal):
        len1=input_signal.INF
        sum_signal=DiscreteSignal(len1)
        outputs=[]
        for i in range(-len1,len1+1):
            signal=DiscreteSignal(len1)
            # title=title = f'h[n-({i})x[{i}]]'
            signal=signal.add(self.impulse_response)
            signal=signal.shift_signal(i)
            outputs.append([input_signal.values[i+len1],signal])
            signal=signal.multiply_const_factor(input_signal.values[i+len1])
            signal.plot()
            sum_signal=sum_signal.add(signal)
            # sum_signal.plot(title=f'h[n-({idx-sig.INF})x[{idx-sig.INF}]]')
            # signal.plot(title)
        title='Sum'
        # sum_signal.plot(title)
        return [outputs,sum_signal]
    def plotting_output(self,outputs,output_sig):
        for idx, (value, sig) in enumerate(outputs):
            temp = sig.multiply_const_factor(value)
            # sum=sum.add(temp)
            # Reconstructed_signal=Reconstructed_signal.add(temp)
            temp.plot(f'h[n-({idx-sig.INF})x[{idx-sig.INF}]]')
        output_sig.plot('Output')
    def plotting_outputs(self,input_signal):
           ran = input_signal.INF
        
           final_output = DiscreteSignal(ran)
           subplot_col = 3
           subplot_row = math.ceil((2*ran+1)/subplot_col)
           plt.figure(figsize=(12,12))
        #    img_root_path='./Discrete'
           delta = DiscreteSignal(ran)  
           delta.set_value_at_time(0, 1)  
           fig_count=1
           j=1
           for i in range(-ran, ran + 1):
            
             shifted_signal = self.impulse_response.shift_signal(i)
             scaled_shifted_signal = shifted_signal.multiply_const_factor(input_signal.values[i + ran])
             scaled_shifted_signal.plot(title=f'h(n-({i}))x({i})')

            
             final_output = final_output.add(scaled_shifted_signal)
             plt.subplot(subplot_row, subplot_col, j)
             scaled_shifted_signal.plot(title=f'h(n-({i}))x({i})',saveTo=f'{img_root_path}/δ(n-({i}))x({i}).png',INF=input_signal.INF,ax=plt.gca())
             
             fig_count=fig_count+1
             j=j+1
           plt.subplot(subplot_row, subplot_col, min(j, subplot_row * subplot_col))  
           final_output.plot(saveTo=f'{img_root_path}/Output=Sum.png',ax=plt.gca())
           plt.tight_layout()
           image_name = 'fig-3'
           plt.savefig(image_path+image_name)
        #    plt.show()
        
    
# impulse_response = DiscreteSignal(INF=5)
# impulse_response.set_value_at_time(0,1)
# impulse_response.set_value_at_time(1,1)
# impulse_response.set_value_at_time(2,1)
# signal=LTI_Discrete(impulse_response)  
# input_signal=DiscreteSignal(INF=5)
# input_signal.set_value_at_time(0,0.5)
# input_signal.set_value_at_time(1,2)
# input_signal.plot('input_signal')
# linears=signal.linear_combination_of_impulses(input_signal)
# signal.plotting_linear_combination(linears)
# [outputs,output_sig]=signal.output(input_signal)
# signal.plotting_output(outputs,output_sig)
        # sum.plot('Sum')

# signal.output(input_signal)
            
        