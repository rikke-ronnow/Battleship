#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:59:47 2022

@author: shimin
"""

#Random
import Battleships
import random 
import copy 

class Battleship: 
    def __init__ (player1, player2):
        player1.guess_board = copy.deepcopy (Battleship.guess_board)
        player1.ships = copy.deepcopy (Battleship.ship_array) 
        player1.player = player
              
        #player1.board = [['#' for y in range(player1.guess_board)] for x in range(player1.guess_board)]

    
        #player1.shots = [[False for y in range (player1.BOARD_SIZE)]for x in range (player1.BOARD_SIZE)]
        #self.shots sets whole board to false, when shot, it will be true

def make_move(board,x,y):
	
	#make a move on the board and return the result, hit, miss or try again for repeat hit
	if board[x][y] == 1:
		return "miss"
	elif board [x][y] ==2:
		return "hit"
    else:
		return "try again" #0 (no guesses), 3(whole ship is sunk)



def random_move(player1, ships):
    while board[x][y] == 1:
        position_X = random.randint(0, player1.BOARD_SIZE -1)
        position_Y = random.randint(0, player1.BOARD_SIZE -1)
        
        res = make_move(board,position_X, position_Y)
        
        #if res == "hit":
         #   print "Hit at " + str(x+1) + "," + str(y+1)
			#check_sink(board,x,y)
			#board[x][y] = '$'
			#if check_win(board):
			#	return "WIN"
		#elif res == "miss":
		#	print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
		#	board[x][y] = "*"

		#if res != "try again":
			
		#	return board
        #if not player1.shots[position_X][position_Y]:
         #   player1.shots[position_X][position_Y] = True 
          #  break  #check if position has been shot at
        
        return position_X, position_Y

def check_sink(board,x,y):

	#figure out what ship was hit
	if board[x][y] == "A":
		ship = "Aircraft Carrier"
	elif board[x][y] == "B":
		ship = "Battleship"
	elif board[x][y] == "S":
		ship = "Submarine" 
	elif board[x][y] == "D":
		ship = "Destroyer"
	elif board[x][y] == "P": 
		ship = "Patrol Boat"
	
	#mark cell as hit and check if sunk
	board[-1][ship] -= 1
	if board[-1][ship] == 0:
		print ship + " Sunk"



#def make_move(player1, position_x, position_y):
       # if not self.validate_position(position_x, position_y):
            #return False

        #state = self.board[position_x][position_y]

        #if state == '#':
            #self.board[position_x][position_y] = '!'
           #return False
        #elif state == '@' or state == '!':
            #return False
        #else:
            #self.hit_ship(position_x, position_y)
            #self.board[position_x][position_y] = '@'
            #return True
            
class hunt_target(Battleship):
    def __init__ (player1):
        Battleship.__init__(player1)
        
        player1.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        #player1.lastX = 0 ##!
        #player1.lastY = 0 ##!
        #player1.position_X = 0
        #player1.position_Y = 0
        player1.potential_targets = []
#storing hits into lastX and lastY
        player1.shots[position_X][position_Y] = True
        player1.lastX = position_X
        player1.lastY = position_Y
        return position_X, position_Y
 #remembering the last shot
    
 
    
def hits(player1, is_hit, ships):
    last_x = player1.lastX
    last_y = player1.lastY
    if board[x][y] == 2:
        
        # target to the left
        target_left = (last_x - 1, last_y)
        if player1.validate_position(target_left[0], target_left[1]) and target_left not in player1.potential_targets:
            player1.potential_targets.append(target_left)

        # target to the right
        target_right = (last_x + 1, last_y)
        if player1.validate_position(target_right[0], target_right[1]) and target_right not in player1.potential_targets:
            player1.potential_targets.append(target_right)

        # target above
        target_above = (last_x, last_y - 1)
        if player1.validate_position(target_above[0], target_above[1]) and target_above not in player1.potential_targets:
            player1.potential_targets.append(target_above)

        # target below
        target_below = (last_x, last_y + 1)
        if player1.validate_position(target_below[0], target_below[1]) and target_below not in player1.potential_targets:
            player1.potential_targets.append(target_below)
            
            #parity
        if len(player1.potential_targets) == 0:
    while True:
        position_x = random.randint(0, player1.BOARD_SIZE - 1)
        position_y = random.randint(0, player1.BOARD_SIZE - 1)
        if not player1.shots[position_x][position_y]:
            if position_x % 2 == 0 and position_y % 2 == 0 or position_x % 2 == 1 and position_y % 2 == 1:
                break

