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
        #print('You hit a ship!')
        self.__hits=self.__hits+1
    
    def add(self,s,p,o):
        self.__size.append(s)
        self.__pos.append(p)
        self.__orient.append(o)
        self.__hits.append(0)
        return self
    
    def sunk(self):
        if self.__size==self.__hits:
            #print('You sunk a ship!')
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
    x=random.randint(0,9)
    y=random.randint(0,9)
    while guess_board[x,y]!=0:
        x=random.randint(0,9)
        y=random.randint(0,9)
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

ship4=Ship(4, np.array([0,9]),"Horizontal")

ship_array=np.append(ship_array,ship4)


for ship in ship_array:
    xcoord,ycoord=coordinates(ship)
    add_ships(ship_board,xcoord,ycoord)

print(ship_board)

'''guess1=np.array([0,0])    
   
guess_ship(guess1)    

guess2=np.array([0,9])    
   
guess_ship(guess2)  
    
print(ship_board)  
print(guess_board)  

guess_ship(np.array([0,0]))

guess_ship(np.array([4,4]))

guess_ship(random_guess())

for ship in ship_array:
    print('hits',ship.hits())

print(guess_board)
print(ship1.pos()[0])'''
#%%%
'''os.system('clear')

turns=10



for turn in range(turns):
  print("Turn:", turn + 1, "of", turns)
  print("Ships left:", len(ship_array))
  print()
  
  #x = int(input("Guess an x coordinate: "))
  #y = int(input("Guess a y coordinate: "))
  

  #guess_coord=np.array([x,y])
  guess_coord=less_random_guess()
  
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
  '''

#%%
'''
turns=100

def play_game(times,guess_strategy):
    a=[]
    for time in range(times):
        for turn in range(turns):
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
          a.append(turns)
        else:
          print("All the ships have been sunk. You win!")
          a.append(turns)
      
    return np.array(a)  
 ''' 
#%%

 
