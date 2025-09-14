#
# Ronnie Johnson
# 09/07/25
# This program calculates what a customer should pay based on the number of books, DVDs, and games being purchased it
# also includes sales tax
# It also validates the input to make sure it is within a certain range

# Define the prices of the items and set as variables
book = 2.25
dvd = 4.35
game = 5.00

# Input: Ask the user to input the number(s) of each item they are purchasing
# num_book = float(input('Enter the number of books: '))
# num_dvd = float(input('Enter the number of DVDs: '))
# num_game = float(input('Enter the number of games: '))

num_book = int(input('Enter the number of books: '))
while num_book < 0 or num_book > 30:
    print(f"Number of books must be between 0 and 30.")
    num_book = int(input("Enter the number of books: "))

num_dvd = int(input('Enter the number of DVDs: '))
while num_dvd < 0 or num_dvd > 15:
    print(f"Number of dvds must be between 0 and 15.")
    num_dvd = int(input("Enter the number of dvds: "))

num_game = int(input('Enter the number of games: '))
while num_game < 0 or num_game > 10:
    print(f"Number of games must be between 0 and 10.")
    num_game = int(input("Enter the number of games: "))

# Processing: Calculate the total cost before tax, sales tax, and total cost after tax
cost_before_tax = book * num_book + dvd * num_dvd + game * num_game
sales_tax = 0.065 * cost_before_tax
total_cost = cost_before_tax + sales_tax

# Output: Display the cost before tax, sales tax, and total cost after tax
print(f"Cost before tax: ${cost_before_tax:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Cost after tax: ${total_cost:.2f}")
