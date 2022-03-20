# Battleship

This is the repository for the guessing strategies; hunt with and without parity. These codes are written within the file 'parity'. We can change the type of strategy to play by running (x,y = parity(guess_board)) or (x,y = non_parity(guess_board)).

A random placement strategy is written in 'RandomPlacement'. This file can be imported into parity to play the guessing strategies against a random placement of ships. 

For each game simulation, a text file is created with the number of guesses it takes to win a game. 

See Parity_board for a visual representation of what the parity strategy does. It makes a random guess on only the white tiles until it makes a hit. 
