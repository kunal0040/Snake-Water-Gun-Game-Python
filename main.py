import random

"""
------Snake Water Gun Game------

Rules:
    - Snake drinks water (Snake wins)
    - Gun shoots snake (Gun wins)
    - Water douses gun (Water wins)
    - If both players choose the same, it's a tie.
The game will be played in a best of 3 format, where the first player to win 2 rounds wins the game.

#For functions:
    s | 1 = Snake
    g | -1 = Gun
    w | 0 = Water

"""

print("===============================")
print("------Snake Water Gun Game-----")
print("===============================\n")

rounds = 3
choices = {"s": 1, "g": -1, "w": 0}
reversechoices = {1: "Snake", -1: "Gun", 0: "Water"}

computer_score = 0
user_score = 0
tie_count = 0


def victory_message():
    word_pool = [
        "!!FABULOUS!!",
        "!!EXTRAORDINARY!!",
        "!!!WONDERFUL!!!",
        "!!MARVELOUS!!",
        "!!SPECTACULAR!!",
        "!!SUPERB!!",
        "!!!FANTASTIC!!!",
        "!!AMAZING!!",
        "!!PHENOMENAL!!",
        "!!SPLENDID!!",
        "!!TERRIFIC!!",
        "!!OUTSTANDING!!",
        "!!STUPENDOUS!!",
    ]

    random_word = random.choice(word_pool)
    return random_word


while rounds:
    computer = random.choice([-1, 0, 1])
    userstr = input("Enter your choice: ").lower().strip()
    if userstr not in choices:
        print("INVALID CHOICE! Please enter 's', 'w', or 'g'.\n")
        continue

    user = choices[userstr]

    print(
        f"Computer chose: {reversechoices[computer]} \nYou chose: {reversechoices[user]}"
    )

    if computer == user:
        print("It's a TIE!\n")
        tie_count += 1

        if tie_count == 2:
            print("Two ties already? You two are reading each other's minds!\n")
        elif tie_count == 5:
            print("FIVE TIES?! This is getting eerie. Are you guys twins?\n")
        continue

    else:
        if (
            (user == 1 and computer == 0)
            or (user == -1 and computer == 1)
            or (user == 0 and computer == -1)
        ):
            print("You WIN!\n")
            user_score += 1
        else:
            print("Computer WINS!\n")
            computer_score += 1

    rounds -= 1

print("\n====================================")
print(f"\tComputer Score: {computer_score}")
print(f"\tYour Score: {user_score}")

if user_score > computer_score:
    print(" --------You WIN the game!--------")
    if computer_score == 0:
        print(f"   \t{victory_message()}")
else:
    print(" ------Computer WINS the game!------")
    if user_score == 0:
        print("  -----Better Luck Next Time!-----")

print("====================================")