"""
Game
  init

  welcome rules

  pick rounds

  run round

  stats (score, player moves)

  round score

  final score

"""
# TODO: add game versions, like:
# traditional
# rock paper scissors spock lizard
# running computer tournament
class Game():
    """
    Inputs: num total_rnds
    Outputs: None
    Purpose:
      Initialize the game starting conditions, including starting scores and the number of rounds to play.
    Example:
        >>> game = classes.Game(3)
        >>> print(game.total_rnds)
        3
    """
    human_score = 0
    computer_score = 0

    def __init__(self, total_rnds):
        self.total_rnds = total_rnds

    def play_rnd():
        """
        Inputs: None
        Outputs: str stating who won
        Purpose:
            Run one round of play. Get each player's move, compute the winner, and display the new scores.
        Example:
            >>> game = classes.Game(3)
            >>> game.play_rnd()
            X won!
            --- Score ---
                X: 1
                Y: 0
        """
        hMove = Human.move() # ensure this accepts lower case
        cMove = Rocker.move() # testing; computer player should be set earlier
        compute_winner(hMove, cMove)
        match_stats() # TODO: write match_stats()

    def compute_winner(human_move, computer_move):
        """
        Inputs:
            hmove (str): Human move
            cmove (str): Computer move
        Outputs: winner (str): Text saying who won and why
        Purpose:
            Given the players' moves as strings, return who won and why.
        Example:
            >>> hmove = "Rock"
            >>> cmove = "Paper"
            >>> compute_winner(hmove, cmove)
            Computer wins!
        """
        matchups = {'rockpaper': ['Paper', 'Computer'],
                    'rockscissors': ['Rock', 'Human'],
                    'paperscissors': ['Scissors', 'Computer'],
                    'paperrock': ['Paper', 'Human'],
                    'scissorsrock': ['Rock', 'Computer'],
                    'scissorspaper': ['Scissors', 'Human']}
        move_winner = matchups[human_move+computer_move][0]
        player_winner = matchups[human_move+computer_move][1]

        if move_winner == 'Rock':
            print(player_winner + 'wins!')
        if move_winner == 'Paper':
            print(player_winner + 'wins!')
        if move_winner == 'Scissors':
            print(player_winner + 'wins!')

    def play_match():
        pass

    def match_stats():
        pass

# --- Player Classes ---
class Player():
  def __init__():
    pass

  def move():
    pass

  def recall_opp_move():
    pass

class Human(Player):
  def __init__():
    pass

  def move():
    pass

# may need to add intermediate Computer player class
class Rocker(Player):
  def __init__():
    pass

class Randomizer(Player):
  def __init__():
    pass

class Copycat(Player):
  def __init__():
    pass

class Cycler(Player):
  def __init__():
    pass
