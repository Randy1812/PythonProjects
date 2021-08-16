import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]
op = ["It's a Draw", "You Win!!", "You Lose", "You entered an invalid number. You Lose."]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0, 2)
if user_choice > 2 or user_choice < 0:
    print(op[3])
else:
    print(symbols[user_choice])
    print(f"Computer Chose:\n{symbols[comp_choice]}")
    if user_choice == comp_choice:
        print(op[0])
    elif (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (
            user_choice == 2 and comp_choice == 0):
        print(op[2])
    else:
        print(op[1])