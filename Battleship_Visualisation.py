#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:54:05 2022

@author: rikke.ronnow
"""

import matplotlib.pyplot as plt
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 10,10
image = np.zeros(nrows*ncols)

# Set every other cell to a random number (this would be your data)

image[0]=1
image[1]=0.1
image[99]=1
image[10]=0.1

#image[::] = np.random.random(nrows*ncols)

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

row_labels = range(nrows)
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','F']
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()