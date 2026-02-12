'''
Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal's Shippers. 
Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

This program will take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers.
Sal's Shippers has several different options for a customer to ship their package:

- Ground Shipping, which is a small flat charge plus a rate based on the weight of your package. 
Price per Pound: 
- 2 lb or less:	$1.50. Over 2 lb but less than or equal to 6 lb:	$3.00. Over 6 lb but less than or equal to 10 lb:	$4.00. Over 10 lb:	$4.75
Flat charge:
- $20

Ground Shipping Premium, which is a much higher flat charge, but you aren't charged for weight.
Flat charge:
- $125

- Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Price per Pound:
- 2 lb or less:	$4.50. Over 2 lb but less than or equal to 6 lb:	$9.00. Over 6 lb but less than or equal to 10 lb:	12.00. Over 10 lb:	$14.25
No Flat charge 
'''

# Defining weight of package in pounds
weight = 4.8

# Ground Shipping. Implementing price per pound cost and the flat charge per package. See prices above
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print('Ground shipping cost for your ' + str(weight) + 'lb package is: $' + str(cost_ground))
# Ground shipping cost for your 4.8lb package is: $34.4

# Premium Gound Shipping
cost_premium_ground = 125
print('Premium ground shipping cost for your ' + str(weight) + 'lb package is: $' + str(cost_premium_ground))
# Premium ground shipping cost for your 4.8lb package is: $125

# Drone Shipping. Implementing price per pound cost. See prices above
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print('Drone shipping cost for your ' + str(weight) + 'lb package is: $' + str(cost_drone))
# Drone shipping cost for your 4.8lb package is: $43.199999999999996

# Improvements to implement later:
# Round numbers to 2 decimals
# Use try except to make sure weight is number
# Implement functions
# Use logic to automatically spit out the cheapest option.