import random
from art import logo, vs
from game_data import data


def play_game():
    continue_playing = True
    start = True
    a = random.choice(data)
    score = 0
    while continue_playing:
        if start:
            start = False
        print(logo)
        # print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}  {a['follower_count']}.")
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
        if not start:
            print(f"You're right! Current Score : {score}")
        print(vs)
        b = random.choice(data)
        while b == a:
            b = random.choice(data)
        # print(f"Against B: {b['name']}, {b['description']}, from {b['country']}  {b['follower_count']}.")
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
        ans = input("\nWho has more followers? type 'A' or 'B' : ")
        if ans == 'a' and (a['follower_count'] > b['follower_count']):
            a = b
            score += 1
        elif ans == 'b' and (b['follower_count'] > a['follower_count']):
            a = b
            score += 1
        else:
            print(f"Sorry that's wrong. Final score : {score}")
            break


while input("\n\nDo you want to play ? ") == 'y':
    play_game()
