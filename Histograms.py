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

#RdYlGn

turns1=np.loadtxt('/Users/rikke.ronnow/Documents/Year 2/I-Explore/Battleship/random_turns1.txt')

turns2=np.loadtxt('/Users/rikke.ronnow/Documents/Year 2/I-Explore/Battleship/random_turns3.txt')


parity=np.loadtxt('/Users/rikke.ronnow/Desktop/parity.txt')

nonparity=np.loadtxt('/Users/rikke.ronnow/Desktop/NonParity.txt')

# turns1=np.append(turns1,-1)
# turns2=np.append(turns1,)

# parity=np.append(parity,0)
# nonparity=np.append(nonparity,0)

turns1=np.append(turns1,160)
turns2=np.append(turns1,160)

parity=np.append(parity,160)
nonparity=np.append(nonparity,160)

# turns2=np.loadtxt('random_turns2.txt')


# turns3=np.loadtxt('random_turns3.txt')


# turns=np.concatenate((turns1,turns2))
# turns=np.concatenate((turns,turns3))

# long_turns=np.loadtxt('random_turns.txt')
# turns=np.concatenate((turns,long_turns))

cmap = plt.get_cmap('RdYlGn')
colors = [cmap(i) for i in np.linspace(0, 1, 5)]

'''plt.hist(turns1,bins=20)
plt.hist(parity,bins=20)
plt.hist(nonparity,bins=20)

plt.ylabel('Frequency')
plt.xlabel('Turns')

plt.show()'''

plt.hist(turns1, bins = 40, histtype='step', cumulative=True, color='g',label='Random')
plt.hist(parity, bins = 40, histtype='step', cumulative=True, color='r',label='Parity')
plt.hist(nonparity, bins = 40, histtype='step', cumulative=True, color='k',label='Non parity')
#plt.hist(turns2, bins = 40, histtype='step', cumulative=True, color=colors[1])

#plt.hist(turns2, bins = 50, histtype='step', cumulative=True, color=colors[4])

plt.legend()
plt.xlim(0,100)
plt.ylabel('Number of games')
plt.xlabel('Turns')

plt.savefig('histogram',bbox_inches='tight',dpi=1000)

plt.show()
