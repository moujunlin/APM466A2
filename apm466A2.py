# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 06:47:31 2021

@author: Admin
"""
import matplotlib.pyplot as plt

gas_prices=[]
for i in range(53):
    gas_prices.append([])
    for j in range(53-i):
        gas_prices[i].append(pow(1.1,i-j)*50)


one_up= [[0 for i in range(53)] for j in range(53)]
one_up_opts={'up':[],'down':[]}
for i in range(53):
    one_up[i][52-i] = max(0,gas_prices[i][52-i]-50)
for i in range(52):
    for j in range(52-i):
        exercise_value = max(gas_prices[j][51-i-j]-50,0)
        expectation_for_future = 0.5*one_up[j+1][51-i-j]+0.5*one_up[j][51-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            one_up_opts['up'].append(j)
            one_up_opts['down'].append(51-i-j)
        one_up[j][51-i-j] = max(exercise_value,expectation_for_future)
plt.plot(one_up_opts['up'],one_up_opts['down'])

two_up= [[0 for i in range(53)] for j in range(53)]
two_up_opts = {'up':[],'down':[]}
for i in range(53):
    two_up[i][52-i] = one_up[i][52-i] 
for i in range(52):
    for j in range(52-i):
        exercise_value = max(gas_prices[j][51-i-j]-50,0)+one_up[j][51-i-j]
        expectation_for_future = 0.5*two_up[j+1][51-i-j]+0.5*two_up[j][51-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            two_up_opts['up'].append(j)
            two_up_opts['down'].append(51-i-j)
        two_up[j][51-i-j] = max(exercise_value,expectation_for_future)
plt.plot(two_up_opts['up'],two_up_opts['down'],label='two_up')

three_up= [[0 for i in range(53)] for j in range(53)]
three_up_opts = {'up':[],'down':[]}
for i in range(53):
    three_up[i][52-i] = one_up[i][52-i] 
for i in range(52):
    three_up[i][51-i] = two_up[i][51-i] 
for i in range(51):
    for j in range(51-i):
        exercise_value = max(gas_prices[j][50-i-j]-50,0)+two_up[j][50-i-j]
        expectation_for_future = 0.5*three_up[j+1][50-i-j]+0.5*three_up[j][50-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            three_up_opts['up'].append(j)
            three_up_opts['down'].append(50-i-j)
        three_up[j][50-i-j] = max(exercise_value,expectation_for_future)
plt.plot(three_up_opts['up'],three_up_opts['down'],label='three_up')

four_up= [[0 for i in range(53)] for j in range(53)]
four_up_opts = {'up':[],'down':[]}
for i in range(53):
    four_up[i][52-i] = one_up[i][52-i] 
for i in range(52):
    four_up[i][51-i] = two_up[i][51-i] 
for i in range(51):
    four_up[i][50-i] = three_up[i][50-i] 
for i in range(50):
    for j in range(50-i):
        exercise_value = max(gas_prices[j][49-i-j]-50,0)+three_up[j][49-i-j]
        expectation_for_future = 0.5*four_up[j+1][49-i-j]+0.5*four_up[j][49-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            four_up_opts['up'].append(j)
            four_up_opts['down'].append(49-i-j)
        four_up[j][49-i-j] = max(exercise_value,expectation_for_future)
plt.plot(four_up_opts['up'],four_up_opts['down'],label='four_up')


one_down= [[0 for i in range(53)] for j in range(53)]
one_down_opts={'up':[],'down':[]}
for i in range(53):
    one_down[i][52-i] = max(0,50-gas_prices[i][52-i])
for i in range(52):
    for j in range(52-i):
        exercise_value = max(50-gas_prices[j][51-i-j],0)
        expectation_for_future = 0.5*one_down[j+1][51-i-j]+0.5*one_down[j][51-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            one_down_opts['up'].append(j)
            one_down_opts['down'].append(51-i-j)
        one_down[j][51-i-j] = max(exercise_value,expectation_for_future) 
plt.plot(one_down_opts['up'],one_down_opts['down'],label='one_down')


two_down= [[0 for i in range(53)] for j in range(53)]
two_down_opts={'up':[],'down':[]}
for i in range(53):
    two_down[i][52-i] = one_down[i][52-i] 
for i in range(52):
    for j in range(52-i):
        exercise_value = max(50-gas_prices[j][51-i-j],0)+one_down[j][51-i-j]
        expectation_for_future = 0.5*two_down[j+1][51-i-j]+0.5*two_down[j][51-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            two_down_opts['up'].append(j)
            two_down_opts['down'].append(51-i-j)
        two_down[j][51-i-j] = max(exercise_value,expectation_for_future)
plt.plot(two_down_opts['up'],two_down_opts['down'],label='two_down')

        
three_down= [[0 for i in range(53)] for j in range(53)]
three_down_opts={'up':[],'down':[]}
for i in range(53):
    three_up[i][52-i] = one_down[i][52-i] 
for i in range(52):
    three_down[i][51-i] = two_down[i][51-i] 
for i in range(51):
    for j in range(51-i):
        exercise_value = max(0,50-gas_prices[j][50-i-j])+two_down[j][50-i-j]
        expectation_for_future = 0.5*three_down[j+1][50-i-j]+0.5*three_down[j][50-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
            three_down_opts['up'].append(j)
            three_down_opts['down'].append(50-i-j)
        three_down[j][50-i-j] = max(exercise_value,expectation_for_future)
plt.plot(three_down_opts['up'],three_down_opts['down'],label='three_down')

four_down_opts={'up':[],'down':[]}
four_down= [[0 for i in range(53)] for j in range(53)]
for i in range(53):
    four_down[i][52-i] = one_down[i][52-i] 
for i in range(52):
    four_down[i][51-i] = two_down[i][51-i] 
for i in range(51):
    four_down[i][50-i] = three_down[i][50-i] 
for i in range(50):
    for j in range(50-i):
        exercise_value = max(0,50-gas_prices[j][49-i-j])+three_down[j][49-i-j]
        expectation_for_future = 0.5*four_down[j+1][49-i-j]+0.5*four_down[j][49-i-j+1]
        if round(exercise_value,2) > round(expectation_for_future,2):
             four_down_opts['up'].append(j)
             four_down_opts['down'].append(49-i-j)
        four_down[j][49-i-j] = max(exercise_value,expectation_for_future)
plt.plot(four_down_opts['up'],four_down_opts['down'],label='four_down')
plt.legend()
print(four_up[0][0],four_down[0][0])
