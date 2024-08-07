# Problem Statement
"""
Generate a Band Name using Python
Tasks:
    Create a greeting for your program.
    Ask the user for the city that they grew up in and store it in a variable.
    Ask the user for the name of a pet and store it in a variable.
    Combine the name of their city and pet and show them their band name.

Note:
    Make sure the input cursor shows on a new line:
"""

print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of your Pet?\n")
print("Your Band Name could be: " + city + " " + pet)