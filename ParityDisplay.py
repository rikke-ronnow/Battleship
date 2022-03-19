#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:49:48 2022

@author: shimin
"""

from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
cmap = ListedColormap(['w','g'])


l = ([0,1] * 5 + [1, 0] * 5) * 5
board = np.array(l).reshape(10,10)
print(board)
plt.matshow(board,cmap=cmap,vmin=0,vmax=1)
