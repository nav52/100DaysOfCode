# Problem Statement
"""
Create a Tip Calculator using Python
Tasks:
    Get the total bill amount
    Ask the user for the amount of tip that they would give (10, 12, 15)
    Ask the user for the number of people the bill needs to be split for.
    Calculate and display the per user share rounded to 2 decimal places.
"""
# Greet
print("Welcome to the tip calculator!")
# Get Inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# Calculate
tip_as_percent = tip/100
tip_amount = bill*tip_as_percent
total_bill = bill + tip_amount
share_per_person = total_bill/people
final_share = round(share_per_person, 2)
print(f"Each person should pay: ${final_share:.2f}") # .2f keeps the trailing zeros as well (check for 150, 12, 5 inputs and you'll get it)
