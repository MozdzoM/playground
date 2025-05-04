import random

from game_data import data
from art import logo, vs


def pick_new_guess():
    new_pick = random.choice(data)
    while new_pick == pick_A:
        new_pick = random.choice(data)
    return new_pick

def compare(a, b):
    """Returns info about who has more followers"""
    if a['follower_count'] > b['follower_count']:
        return 'A'
    elif b['follower_count'] > a['follower_count']:
        return 'B'
    else:
        return 'even'

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


pick_A = random.choice(data)
pick_B = pick_new_guess()
score = 0

print(logo)
while True:
    # print A vs. B info
    print(f"Compare A: {format_data(pick_A)}")
    print(vs)
    print(f"Against B: {format_data(pick_B)}")

    # prints info and returns guess value
    guess = input("Who has more followers? Type 'A' or 'B': ").title()
    answer = compare(pick_A, pick_B)

    # clear the screen
    print("\n" * 30)
    print(logo)

    # if right: take 2nd celeb, make him 1st and pick another random
    # if wrong: final score screen w/ play again? prompt
    if answer == 'even'or guess == answer:
        score += 1
        pick_A = pick_B
        pick_B = pick_new_guess()
        print(f"You're right! Current score: {score}")
    elif guess != answer:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
