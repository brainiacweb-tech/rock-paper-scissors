#!/usr/bin/env python3
"""
Rock Paper Scissors Game
Author: brainiacweb-tech
"""
import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def play():
    scores = {"You": 0, "Computer": 0, "Ties": 0}
    print("\n Rock Paper Scissors — first to 3 wins!\n")
    while max(scores["You"], scores["Computer"]) < 3:
        player = input("Choose (rock/paper/scissors) or q to quit: ").strip().lower()
        if player == 'q': break
        if player not in CHOICES:
            print("Invalid choice."); continue
        computer = random.choice(CHOICES)
        print(f"  Computer chose: {computer}")
        if BEATS[player] == computer:
            print("  You win this round!"); scores["You"] += 1
        elif BEATS[computer] == player:
            print("  Computer wins this round!"); scores["Computer"] += 1
        else:
            print("  It's a tie!"); scores["Ties"] += 1
        print(f"  Score -> You: {scores['You']}  Computer: {scores['Computer']}  Ties: {scores['Ties']}\n")
    if scores["You"] == 3:
        print("You are the champion!")
    elif scores["Computer"] == 3:
        print("Computer wins the match!")

if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != 'y':
            break
