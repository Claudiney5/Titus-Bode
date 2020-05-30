# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:14:22 2020

@author: Master
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

base = pd.read_csv('systems.csv')

X = base.iloc[:,1].values
y = base.iloc[:,2].values

plt.scatter(X, y, s=5)
plt.xlabel('Nº de planetas')
plt.ylabel('Dist. em Parsecs')
