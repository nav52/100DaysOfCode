# Problem Statement
"""
Build a Rock, Paper, Scissors game. 
Tasks:
    Get the user choice 
    Use randomization to get the Computer's Choice.
    Scissor cuts Paper, Paper covers Rock and Rock crushes Scissor.
    Based on the above logic, decide who wins and display it.
"""

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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rock_paper_scissor = [rock, paper, scissors]

if user_input not in [0,1,2]:
    print("Invalid Input. You Lose!!")
else:
    print(rock_paper_scissor[user_input])

computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(rock_paper_scissor[computer_choice])

if user_input == computer_choice:
    print("It's a draw")
elif user_input == 0:
    if computer_choice == 1:
        print("You Lose!")
    else:
        print("You Win!!")
elif user_input == 1:
    if computer_choice == 2:
        print("You Lose!")
    else:
        print("You Win!!")
else:
    if computer_choice == 0:
        print("You Lose!")
    else:
        print("You Win!!")
