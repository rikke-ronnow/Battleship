#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:00:22 2022

@author: rikke.ronnow
"""

#assign different values to each location depending on whether it has been hit
#sunk, missed, or never been shot

import numpy as np
import random
#import os

ship_board=np.zeros((10,10))
guess_board=np.zeros((10,10))

class Ship:
    def __init__(self, size=2, position=np.array([0.0,0.0]),orientation="Horizontal",hits=0):
        self.__size=size
        self.__pos=position
        self.__orient=orientation
        self.__hits=hits
    
    def __repr__(self):
        return "size=%s position=%s, orientation=%s, hits=%s" % ( self.__size, self.__pos, self.__orient, self.__hits)
    
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
                return "Sunk"
            else:
                return "Hit"
        
        else:
            guess_board[guess[0],guess[1]]=1
            return "MIss"

        
#%%

def random_guess():
    x=random.randint(0,9)
    y=random.randint(0,9)
    return np.array([x,y])

def less_random_guess():
    x=random.randint(0,7)
    y=random.randint(0,7)
    while guess_board[x,y]!=0:
        x=random.randint(0,7)
        y=random.randint(0,7)
    return np.array([x,y])

#%%

ship_board=np.zeros((10,10))
guess_board=np.zeros((10,10))

ship_array=np.array([])

ship1=Ship()

ship_array=np.append(ship_array,ship1)


ship2=Ship(3,np.array([2,1]),"Vertical")

ship_array=np.append(ship_array,ship2)

ship3=Ship(4, np.array([6,6]),"Horizontal")

ship_array=np.append(ship_array,ship3)
'''
ship4=Ship(4, np.array([0,9]),"Horizontal")

ship_array=np.append(ship_array,ship4)

ship5=Ship(5, np.array([4,3]),"Vertical")

ship_array=np.append(ship_array,ship5)'''


for ship in ship_array:
    xcoord,ycoord=coordinates(ship)
    add_ships(ship_board,xcoord,ycoord)

print(ship_board)
#%%%



def ship_validation(board, ship):
    x,y = ship.pos()
    for c in ship.pos():
        if c < 0 or c > 7:
            return False
    
    if ship.size() < 1:
        return False
    
    if ship.orient() == "Horizontal":
        if x+ship.size()-1>7:
            return False
        for i in range(ship.size()):
            if board[x+i][y] != 0:
                return False
    elif ship.orient() == "Vertical":
        if y+ship.size()-1>7:
            return False
        for i in range(ship.size()):
            if board[x][y+i] != 0:
                return False
    else:
        return False
    return True
    

def ship_placement_random(l:list=[2,2,2]):
    board_temp = np.zeros((8,8))
    ship_arr = np.array([])
    for length in l:
        while True:
            ship_temp = Ship(length, 
                             np.array([random.randint(0,7),random.randint(0,7)]), 
                             random.choice(["Horizontal", "Vertical"]))
            if ship_validation(board_temp, ship_temp):
                break
        #while not ship_validation(board_temp, ship_temp):
        #    ship_temp = Ship(length, 
        #                     np.array([random.randint(0,9),random.randint(0,9)]), 
        #                     random.choice(["Horizontal", "Vertical"]))
        x_temp, y_temp = ship_temp.pos()
        if ship_temp.orient() == "Horizontal":
            for i in range(length):
                board_temp[x_temp+i][y_temp] = 1
        elif ship_temp.orient() == "Vertical":
            for i in range(length):
                board_temp[x_temp][y_temp+i] = 1
        ship_arr=np.append(ship_arr,ship_temp)
    #print(board_temp)
    return ship_arr


#%%

turns=100
a=[]
for time in range(100):
    ship_board=np.zeros((8,8))
    guess_board=np.zeros((8,8))

    '''ship_array=np.array([])
    
    ship1=Ship()
    
    ship_array=np.append(ship_array,ship1)
    
    
    ship2=Ship(3,np.array([2,1]),"Vertical")
    
    ship_array=np.append(ship_array,ship2)
    
    ship3=Ship(4, np.array([6,6]),"Horizontal")
    
    ship_array=np.append(ship_array,ship3)
    
    ship4=Ship(4, np.array([0,9]),"Horizontal")
    
    ship_array=np.append(ship_array,ship4)'''
    ship_array=ship_placement_random()
    
    
    for ship in ship_array:
        xcoord,ycoord=coordinates(ship)
        add_ships(ship_board,xcoord,ycoord)
    for turn in range(turns):
          
         guess_coord=less_random_guess()
          
         guess_ship(guess_coord)

         if np.sum(ship_board)==0:
             break

    if np.sum(ship_board)!=0:
         a.append(turn)
    else:
         a.append(turn)  

#%%

turns=np.array(a)

np.savetxt('random_8x8.txt',turns)    


