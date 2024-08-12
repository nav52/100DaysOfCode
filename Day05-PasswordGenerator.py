# Problem Statement
"""
Build a Password Generator Project
Tasks:
    The program will ask:

    How many letters would you like in your password?
    How many symbols would you like?
    How many numbers would you like?

    The objective is to take the inputs from the user to these questions and then generate a random password. 

    Easy Version
        Generate the password in sequence. Letters, then symbols, then numbers.
    Hard Version
         Every time you generate a password, the positions of the symbols, numbers, and letters are different. 
         This will make the password more difficult for hackers to crack.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy_version_list = []
for num in range(0,nr_letters):
    easy_version_list.append(random.choice(letters))
for num in range(0, nr_symbols):
    easy_version_list.append(random.choice(symbols))
for num in range(0, nr_numbers):
    easy_version_list.append(random.choice(numbers))

print(easy_version_list)
hard_version_list = easy_version_list.copy()
random.shuffle(hard_version_list)
print(hard_version_list)

print(f"Your password is: {''.join(hard_version_list)}")
