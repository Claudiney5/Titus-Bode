# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:18:31 2020

@author: Claudiney Martins
"""

import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('compositepars.csv')
base.drop(base[base.fpl_bmasse == 'NaN'].index, inplace=True)
base.drop(base[base.fst_dist == 'NaN'].index, inplace=True)

planet_mass = 2
st_distance = 2000

base.drop(base[base.fpl_bmasse > planet_mass].index, inplace=True)
base.drop(base[base.fst_dist > st_distance].index, inplace=True)

X = base.iloc[:, 45].values
y = base.iloc[:, 18].values

plt.scatter(X, y, s=5)
plt.xlabel('Distância (pc)')
plt.ylabel('Massa da Terra')

