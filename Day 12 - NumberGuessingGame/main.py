from art import logo
import random


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a random number between 1 and 100.")
    diff = str(input("Choose a difficulty (high / low) : "))
    if diff == "high":
        chances = 5
    elif diff == "low":
        chances = 10
    num = random.randint(1, 100)
    while chances != 0:
        guess = int(input("Make a guess : "))
        if guess == num:
            print("You guessed the number right. You Win!!")
            break
        elif guess > num:
            print("Too High. Guess Again!")
            print(f"You have {chances} tries remaining.")
            chances -= 1
        elif guess < num:
            print("Too Low. Guess Again!")
            print(f"You have {chances} tries remaining.")
            chances -= 1
    if chances < 0:
        print("You Lose")


play_game()
while input("Do you want to play again? (y/n)") == "y":
    play_game()
