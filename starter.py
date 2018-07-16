"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. By Udacity"""
from random import randint

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class Human(Player):
  def move():
      # validate input
    pass

# may need to add intermediate Computer player class
class Rocker(Player):
    pass

class Randomizer(Player):
    pass

class Copycat(Player):
    pass

class Cycler(Player):
    pass

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
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
