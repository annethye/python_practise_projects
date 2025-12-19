'''
Time Traveller's Toolkit
A Python script to simulate the experience of time travel using various Python modules

You'll start by building a custom module, then work with dates and times, perform precise calculations, 
implement random selection features, and finally, generate a personalised time travel message.

For clarity the custom_module.py file contains the function generate_time_travel_message:
def generate_time_travel_message(year, destination, cost):
  return f'Pack your bags! You\'re travelling to {destination} in the year {year}. The cost of this trip will be {cost} €'
'''

# Import datetime module with an alias of dt
import datetime as dt
# Import Decimal from the decimal module
from decimal import Decimal 
# Import the randint and choice functions from the random module
from random import randint, choice
# Import your file custom_module.py
import custom_module


# Retrieve the current date and time
current_date = dt.date.today()
current_time = dt.datetime.now().time()
# Print out date and time
print(f'Today\'s date is: {current_date} \nThe exact time is: {current_time }')

# Generate a random year between 1900 and 2100 to travel to
target_year = randint(1900, 2100)
# Extract the current year
current_year = current_date.year
# Calculate how many years have been travelled
years_travelled = abs(current_year - target_year)

# Perfrom precise financial calculations using Decimal. Format to two decimal places.
# Base cost for using time travel service
base_cost = Decimal('2000.00')
# Cost multiplier for each year travelled
cost_multiplier = Decimal('9.99')
# Total cost of time travel
cost = base_cost + cost_multiplier * years_travelled

# List of possible destinations for the time travel
destination_possibilities = ['Paris', 'New York', 'London', 'Sydney', 'Cairo']
destination = choice(destination_possibilities)


# Generate time travel message using the function from the custom_module:
print(custom_module.generate_time_travel_message(target_year, destination, cost))


'''
Improvement Ideas:

- Allow user input for destination and year
- Include error handling for invalid inputs.
- Generate target date with month and year specified
- Add more destinations and fun facts about each place and time.
'''