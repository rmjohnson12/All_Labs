#
# Ronnie Johnson
# 8/19/25
# This program calculates what a customer should pay based on the number of books, DVDs, and games being purchased it
# also includes sales tax
#

#Define the prices of the items and set as variables
book = 2.25
dvd = 4.35
game = 5.00

#Input: Ask the user to input the number(s) of each item they are purchasing
num_book = float(input('Enter the number of books: '))
num_dvd = float(input('Enter the number of DVDs: '))
num_game = float(input('Enter the number of games: '))

#Processing: Calculate the total cost before tax, sales tax, and total cost after tax
cost_before_tax = book * num_book + dvd * num_dvd + game * num_game
sales_tax = 0.065 * cost_before_tax
total_cost = cost_before_tax + sales_tax

#Output: Display the cost before tax, sales tax, and total cost after tax
print(f"Cost before tax: ${cost_before_tax:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Cost after tax: ${total_cost:.2f}")
