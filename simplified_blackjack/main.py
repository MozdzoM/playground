import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and calculate their score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def print_results(my_score, computer_score):
    """Compares final results"""
    if my_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 21:
        print("Lose, opponent has Blackjack 😱")
    elif my_score == 21:
        print("Win with a Blackjack 😎")
    elif my_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif my_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")


def blackjack():
    print(logo)
    my_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    my_score = 0
    computer_score = 0
    is_game_over = False

    while not is_game_over:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if my_score == 21 or computer_score == 21 or my_score > 21:
            is_game_over = True
        else:
            draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw == "y":
                my_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print_results(my_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 30)
    blackjack()