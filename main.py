"""
Welcome player
Explain rules

1. choose round number from odd num >= 3
2. randomly pick computer player
3. Initialize class game
4. play rounds; for each round:
    A. get player moves
        I. human move should be validated on case and spelling
        II. human should try again until they input valid move
    B. compute score
    C. display running score
    D. display opponents' previous move
"""
import classes

game = classes.Game(3)
print(game.total_rnds)
