# Battleship

## Intro

This repository contains code which is used to run a game of Battleship. It also contains a probabilistic strategy and a reinforcement learning strategy, which can be passed as arguments to the function which runs the game.

Battleship is a popular game around the world in which two players place their “battleships” at positions in a lattice unknown to the opposing player. They then take turns guessing the location of their opponent's ship, if they guess correctly they have “hit” their opponent's ship and if they ‘hit’ all the parts of a ship then the ship is ‘sunk’. The player who sinks all their opponent’s ships first wins.

Using Battleship_Visualisation.py allows the player to play a game of Battleships with 5 Battleships in randomly generated positions and orientations. After each round a plot is generated showing whether the player hit a ship. If the player hits a ship, that square on the graph will turn red, if they miss it will turn black, and if they sink the ship, the whole ship will turn green. Once they have sunk all the ships they have won, and if they do not sink all of the ships in a set number of turns, a board will display the ships/parts of ships that they haven't hit yet.

Battleship.py plays the game using a random guesser 100 times with 3 battleships in randomly generated positions. It saves as a .txt file a list of how many turns it took for the strategy to win the game. 

RandomPlacement.py contains functions necessary to randomly generate ships of a specified size. It is currently set to 1 2x1 ship, 1 3x1 ship and 1 4x1 ship.

Histograms.py reads in .txt files containing the number of turns taken to win Battleships, and uses these to plot a cumulative histogram.