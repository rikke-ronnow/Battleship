## Battleship

This is the repository for reinforcement learning model of the battleship.

#Setting:

3x3 board and 2x1 ship
ship location is determined by a setting the left/top location of the horiztonal/vertical 2x1/1x2 ship

#Heat map explained:

Aim: Want to test whether the q table can reflect the placing rule
Placing rule: column is fixed so it must be col 1&2, but the ship can be in either row 1/2 with equal probability
Result: All the 4 possible locations have roughly similar values and are much higher than the rest of the board
