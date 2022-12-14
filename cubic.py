# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:18:55 2022

@author: bhava
"""

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as pt

x=[0,8,16,24,32,40]
y=[14.621,11.843,9.870,8.418,7.305,6.413]

f=CubicSpline(x, y)
y0=f(x)

x_new=[4,36]
y_new=f(x_new)

print(y_new)

pt.title("CubicSpline")
pt.scatter(x,y)
pt.plot(x,y0)
pt.show()
