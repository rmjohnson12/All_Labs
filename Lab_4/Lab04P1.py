##
# Student Name - Ronnie Johnson
# Date - 09/14/2025
# Landscape Job Estimator
#
import math  # This library is needed for line 26

FillThisIn = None  # Ignore this line, do not change or remove

# Change all the FillThisIn below with correct implementation

# Global constants for paint job estimator
FEET_PER_BAG = 50
HOURS_PER_BAG = 2
LABOR_CHARGE = 40.00
PROJECT_FEE = 100.00


# main module
def main():
    # Ask the user for the garden space in square feet
    garden_space = float(input('Enter garden space in square feet: '))

    # Ask the user for the mulch price
    mulch_price = float(input('Enter mulch price per bag: '))

    # Calculate number of bags needed
    num_bags = math.ceil(garden_space / FEET_PER_BAG)

    # Calculate labor hours (2 hours labor for every bag of mulch)
    hours_labor = num_bags * HOURS_PER_BAG

    # Calculate cost of labor (including project fee)
    cost_labor = LABOR_CHARGE * hours_labor + PROJECT_FEE

    # Calculate mulch cost
    cost_mulch = num_bags * mulch_price

    # Print cost estimate
    show_cost_estimate(num_bags, hours_labor, cost_mulch, cost_labor)


def show_cost_estimate(bags_mulch, labor_hours, mulch_total, labor_total):
    """
    The showCostEstimate function calculates the total cost
    and displays the cost estimate details.

    :param bags_mulch: Number of bags of mulch
    :param labor_hours: Hours of labor
    :param mulch_total: Total cost of mulch
    :param labor_total: Total cost of labor
    :return:
    """

    # Calculate total cost
    total_cost = mulch_total + labor_total

    # Display results
    print(f'Bags of mulch: {bags_mulch}')
    print(f'Hours of labor: {labor_hours}')
    print(f'Mulch charges: ${mulch_total:.2f}')
    print(f'Labor charges: ${labor_total:.2f}')
    print(f'Total cost: ${total_cost}')

main()
