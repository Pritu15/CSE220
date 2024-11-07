import numpy as np
import matplotlib.pyplot as plt
from ContinuousSignal import ContinuousSignal
from DiscreteSignal import DiscreteSignal
from LTI_Continuous import LTI_Continuous
from LTI_Discrete import LTI_Discrete

import numpy as np

# Stock Market Prices as a Python List
price_list = list(map(int, input("Stock Prices: ").split()))
n = int(input("Window size: "))
stock_prices=DiscreteSignal(len(price_list))
for i in range(len(price_list)-1):
    stock_prices.set_value_at_time(i,price_list[i])
stock_prices.plot()
Unweighted_Window_signal=DiscreteSignal(len(price_list)-1)
for i in range(n):
    Unweighted_Window_signal.set_value_at_time(i,1/n)
Unweighted_Window_signal.plot()
A=LTI_Discrete(Unweighted_Window_signal)
[outputs,sum_signal]=A.output(stock_prices)
sum_signal.plot()
weighted_Window_signal=DiscreteSignal(len(price_list)-1)
s=(n*(n+1))//2
for i in range(n):
    weighted_Window_signal.set_value_at_time(i,(i+1)/s)
weighted_Window_signal.plot()
# price_list = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 4

# Please determine uma and wma.

# Unweighted Moving Averages as a Python list
uma = []
uma=sum_signal.values


# Weighted Moving Averages as a Python list
A=LTI_Discrete(weighted_Window_signal)
[outputs,sum_signal]=A.output(stock_prices)
wma =sum_signal.values

# Print the two moving averages
print("Unweighted Moving Averages: " + ", ".join(f"{num:.2f}" for num in uma))
print("Weighted Moving Averages:   " + ", ".join(f"{num:.2f}" for num in wma))