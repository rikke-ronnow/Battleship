# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:02:42 2022

@author: ryazi
"""

import numpy as np
import random as random

class Field:
    def __init__(self):
        self.position = np.zeros(shape=(10,10))
        #posistion of the 2x1 ship
        self.ship_position1 = np.array([2,1])
        self.ship_position2 = np.array([2,2])
        self.ship_status1 = False #True if any part of the ship is hit
        #self.ship_status2 = False
        
    
    def get_number_of_states(self):
        #product of 
        #3 different possibile status at each location
        #possible location of the 2x1 ship
        #status of different parts of the ship
        return (3*10**2)*(10**4)*4
    
    def get_state(self):
        state = 0
        #so 0-2700 can uniquely represent the status of each location
        for index, x in np.ndenumerate(self.position):
            state += index[0]*x + index[1]*x
        
        #thinking how to get the unique states
        state = state + self.ship_position1[0]*10**4*2
        state = state + self.ship_position1[1]*10**5*2
        state = state + self.ship_position2[0]*10**6*2
        state = state + self.ship_position2[1]*10**7*2
        
        if self.shipstatus1:
            state = state + 1

        return state
        
    def make_action(self, action):
        xy1 = self.ship_posistion1
        xy2 = self.ship_position2
        
        if action != xy1 and xy2:  #Miss the ship
            return -10, False
        
        elif action == xy1 or xy2:  #Hit any part of the ship
            if self.ship_status1 == 0:
                self.ship_status1 = True
                return 20, False
            else:
                return 30, True
            
        elif action == 2:  # Go Left
            if x == 0:
                return -10, False
            else:
                self.position = (x - 1, y)
                return -1, False
        elif action == 3:  # Go Right
            if x == self.size - 1:
                return -10, False
            else:
                self.position = (x + 1, y)
                return -1, False
        elif action == 4:  # Pickup item
            if self.item_in_car:
                return -10, False
            elif self.item_pickup != (x, y):
                return -10, False
            else:
                self.item_in_car = True
                return 20, False
        elif action == 5:  # Drop off item
            if not self.item_in_car:
                return -10, False
            elif self.item_drop_off != (x, y):
                self.item_pickup = (x, y)
                self.item_in_car = False
                return -10, False
            else:
                return 20, True
            
#%%

size = 10
item_start = (0, 0)
item_drop_off = (9, 9)
start_position = (0, 9)
field = Field(size, item_start, item_drop_off, start_position)
number_of_states = field.get_number_of_states()
number_of_actions = 6
q_table = np.zeros((number_of_states, number_of_actions))
epsilon = 0.1
alpha = 0.1
gamma = 0.6
for _ in range(10000):
    field = Field(size, item_start, item_drop_off, start_position)
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
    
    field = Field(size, item_start, item_drop_off, start_position)
    done = False
    steps = 0
    
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
        
        steps = steps + 1
    
    return steps

#%%

runs_rl = [reinforcement_learning() for _ in range(100)]
print(sum(runs_rl)/len(runs_rl))