#!/usr/bin/env python3

import random

options = ["rock", "paper", "scissors"]

def play_game():
    computer_option = random.choice(options)
    print("\nWelcome to Group2 Rock, Paper, Scissors!")
    user_option = input("Enter your choice (rock, paper, or scissors): ")

    print("You chose:", user_option)
    print("Computer chose:", computer_option)

    if user_option == computer_option:
        print("It's a tie!")
    elif (user_option == "rock" and computer_option == "scissors") or \
         (user_option == "paper" and computer_option == "rock") or \
         (user_option == "scissors" and computer_option == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
