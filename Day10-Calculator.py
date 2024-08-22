"""
Build a Calculator program
Tasks:
    Define the functions for add, subtract, multiply and divide
    Map the operator symbols to functions using dictionary
    Ask the user to type the first number.
    Ask the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
    Ask the user to type the second number.
    Work out the result based on the chosen mathematical operator.
    Ask if the user wants to continue working with the previous result.
    If yes, loop to use the previous result as the first number and then repeats the calculation process.
    If no, ask the user for the fist number again and wipes all memory of previous calculations.
    If end, exit the program
"""


from sidekick_modules.calculator_art import logo
print(logo)

# Functions for calculator operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary to store the operations based on symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    number_1 = float(input("Give the first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick one of the operations to perform: ")
        number_2 = float(input("Give the next number: "))
        result = operations[operator](number_1, number_2)
        print(f"{number_1} + {number_2} = {result}")
        carry_on = input(f"Type 'yes' to performing operations with {result} or Type 'no' to start over or Type 'end' to exit the calculator: ").lower()
        if carry_on == 'yes':
            number_1 = result
        elif carry_on == 'no':
            should_accumulate = False
            print("\n"*30)
            calculator()
        else:
            return

calculator()