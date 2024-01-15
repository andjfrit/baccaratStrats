# baccaratStrats
Testing out different baccarat strats simulator
-
baccarat game is standard such as dealings and rules for winner


Initially this is only martingale strategy: which follows the following algorith 

Players start with 12800 units and the starting bet is 100 units
Each player is allowed 3 buy backs if they ever go below 100 units where they can buy back in for 12800 units

The highest win streak, worst loss streak, # of players who go bankrupt, highest winning from any player and more interesting data is kept

1: bet 1 unit on banker.

2: if win: go back to step 1. else: bet 1 unit on Player

3: until win: bet 2 times the previous units on player. On win go back to step 1 

Graph is line graph using pyplot
y: avg winning for each player 
x: the number of hands 

To run simulation:
- download zip
- run main
- input number of players and number of hands for each player to play
- play around with starting info, such as starting wallet, minimum bet, buyback numbers etc...
