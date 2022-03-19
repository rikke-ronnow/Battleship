## Battleship

This is the repository for reinforcement learning model of the battleship.

#Setting:

3x3 board and 2x1 ship
ship location is determined by a setting the left/top location of the horiztonal/vertical 2x1/1x2 ship

#Heat map explained:

horizontal_1:
ship set to be horizontal
possibility of ship locations evenly distributed between (0,1) and (1,1)

horizontal_2: 
ship set to be horizontal
possibility of ship locations evenly distributed between (0,0), (0,1), (1,0) and (1,1)

all:
ship orientation is random
possibility of ship locations evenly distributed between (0,0), (0,1), (1,0) and (1,1)
