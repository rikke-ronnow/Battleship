import numpy as np
import copy
from math import factorial

def shoot(GameState, *locations):
    AlteredGameState = copy.copy(GameState)
    for x in locations:
        AlteredGameState[x[0]][x[1]] = -1
    return AlteredGameState 

def outer(GameState, Ships):
    
    global CountMatrix, n, m
    n, m = np.shape(GameState)
    CountMatrix = np.zeros(shape=(n,m))
    
    
    def inner(Matrix, ShipsLeft):
        
        global CountMatrix
        ShotNotPossible = True
        if ShipsLeft > 0:
            
            for i in range(n):
                for j in range(m - 1):
                    if Matrix[i][j] == 0 and Matrix[i][j + 1] == 0:
                        ShotNotPossible = False
                        inner(shoot(Matrix, (i, j),(i, j + 1)), ShipsLeft - 1)
                    
            for k in range(m):    
                for l in range(n - 1):
                    if Matrix[l][k] == 0 and Matrix[l + 1][k] == 0:
                        ShotNotPossible = False
                        inner(shoot(Matrix, (l, k), (l + 1, k)), ShipsLeft - 1)
                        
            if ShotNotPossible:
                CountMatrix = CountMatrix + (Matrix == -1)/factorial(Ships-ShipsLeft)
        else:
            CountMatrix = CountMatrix + (Matrix == -1)/factorial(Ships)
            
    inner(GameState, Ships)
    
    MaxProb = (0,0)
    
    for i in range(n):
        for j in range(m):
            if CountMatrix[i][j] > MaxProb[0]:
                MaxProb = (i, j)

    return MaxProb

def ShipsLeft(Board):
    return 3 - sum(sum(Board==3))/2

def LocateUnsunk(Board):
    for i, row in enumerate(Board):
        for j, x in enumerate(row):
            if x == 2:
                return (i, j)

def BigAlStrat(Board):
    if sum(sum(Board == 2)) != 0:
        i, j = LocateUnsunk(Board)
        
        if 0 < i < 8 and 0 < j < 8:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if 0 < i < 8 and j == 0:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            
        if 0 < i < 8 and j == 8:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if i == 8 and 0 < j < 8:  
            if Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if 0 == i and 0 < j < 8:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            else:
                return (i, j-1)
            
        if 0 == i and 0 == j:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
        if 0 == i and 8 == j:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            else:
                return (i, j-1)
            
        if 8 == i and 0 == j:  
            if Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            
        if 8 == i and 8 == j:  
            if Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        
    else:
        return outer((Board != 0), ShipsLeft(Board))



