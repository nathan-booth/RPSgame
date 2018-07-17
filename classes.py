"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. By Udacity"""
from random import randint
import itertools

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
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
        return f"Your opponent played {opp_move} in the previous round."

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

class Cycler(Player):
    def move(self):
        # print(self.my_moves)
        # cycle = []
        # iterate = 0
        # for x in itertools.islice(itertools.cycle(range(3)), 3): # 3 options, 3 rounds, adapted from StackOverflow
        #     cycle.append(x)
        # return self.moves[cycle[iterate]]
        return self.moves[1]

    # def learn(self):
    #     my_moves = []

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
        print(f"Player 1: {move1} \nPlayer 2: {move2}\n-----\n")
        p1_recall = self.p1.learn(move1, move2)
        p2_recall = self.p2.learn(move2, move1)
        print(f"Player 1:\n  {p1_recall} \nPlayer 2:\n  {p2_recall}")

    def play_game(self):
        print("Game start!")
        rounds = 5
        for round in range(1,rounds+1): # non-technical counting
            print(f"\n..........\nRound {round}:\n..........\n")
            self.play_round()
        print("Game over!")
