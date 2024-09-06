"""
Build a Blackjack Game
Tasks:
    Define the functions for deal_card, calculate_score, compare scores and decide winner
    Deal 2 cards each for user and computer.
    Request user if they need the next card.
    Based on input, deal, calculate, compare and decide winner.
    Ace is both 11 and 1.
    11 & 10 is a Blackjack. Show the score as 0 to indicate blackjack and call the winner
"""


from sidekick_modules.blackjack_art import logo
import random


# Function to decide winner of blackjack
def compare(user_score, comp_score):
    """ Takes the user and computer score, compares and decides the winner """
    if comp_score == 0:
        print("You Lose😤. Computer has a Blackjack!!")
    elif user_score == 0:
        print("You Win😃. You have a Blackjack!!")
    elif user_score > 21:
        print("You went over. You Lose😤")
    elif comp_score > 21:
        print("Opponent went over. You Win😃")
    elif user_score == comp_score:
        print("It's a Draw🤝")
    elif user_score > comp_score:
        print("You Win😃")
    else:
        print("You Lose😤")


def calculate_score(cards_list):
    """ Takes a list of cards and returns the sum"""
    if sum(cards_list) == 21 and len(cards) == 2:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


# Function to pick a card
def deal_card():
    """ Returns a random card from the deck"""
    return random.choice(cards)


# cards A, 2-10, J, Q, K
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_blackjack():
    """ Function to play the game of Blackjack """
    print(logo)
    your_cards = []
    computer_cards = []
    your_score = -1
    computer_score = -1
    is_game_over = False

    # Deal 2 cards for each player
    for _ in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {your_cards}, current score: {calculate_score(your_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            is_game_over = True
        else:
            # Check if the user wants another card
            need_next_card = input("Type 'y' to get another card, type 'n' to pass: ").upper()
            if need_next_card == 'Y':
                your_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(your_score, computer_score)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == 'y':
    print("\n" * 50)
    play_blackjack()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()