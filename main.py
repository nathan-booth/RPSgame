"""
Welcome player
Explain rules

choose round number from odd num >= 3
randomly pick computer player

play game
  human = input().lower() in ["rock", "paper", "scissors"]
    if invalid, try again
  computer move
  round winner
  display running score (for loop)
    if last round, then final score
    else running score
"""
import classes

game = classes.Game(0,0,3)
print(game.human_score)
