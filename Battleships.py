#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:00:22 2022

@author: rikke.ronnow
"""

#assign different values to each location depending on whether it has been hit
#sunk, missed, or never been shot

import numpy as np

Board_player=np.zeros((5,5))
Board_opponent=np.zeros((5,5))

class Ship:
    def __init__(self, size=2, position=np.array([0.0,0.0]),orientation="Horizontal",hits=0):
        self.__size=[size]
        self.__pos=[position]
        self.__orient=[orientation]
        self.__hits=[hits]
    
    def __repr__(self):
        return "size(s)=%s position(s)=%s, orientation(s)=%s, hits=%s" % ( self.__size, self.__pos, self.__orient, self.__hits)
    
    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.__size, self.__pos, self.__orient, self.__hits)
    
    def pos(self):
        return self.__pos[-1]
    
    def orient(self):
        return self.__orient[-1]
    
    def size(self):
        return self.__size[-1]
    
    def hits(self):
        return self.__hits[-1]
    
    def add(self,s,p,o):
        self.__size.append(s)
        self.__pos.append(p)
        self.__orient.append(p)
        self.__hits.append(0)
        return self
    
def coordinates(ship):
        
    size=ship.size()
    position=ship.pos()
    orientation=ship.orient()
        
    if orientation=="Horizontal":
        xcoordinates=[]
        ycoordinates=[]
            
        for i in range(size):
            xcoord=position[0]+i
            ycoord=position[1]
            xcoordinates.append(xcoord)
            ycoordinates.append(ycoord)
            
    if orientation=="Vertical":
        xcoordinates=[]
        ycoordinates=[]
            
        for i in range(size):
            xcoord=position[0]
            ycoord=position[1]
            xcoordinates.append(xcoord)
            ycoordinates.append(ycoord)
            
    else:
        xcoordinates=position[0]
        ycoordinates=position[1]
                
    return xcoordinates,ycoordinates
    
        
def guess(position):
    def __init__(self, position=np.array([0.0,0.0])):
        self.__pos=[position]

    def hit(self):
        for coord in ship.coordinates():
            if self.__pos==coord:
                return 1