"""
Welcome player
Explain rules

1. choose round number from odd num >= 1
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
from random import randint

if __name__ == '__main__':
    player_pool = {'human': classes.Human(),
                   'rocker': classes.Rocker(),
                   'randomizer': classes.Randomizer(),
                   'copycat': classes.Copycat(),
                   'cycler': classes.Cycler()}
    player1 = input("""Who is Player 1? The choices are Human, Rocker, Randomizer, Copycat, and Cycler.""").lower()
    player2 = input("""Who is Player 2? The choices are Human, Rocker, Randomizer, Copycat, and Cycler.""").lower()

    game = classes.Game(player_pool[player1], player_pool[player2])
    game.play_match()
