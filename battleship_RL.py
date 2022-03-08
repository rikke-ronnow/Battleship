# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:02:42 2022

@author: ryazi
"""
from Battleships.py import *
import numpy as np
import random as random

ship1 = Battleships.Ship()

class Field:
    def __init__(ship):
        self.board = np.zeros(shape=(10,10))
        #thinking how to get the 2x1 ship
        self.ship_position = ship.pos()
        self.ship_position2 = 
        self.ship_status1 = ship.hits()
        
    
    def get_number_of_states(self):
        #product of 
        #3 different possibile status at each location
        #possible location of the 2x1 ship
        #status of different parts of the ship
        return 0
    
    def get_state(self):
        state = 0
        for i,x in enumerate((self.board.reshape(-1))):
            state += int(x*2**(2*i))
        return state
    
    #unfinished
    def make_action(ship, guess):
        
        if guess_ship(guess_input) == sth:  # missed
                return -10, False
        elif guess_ship(guess_input) == sth:  # hit
                return +10, False
        elif guess_ship(guess_input) == sth:  # sunk
                return +20, True
        elif guess_ship(guess_input) == sth:  # repeated
                return -20, False
            
#%%

field = Field(ship)
number_of_states = field.get_number_of_states()
number_of_actions = 100
q_table = np.zeros((number_of_states, number_of_actions))
epsilon = 0.1
alpha = 0.1
gamma = 0.6
for _ in range(10000):
    field = Field(ship)
    done = False
    
    while not done:
        state = field.get_state()
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 5)
        else:
            action = np.argmax(q_table[state])
            
        reward, done = field.make_action(action)
        # Q[state, action] = (1 – alpha) * Q[state, action] + alpha * (reward + gamma * max(Q[new_state]) — Q[state, action])
        
        new_state = field.get_state()
        new_state_max = np.max(q_table[new_state])
        
        q_table[state, action] = (1 - alpha)*q_table[state, action] + alpha*(reward + gamma*new_state_max - q_table[state, action])

#%%

def reinforcement_learning():
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.6
    
    field = Field(ship)
    done = False
    steps = 0
    
    while not done:
        state = field.get_state()
        if random.uniform(0, 1) < epsilon:
            action = guess_ship(guess)
        else:
            action = np.argmax(q_table[state])
            
        reward, done = field.make_action(action)
        # Q[state, action] = (1 – alpha) * Q[state, action] + alpha * (reward + gamma * max(Q[new_state]) — Q[state, action])
        
        new_state = field.get_state()
        new_state_max = np.max(q_table[new_state])
        
        q_table[state, action] = (1 - alpha)*q_table[state, action] + alpha*(reward + gamma*new_state_max - q_table[state, action])
        
        steps = steps + 1
    
    return steps

#%%

runs_rl = [reinforcement_learning() for _ in range(100)]
print(sum(runs_rl)/len(runs_rl))