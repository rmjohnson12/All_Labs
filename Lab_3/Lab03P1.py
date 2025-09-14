#
# Ronnie Johnson
# 09/07/2025
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Accumulators
acc_books = 45
acc_dvds = 32
acc_games = 15

# Display the inventory stock table.
for month in range(1, 4):
    books += acc_books
    dvds += acc_dvds
    games += acc_games
    print(f'Month {month}')
    print(f'\tBooks: {books}')
    print(f'\t DVDs: {dvds}')
    print(f'\tGames: {games}')
