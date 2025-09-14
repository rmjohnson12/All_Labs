import random

guess_num=1
num_rand = random.randint(100, 999)
num_str = str(num_rand)
print("num_rand =", num_rand)  # For testing purposes, remove or comment out in production

num_entered = int(input(f'Guess #{guess_num}: '))

def main(num_entered):

    while num_entered != num_rand:
        num_entered = int(input(f'Guess #{guess_num+1} #: '))
        guess_num=guess_num+1

    else:
        print("You got it!")
        again = str(input("Do you want to play again? (yes or no): ")).lower()

    if again == "yes":
         print("Thanks for playing!")

