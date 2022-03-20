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
    
    MaxProb = (0,(0,0))
    
    for i in range(n):
        for j in range(m):
            if CountMatrix[i][j] > MaxProb[0]:
                MaxProb = (CountMatrix[i][j], (i, j))

    return MaxProb[1]

def ShipsLeft(Board):
    return 3 - sum(sum(Board==3))/2

def LocateUnsunk(Board):
    for i, row in enumerate(Board):
        for j, x in enumerate(row):
            if x == 2:
                return (i, j)

def BigAlStrat(Board):
    n, m = np.shape(Board)
    
    if sum(sum(Board == 2)) != 0:
        i, j = LocateUnsunk(Board)
        
        if 0 < i < n-1 and 0 < j < m-1:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if 0 < i < n-1 and j == 0:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            
        if 0 < i < n-1 and j == m-1:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if i == n-1 and 0 < j < m-1:  
            if Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        if 0 == i and 0 < j < m-1:  
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
        if 0 == i and m-1 == j:  
            if Board[i+1][j] == 0 or Board[i+1][j] == 2:
                return (i+1, j)
            else:
                return (i, j-1)
            
        if n-1 == i and 0 == j:  
            if Board[i][j+1] == 0 or Board[i][j+1] == 2:
                return (i, j+1)
            elif Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            
        if n-1 == i and m-1 == j:  
            if Board[i-1][j] == 0 or Board[i-1][j] == 2:
                return (i-1, j)
            else:
                return (i, j-1)
            
        
    else:
        return outer((Board != 0)*1, ShipsLeft(Board))

data = [30,
 24,
 23,
 31,
 14,
 13,
 27,
 26,
 23,
 26,
 16,
 25,
 14,
 30,
 26,
 31,
 31,
 26,
 22,
 13,
 32,
 29,
 35,
 26,
 30,
 30,
 16,
 19,
 31,
 23,
 29,
 23,
 18,
 31,
 33,
 23,
 17,
 19,
 29,
 27,
 29,
 27,
 19,
 25,
 30,
 27,
 35,
 30,
 18,
 30,
 35,
 27,
 26,
 24,
 23,
 23,
 25,
 29,
 33,
 23,
 18,
 23,
 23,
 22,
 30,
 29,
 26,
 29,
 23,
 24,
 19,
 29,
 14,
 23,
 29,
 28,
 29,
 14,
 23,
 29,
 32,
 13,
 23,
 25,
 19,
 25,
 19,
 30,
 34,
 30,
 26,
 28,
 14,
 23,
 17,
 19,
 24,
 30,
 34,
 29]