"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. By Udacity"""
from random import randint
import itertools

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'paper'

    def learn(self, my_move, their_move):
        pass

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
    cycle = []
    for x in itertools.islice(itertools.cycle(range(3)), Game.play_game.rounds):
        cycle.append(x)
    def move(self):
        move_index = 0
        while move_index <= 2:



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
        rounds = 3
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
