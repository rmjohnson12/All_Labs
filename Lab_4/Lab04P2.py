##
# Student Name - Ronnie Johnson
# Date - 09/14/25
# Trish's Swap Shop Calculator
#
# Global Constants
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
TAX_RATE = 0.065  # Tax Rate of 6.5%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.

def calc_and_display_total(books, dvds, games):
    # Calculate totals for each item
    book_total = books * BOOK_PRICE
    dvd_total = dvds * DVD_PRICE
    game_total = games * GAME_PRICE

    # Subtotal
    subtotal = book_total + dvd_total + game_total

    # Tax
    tax_amount = subtotal * TAX_RATE

    # Calculate final total
    total = subtotal + tax_amount

    # Results
    print(f"Books: ${book_total:.2f}")
    print(f"DVDs: ${dvd_total:.2f}")
    print(f"Games: ${game_total:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")


main()
