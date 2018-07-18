import classes


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
