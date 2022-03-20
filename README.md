## Battleship

This is the repository for q-learning model of the battleship.

#Setting:

3x3 board and 2x1 ship
ship location is determined by a setting the left/top location of the horiztonal/vertical 2x1/1x2 ship

#Algorithm:

The idea is the agent will play the games many times and get reward/punishment for different actions at different states.
Actions are making a guess on different locations. States are the specific situation of the board. 

#Heat map explained:

Aim: Want to test whether the q table can reflect the placing rule

Placing rule: column is fixed so it must be col 1&2, but the ship can be in either row 1/2 with equal probability

Production: The q-table is trained under the placing rule, generating q-values foe each state-action pair. After training, the q-values for different locations at initial state is taken to generate the heatmap.

Result: All the 4 possible locations have roughly similar values and are much higher than the rest of the board as expected. So the agent is more likely to choose those 4 locations which is the right thing to do.
