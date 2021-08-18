############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    return random.choice(cards)


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        print("You Lose")
    if user_score == dealer_score:
        return "It's a Draw"
    elif dealer_score == 0:
        return "You Lose. Dealer has BlackJack"
    elif user_score == 0:
        return "You Win!. You have BlackJack"
    elif user_score > 21:
        return "You Lose"
    elif dealer_score > 21:
        return "You Win"
    elif user_score > dealer_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    game_over = False
    for i in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())
    while not game_over:
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer's first card: {dealer_cards[0]}")
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Do you want to draw another card ? ") == "y":
                user_cards.append(deal_cards())
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    user_cards.append(deal_cards())
                else:
                    game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your Final Hand: {user_cards}, Your Final Score: {user_score}")
    print(f"Dealer's Final Hand: {dealer_cards}, Dealer's Final Score: {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Do you wish to play? ") == "y":
    play_game()
