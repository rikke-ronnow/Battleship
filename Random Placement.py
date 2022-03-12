#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:59:56 2022

@author: shimin
"""
import numpy as np
import random
from Battleships import Ship, coordinates, add_ships

def ship_validation(board, ship):
    x,y = ship.pos()
    for c in ship.pos():
        if c < 0 or c > 9:
            return False
    
    if ship.size() < 0:
        return False
    
    if ship.orient() == "Horizontal":
        if x+ship.size()-1>9:
            return False
        for i in range(ship.size()):
            if board[x+i][y] != 0:
                return False
    elif ship.orient() == "Vertical":
        if y+ship.size()-1>9:
            return False
        for i in range(ship.size()):
            if board[x][y+i] != 0:
                return False
    else:
        return False
    return True
    

def ship_placement_random(l:list=[2,3,4,4]):
    board_temp = np.zeros((10,10))
    ship_arr = np.array([])
    for length in l:
        ship_temp = Ship(length, 
                         np.array([random.randint(0,9),random.randint(0,9)]), 
                         random.choice(["Horizontal", "Vertical"]))
        while not ship_validation(board_temp, ship_temp):
            ship_temp = Ship(length, 
                             np.array([random.randint(0,9),random.randint(0,9)]), 
                             random.choice(["Horizontal", "Vertical"]))
        x_temp, y_temp = ship_temp.pos()
        if ship_temp.orient() == "Horizontal":
            for i in range(length):
                board_temp[x_temp+i][y_temp] = 1
        elif ship_temp.orient() == "Vertical":
            for i in range(length):
                board_temp[x_temp][y_temp+i] = 1
        ship_arr=np.append(ship_arr,ship_temp)
    return ship_arr


s = ship_placement_random()
print(s)




