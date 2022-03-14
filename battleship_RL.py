# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 00:02:42 2022

@author: ryazi
"""
#%%

#Code by Rikke

import numpy as np
import random
import os

ship_board=np.zeros((3,3))
guess_board=np.zeros((3,3))

class Ship:
    def __init__(self, size=2, position=np.array([1,1]),orientation="Horizontal",hits=0):
        self.__size=size
        self.__pos=position
        self.__orient=orientation
        self.__hits=hits
    
    def __repr__(self):
        return "size(s)=%s position(s)=%s, orientation(s)=%s, hits=%s" % ( self.__size, self.__pos, self.__orient, self.__hits)
    
    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.__size, self.__pos, self.__orient, self.__hits)
    
    def pos(self):
        return self.__pos
    
    def orient(self):
        return self.__orient
    
    def size(self):
        return self.__size
    
    def hits(self):
        return self.__hits
    
    def updatehits(self):
        self.__hits=self.__hits+1
    
    def add(self,s,p,o):
        self.__size.append(s)
        self.__pos.append(p)
        self.__orient.append(o)
        self.__hits.append(0)
        return self
    
    def sunk(self):
        if self.__size==self.__hits:
            return True
        else:
            return False
    
    
def coordinates(ship):
        
    size=ship.size()
    position=ship.pos()
    orientation=ship.orient()
    xcoordinates=np.array([])
    ycoordinates=np.array([])   

    
    if orientation=="Horizontal":
        for i in range(size):
            xcoord=position[0]+i
            ycoord=position[1]
            xcoordinates=np.append(xcoordinates,xcoord)
            ycoordinates=np.append(ycoordinates,ycoord)
            
    elif orientation=="Vertical":    
        for i in range(size):
            xcoord=position[0]
            ycoord=position[1]+i
            xcoordinates=np.append(xcoordinates,xcoord)
            ycoordinates=np.append(ycoordinates,ycoord)
            
    else:
        xcoordinates=position[0]
        ycoordinates=position[1]         
    return xcoordinates.astype(int),ycoordinates.astype(int)
    

def add_ships(board,xcoordinates,ycoordinates):
    for i in range(xcoordinates.size):
        board[xcoordinates[i],ycoordinates[i]]=8
        
def guess(board,guess):
    if board[guess[0],guess[1]]!=0:
        board[guess[0],guess[1]]=2
        return True
    else:
        board[guess[0],guess[1]]=1
        return False
    
def guess_ship(guess):
    for ship in ship_array:
        xcoords=coordinates(ship)[0]
        ycoords=coordinates(ship)[1]
        if guess[0] in xcoords and guess[1] in ycoords:
            if ship_board[guess[0],guess[1]]!=0:
                ship.updatehits()
            guess_board[guess[0],guess[1]]=2
            ship_board[guess[0],guess[1]]=0
            if ship.sunk():
                for i in range(len(xcoords)):
                    guess_board[xcoords[i],ycoords[i]]=3
                return 3
            return 2
            break
        else:
            guess_board[guess[0],guess[1]]=1
            return 1

ship_array=np.array([])

ship1=Ship()

ship_array=np.append(ship_array,ship1)

for ship in ship_array:
    xcoord,ycoord=coordinates(ship)
    add_ships(ship_board,xcoord,ycoord)
#%%

class Field:
    def __init__(self,ship,guess_board):
        #useless for now, using guess_board and ship_board instead
        self.board = guess_board
        self.ship_position = coordinates(ship)[0]
        self.ship_position2 = coordinates(ship)[0]
        self.ship_status1 = ship.hits()
        
    
    def get_number_of_states(self):
        #product of 
        #4 different possibile status at each location
        #9 location
        return 4**9
    
    def get_state(self):
        #encoding each location and its status into an integer
        state = 0
        for i,x in enumerate((guess_board.reshape(-1))):
            state += int(x*2**(2*i))
        return state

    def make_action(self, action):
        
        #different action and their corresponding reward
        location_list = [[1, 1], [0, 0], [0, 1], [0, 2], [2, 0], [2, 1], [2, 2], [1, 0], [1, 2]]
        result = guess_ship(location_list[action])
        if result == 1:  # missed
            return -10, False
        elif result == 2:  # hit
            return +10, False
        elif result == 3:  # sunk
            return +20, True
        
    
#%%

#set up board
ship_board=np.zeros((3,3))
guess_board=np.zeros((3,3))
field = Field(ship1,guess_board)

#set up q table
number_of_states = field.get_number_of_states()
number_of_actions = 9
q_table = np.zeros((number_of_states, number_of_actions))

#parameters
epsilon = 0.9 #high cuz want mainly exploring for training
alpha = 0.1
gamma = 0.6

#training
for _ in range(10000):
    
    done = False
    int_list = [0,1,2,3,4,5,6,7,8]
    
    ship_board=np.zeros((3,3))
    guess_board=np.zeros((3,3))
    
    ship_array=np.array([])
    
    p1 = random.randint(0,1)
    p2 = random.randint(0,1)
    ship1=Ship(position=np.array([p1,p2]))
    
    ship_array=np.append(ship_array,ship1)
    
    for ship in ship_array:
        xcoord,ycoord=coordinates(ship)
        add_ships(ship_board,xcoord,ycoord)
    
    while not done:
        state = field.get_state()
        p = random.uniform(0, 1)
        if p < epsilon:
            i = random.randint(0, len(int_list)-1)
            action = int_list[i]
            int_list.remove(action)
        else:
            action = np.argmax(q_table[state])
            
        reward, done = field.make_action(action)
        
        #formula for calculating q value
        # Q[state, action] = (1 – alpha) * Q[state, action] + alpha * (reward + gamma * max(Q[new_state]) — Q[state, action])
        
        new_state = field.get_state()
        new_state_max = np.max(q_table[new_state])
        
        q_table[state, action] = (1 - alpha)*q_table[state, action] + alpha*(reward + gamma*new_state_max - q_table[state, action])

#%%

#set up the model
def reinforcement_learning():
    epsilon = 0.1 #low cuz want to use trained q table
    alpha = 0.1
    gamma = 0.6
    
    done = False
    int_list = [0,1,2,3,4,5,6,7,8]
    
    ship_board=np.zeros((3,3))
    guess_board=np.zeros((3,3))

    
    ship_array=np.array([])
    
    p1 = random.randint(0,1)
    p2 = random.randint(0,1)
    ship1=Ship(position=np.array([p1,p2]))
    
    ship_array=np.append(ship_array,ship1)
    
    for ship in ship_array:
        xcoord,ycoord=coordinates(ship)
        add_ships(ship_board,xcoord,ycoord)
    
    steps = 0
    
    while not done:
        state = field.get_state()
        p = random.uniform(0, 1)
        if p < epsilon:
            i = random.randint(0, len(int_list)-1)
            action = int_list[i]
            int_list.remove(action)
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

#average step required to win the game
runs_rl = [reinforcement_learning() for _ in range(1000)]
print(sum(runs_rl)/len(runs_rl))