import numpy as np
import matplotlib.pyplot as plt
from ContinuousSignal import ContinuousSignal
from DiscreteSignal import DiscreteSignal
from LTI_Continuous import LTI_Continuous
from LTI_Discrete import LTI_Discrete
#****************LTI Discrete***********************************



impulse_response = DiscreteSignal(INF=5)
impulse_response.set_value_at_time(0,1)
impulse_response.set_value_at_time(1,1)
impulse_response.set_value_at_time(2,1)
signal=LTI_Discrete(impulse_response)  
input_signal=DiscreteSignal(INF=5)
input_signal.set_value_at_time(0,0.5)
input_signal.set_value_at_time(1,2)
input_signal.plot('input_signal')
linears=signal.linear_combination_of_impulses(input_signal)
signal.plotting_linear_combinations(input_signal)
# signal.plotting_linear_combination(linears)
[outputs,output_sig]=signal.output(input_signal)
signal.plotting_outputs(input_signal)




#*******************************LTI Continuous*******************************
def signal_function(t):
        return np.where(t >= 0, np.exp(-1*t), 0)
def signal_functions(t):

         return np.where((t >= 0) & (t <= 0.5), 1 / 0.5, 0)
def y_t(t):
    return (1-np.exp(-1*t))
def unit_step_functions(t):

         return np.where(t >= 0, 1, 0)
def multi(t):
    return unit_step_functions(t)*y_t(t)
_signal = ContinuousSignal(signal_function)
signal=LTI_Continuous(ContinuousSignal(unit_step_functions))

results=signal.linear_combination_of_impulse(_signal,0.5)
_signal = ContinuousSignal(signal_function)
signal=LTI_Continuous(ContinuousSignal(unit_step_functions))

[signals,values]=signal.linear_combination_of_impulse(_signal,0.5)


#linear combination part


signal.plotting_linear_combinations(signals,values,0.5)
signal.resconstructing_signal(_signal)


#output approx part
[outputs,values,output_sig]=signal.output_approx(_signal,0.5)
signal.plotting_output_approx(outputs,values,0.5)
a1=ContinuousSignal(lambda t:(1-np.exp(-t))*np.heaviside(t,1))
# a1.plot()
print('Show Approximation')
signal=LTI_Continuous(unit_step_functions)
signal.show_approximations(ContinuousSignal(signal_function),ContinuousSignal(multi))

