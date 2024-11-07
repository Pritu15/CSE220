import numpy as np
import matplotlib.pyplot as plt
from ContinuousSignal import ContinuousSignal
from DiscreteSignal import DiscreteSignal
from LTI_Continuous import LTI_Continuous
from LTI_Discrete import LTI_Discrete

d1=int(input('Degree of the first Polynomial:'))
# print(d1)
coeffs1 = list(map(int, input("Coefficients: ").split()))
# print(coeffs1)
d2=int(input('Degree of the first Polynomial:'))



# print(d2)
coeffs2 = list(map(int, input("Coefficients: ").split()))


# print(coeffs2)
ans_poly=d1+d2
print(f'Degree of the Polynomial:{ans_poly}')
INF=(len(coeffs1)+(len(coeffs2)-1)*2)//2
B=DiscreteSignal(d1+d2)
for i in range(len(coeffs2)):
    B.set_value_at_time(i,coeffs2[len(coeffs2)-i-1])

A=DiscreteSignal(d1+d2)
for i in range(len(coeffs1)):
    A.set_value_at_time(i,coeffs1[len(coeffs1)-i-1])
A.plot()
B.plot()
# B.shift_signal(0).plot()
ans=LTI_Discrete(B)
[outputs,sum_signal]=ans.output(A)
for i in range(len(sum_signal.values)):
    print(sum_signal.values[i])
ans.plotting_outputs(A)

    
#3
#2 0 -3 1
#2
#3 -2 1
