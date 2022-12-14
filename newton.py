# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:05:03 2022

@author: bhava
"""


x=[0,1,2,5.5,11,13,16,18]
y=[0.5,3.134,5.3,9.9,10.2,9.535,7.2,6.2]

def divided_diff_table(x, y):
  table = []
  n = len(x)
  temp = []

  for i in range(1, n):
    temp.append((y[i] - y[i-1])/(x[i] - x[i-1]))

  diff = 2
  table.append(temp)

  while len(table[-1]) > 1:
    temp = []
    ind = 0
    latest = table[-1]

    for i in range(1, len(latest)):
      temp.append((latest[i] - latest[i-1])/(x[ind + diff] - x[ind]))
      ind += 1

    table.append(temp)
    diff += 1

  return table



def newton_divided_diff(x, y, new_x):
  diff = divided_diff_table(x, y)
  order = len(diff)
  pred_val = y[0]
  d = 1

  for i in range(order):
    prod = 1
    
    for j in range(d):
      prod *= (new_x - x[j])

    pred_val += (prod * diff[i][0])

  return pred_val



pred_x = [0.5,3]
pred_y = []

for i in pred_x:
  pred_y.append(newton_divided_diff(x, y, i))

print(pred_y)

