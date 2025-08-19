#
# Ronnie Johnson
# 8/19/25
# Asks for the user to input their name and then returns the user's name in a greeting message. It also prints
# today's date.
#

import datetime

name = input('What is your name? ')
print(f'Welcome to CSC121 {name}!')
print(f'Today is {datetime.date.today():%B %d, %Y}')
