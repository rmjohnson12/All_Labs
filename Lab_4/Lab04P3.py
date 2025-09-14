##
# Student Name - Ronnie Johnson
# Date - 09/14/25
# Dungeons and Dragonseque Die Roll Simulator

import random

def main():
    # Input validation loop
    num_rolls = int(input("How many times do you want to roll the die? "))
    while num_rolls < 5 or num_rolls > 15:
        print("Enter a number between 5 and 15.")
        num_rolls = int(input("How many times do you want to roll the die? "))

    # Call roll_die function
    roll_die(num_rolls)
    print("Thanks for playing!")


def roll_die(rolls):
    for i in range(1, rolls + 1):
        num_rand = random.randint(1, 20)

        # Critical hit check
        if num_rand == 20:
            result = "CRITICAL HIT!"
        else:
            remainder = num_rand % 4
            if remainder == 0:
                result = "Sword"
            elif remainder == 1:
                result = "Shield"
            elif remainder == 2:
                result = "Spell"
            else:
                result = "Potion"

        print(f"Roll {i}: {num_rand} ==> {result}")

main()
