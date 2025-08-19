#
# Ronnie Johnson
# 8/19/25
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.
miles = float(input('Enter number of miles: '))

# Get the speed in MPH.
speed = float(input('Enter speed in MPH:  '))

# Calculate the travel time.
travel_time = miles / speed
# Get any decimal portion of the travel time.
travel_time2 = travel_time - int(travel_time)
# Convert the decimal portion of the travel time to minutes.
travel_mins = 60 * travel_time2
# Get the whole number of hours from the travel time.
travel_hours = int(travel_time)

# Display the travel time as the whole number of hours and the remaining minutes formatted to 2 decimal places.
print(f"You should cover that distance in {travel_hours} hours and {travel_mins:.2f} minutes.")
