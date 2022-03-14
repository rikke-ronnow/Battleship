#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:26:50 2022

@author: rikke.ronnow
"""

import numpy as np
import random
import os
#import Battleships
import matplotlib.pyplot as plt
'''
b=play_game(100,less_random_guess())

#%%
turns=100

def play_game(times,guess_strategy):
    a=[]
    for time in range(times):
        for turn in range(100):
          print("Turn:", turn + 1, "of", turns)
          print("Ships left:", len(ship_array))
          print()
          
          #x = int(input("Guess an x coordinate: "))
          #y = int(input("Guess a y coordinate: "))
          
        
          guess_coord=guess_strategy
          #guess_coord=less_random_guess()
          
          guess_ship(guess_coord)
        
          print(guess_board)
          #print(ship_board)
          
          if np.sum(ship_board)==0:
              break
        
        # End Game
        if np.sum(ship_board)!=0:
          print("You lose!")
        else:
          print("All the ships have been sunk. You win!")
          a.append(turns)
      
    return np.array(a)'''

#%%

turns1=np.loadtxt('random_turns1.txt')

plt.hist(turns1,bins=20)

turns2=np.loadtxt('random_turns2.txt')

plt.hist(turns2,bins=20)

turns3=np.loadtxt('random_turns3.txt')

plt.hist(turns3,bins=20)

#%%

turns=np.concatenate((turns1,turns2))
turns=np.concatenate((turns,turns3))

long_turns=np.loadtxt('turns.txt')
turns=np.concatenate((turns,long_turns))

plt.hist(turns,bins=20)

plt.ylabel('Frequency')
plt.xlabel('Turns')

plt.show()

