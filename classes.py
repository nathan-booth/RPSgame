"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. By Udacity"""
from random import randint

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'scissors'

    def recall(self, my_move, opp_move):
        """
        Inputs:
            my_move (str): 'rock' 'paper' or 'scissors'
            opp_move (str): 'rock' 'paper' or 'scissors'
        Outputs:
            my_move (str): 'rock' 'paper' or 'scissors'
            opp_move (str): 'rock' 'paper' or 'scissors'
        Example:
            >>> recall('paper', 'rock')
            Your opponent played rock in the previous round.
        """
        print(f"Your opponent played {opp_move} in the previous round.")
        return my_move, opp_move

class Human(Player): # TODO: test
    def move(self):
        hmove = input("What's your play? ").lower()
        while hmove not in self.moves:
            hmove = input("What's your play? ").lower()
        return hmove

class Rocker(Player):
    def move(self):
        return 'rock'

class Randomizer(Player):
    def move(self):
        return self.moves[randint(0, len(self.moves)-1)]

class Copycat(Player): # TODO: recall previous opp move and copy the move for next move, start with rock
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

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def winner(self, p1_move, p2_move):
        """
        Inputs:
            p1_move (str): Player 1's move
            p2_move (str): Player 2's move
        Outputs:
            Winner (str): Whether player 1 or 2 won
        Purpose:
            Compute the winner of a round.
        Example:
            >>> self.winner('rock', 'paper')
            Player 2 wins!
            >>> self.winner('paper', 'paper')
            No winner.
            >>> self.winner('rock', 'scissors')
            Player 1 wins!
        """
        if p1_move == p2_move:
            return "No winner.\n", 0 # no winner
        elif ((p1_move == 'rock' and p2_move == 'scissors') or \
              (p1_move == 'scissors' and p2_move == 'paper') or \
              (p1_move == 'paper' and p2_move == 'rock')):
              print("Player 1 wins!\n")
              return 1 # player 1
        else:
            print("Player 2 wins!\n")
            return 2 # player 2

    def scoreboard(self, rnd_winner, prev_p1_score, prev_p2_score):
        """
        Inputs:
            scored (int): Encoding of which player score to increment
        Outputs:
            p1_score (int): Player 1's updated score
            p2_score (int): Player 2's updated score
            Scoreboard
        Purpose:
            Display a scoreboard of the game and track the current player scores.
        """
        if rnd_winner == 1:
            new_p1_score = prev_p1_score + 1
            print(f" Score\n {new_p1_score} | {prev_p2_score}\n-----")
            return new_p1_score, prev_p2_score
        elif rnd_winner == 2:
            new_p2_score = prev_p2_score + 1
            print(f" Score\n {prev_p1_score} | {new_p2_score}\n-----")
            return prev_p1_score, new_p2_score
        else:
            print(f" Score\n {prev_p1_score} | {prev_p2_score}\n-----")
            return prev_p1_score, prev_p2_score

    def play_round(self):
        """
        Inputs: None
        Outputs:
            p1_move (str): Player 1's move
            p2_move (str): Player 2's move
        Purpose:
            Get the moves of two players.
        """
        p1_move = self.p1.move()
        p2_move = self.p2.move()
        print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n-----")

        return p1_move, p2_move

    def play_game(self):
        print("Game start!\n")
        rounds = 5
        p1_score = 0
        p2_score = 0
        for round in range(1,rounds+1): # non-technical counting
            print(f"\n..........\nRound {round}:\n..........\n")
            p1_move, p2_move = self.play_round()
            winning_p = self.winner(p1_move, p2_move)
            p1_score, p2_score = self.scoreboard(winning_p, p1_score, p2_score)
            prev_p1_move, prev_p2_move = self.p1.recall(p1_move, p2_move)
            prev_p2_move, p1_opp_move = self.p2.recall(p2_move, p1_move)

        print("\nGame over!")
