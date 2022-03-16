#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:54:05 2022

@author: rikke.ronnow
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap



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
        print('You hit a ship!')
        self.__hits=self.__hits+1
    
    def add(self,s,p,o):
        self.__size.append(s)
        self.__pos.append(p)
        self.__orient.append(o)
        self.__hits.append(0)
        return self
    
    def sunk(self):
        if self.__size==self.__hits:
            print('You sunk a ship!')
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
            board[guess[0],guess[1]]=2
            if ship.sunk():
                for i in range(len(xcoords)):
                    guess_board[xcoords[i],ycoords[i]]=3
                    board[xcoords[i],ycoords[i]]=1

            break
        else:
            guess_board[guess[0],guess[1]]=1
            board[guess[0],guess[1]]=3

            
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
    
#print(ship_board)

            

cmap = ListedColormap(['w','g', 'r','k'])

# Make a 9x9 grid...
nrows, ncols = 10,10
board = np.zeros(nrows*ncols)


board = board.reshape((nrows, ncols))

row_labels = range(nrows)
col_labels = range(ncols)
plt.matshow(board,cmap=cmap)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()


           
turns=40

for turn in range(turns):
  
    
  print("Turn:", turn + 1, "of", turns)
  print()
  
  x = int(input("Guess a row: "))
  y = int(input("Guess a column: "))
  
  guess_coord=np.array([x,y])

  guess_ship(guess_coord)

  row_labels = range(nrows)
  col_labels = range(ncols)
  plt.matshow(board,cmap=cmap,vmin=0,vmax=3)
  plt.xticks(range(ncols), col_labels)

  plt.yticks(range(nrows), row_labels)

  plt.show()

  
  if np.sum(ship_board)==0:
      break

# End Game
if np.sum(ship_board)!=0:
  print("You lose!")
else:
  print("All the ships have been sunk. You win!")










