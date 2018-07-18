import classes

player_pool_text = """You may choose from the following player pool:
  Human: you control the moves
  Rocker: computer that always chooses rock
  Randomizer: computer that moves randomly
  Copycat: computer that imitates the opponent's previous move
  Cycler: computer that cycles through rock, paper, and scissors"""

if __name__ == '__main__':
    player_pool = {'human': classes.Human(),
                   'rocker': classes.Rocker(),
                   'randomizer': classes.Randomizer(),
                   'copycat': classes.Copycat(),
                   'cycler': classes.Cycler()}
    print(player_pool_text)
    player1 = input("Who is Player 1?").lower()
    player2 = input("Who is Player 2?").lower()
    while player1 not in player_pool or player2 not in player_pool:
        player1 = input("Who is Player 1?").lower()
        player2 = input("Who is Player 2?").lower()

    game = classes.Game(player_pool[player1], player_pool[player2])
    game.play_match()
