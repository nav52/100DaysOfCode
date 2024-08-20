"""
Build a Blind Auction program
Tasks:
    Get the user input on name and their bid
    Store it in a dictionary 
    Do the above untill all bids are received
    Find the highest bidder from the dictionary and display them as winner
"""

from sidekick_modules.blind_auction_art import logo
print(logo)

# Function to get the highest bidder
def find_highest_bidder(bidders_info):
    winner = ""
    max_amount = 0
    for bidder in bidders_info:
        bid_amount = bidders_info[bidder]
        if bid_amount > max_amount:
            max_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_amount}")

# User inputs for name and bids
bidders_info = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders_info[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bidders_info)
    else:
        print("\n" * 50)