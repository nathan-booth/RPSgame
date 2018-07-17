"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. By Udacity"""
from random import randint

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self, my_move=None, opp_move=None):
        return 'scissors'

    def learn(self, my_move, opp_move):
        """
        Inputs:
            my_move (str):
            opp_move (str):
        Outputs:
            opp_move (str):
        Example:
            >>> learn('paper', 'rock')
            Your opponent played rock in the previous round.
        """
        return f"Your opponent played {opp_move} in the previous round.", my_move, opp_move

class Human(Player):
  def move():
      # validate input
    pass

# may need to add intermediate Computer player class
class Rocker(Player):
    def move(self):
        return 'rock'

class Randomizer(Player):
    def move(self):
        return self.moves[randint(0, len(self.moves)-1)]

class Copycat(Player):
    pass

class Cycler(Player): # TODO: pass previous move to this move
    my_move = ''
    def move(self, my_move=my_move):
        if self.my_move == 'rock':
            my_move = 'paper'
            return self.moves[1]
        if self.my_move == 'paper':
            my_move = 'scissors'
            return self.moves[2]
        else:
            my_move = 'rock'
            return self.moves[0]

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} \nPlayer 2: {move2}\n-----")

        p1_recall, p1_my_move, p1_opp_move = self.p1.learn(move1, move2)
        p2_recall, p2_my_move, p2_opp_move = self.p2.learn(move2, move1)
        print(f"Player 1:\n  {p1_recall} \nPlayer 2:\n  {p2_recall}")

    def play_game(self):
        print("Game start!")
        rounds = 5
        for round in range(1,rounds+1): # non-technical counting
            print(f"\n..........\nRound {round}:\n..........\n")
            self.play_round()
        print("Game over!")
