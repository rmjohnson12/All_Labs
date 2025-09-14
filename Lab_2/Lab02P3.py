#
# Ronnie Johnson
# 8/31/2025
# Bargain Swap Shop Calculator
#

# Get the inputs
tot_purchase = float(input('Enter the total purchase amount: '))
member = input('Is the customer a loyalty program member (y/n): ')

# Add in the sales tax and compute the total after tax
tax_amt = tot_purchase * 0.065
total = tot_purchase + tax_amt

# Gift card calculations
if member == 'y' and tot_purchase >= 50 and tot_purchase <= 100:
    giftCard = 15
elif member == 'y' and tot_purchase > 100:
    giftCard = 25
elif member == 'n' and tot_purchase > 100:
    giftCard = 5
else:
    giftCard = 0

# Output the totals up to 2 decimals
print(f"Sales tax: ${tax_amt:.2f}")
print(f"Total after tax: ${total:.2f}")
print(f"Gift Card Awarded: ${giftCard}")