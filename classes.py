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
            my_move (str): 'rock' 'paper' or 'sciessors'
            opp_move (str): 'rock' 'paper' or 'sciessors'
        Outputs:
            my_move (str): 'rock' 'paper' or 'sciessors'
            opp_move (str): 'rock' 'paper' or 'sciessors'
        Example:
            >>> recall('paper', 'rock')
            Your opponent played rock in the previous round.
        """
        return f"Your opponent played {opp_move} in the previous round.", my_move, opp_move

class Human(Player): # TODO: fix extra arg error
    def move():
        hmove = input("What's your play? ").lower()
        while hmove not in self.moves:
            hmove = input("What's your play? ").lower()
        return hmove

# may need to add intermediate Computer player class
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

    def score(self, p1_move, p2_move, p1_score=0, p2_score=0): # FIX: track score
        """
        Inputs:
            p1_move (str): Player 1's move
            p2_move (str): Player 2's move
            p1_score (int): Player 1's current score
            p2_score (int): Player 2's current score
        Outputs:
            Winner + Scoreboard (str): Whether player 1 or 2 won and their incremented scores
            p1_score (int): Player 1's updated score
            p2_score (int): Player 2's updated score
        Purpose:
            Compute the winner of a round and display a scoreboard of the game thus far and track the current player scores.
        Example:
        """
        score = f" Score\n {p1_score} | {p2_score}\n-----"

        if p1_move == p2_move:
            return "No winner.\n" + score, p1_score, p2_score
        elif ((p1_move == 'rock' and p2_move == 'scissors') or \
              (p1_move == 'scissors' and p2_move == 'paper') or \
              (p1_move == 'paper' and p2_move == 'rock')):
              p1_score += 1
              return "Player 1 wins!\n" + score, p1_score, p2_score
        else:
            p2_score += 1
            return "Player 2 wins!\n" + score, p1_score, p2_score

    def play_round(self):
        # Move
        p1_move = self.p1.move()
        p2_move = self.p2.move()
        print(f"Player 1: {p1_move} \nPlayer 2: {p2_move}\n-----")

        # Score
        scoreboard, p1_score, p2_score = self.score(p1_move, p2_move)
        print(scoreboard)

        # Recall
        p1_recall, p1_my_move, p1_opp_move = self.p1.recall(p1_move, p2_move)
        p2_recall, p2_my_move, p2_opp_move = self.p2.recall(p2_move, p1_move)
        print(f"Player 1:\n  {p1_recall} \nPlayer 2:\n  {p2_recall}")

        # Values to update
        return p1_move, p2_move

    def play_game(self):
        print("Game start!")
        rounds = 5
        for round in range(1,rounds+1): # non-technical counting
            print(f"\n..........\nRound {round}:\n..........\n")
            p1_move, p2_move = self.play_round()

        print("Game over!")
