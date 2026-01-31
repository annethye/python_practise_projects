'''
Len's Slice
You work at Len's Slice, a new pizza joint in the neighborhood. 
You are going to use your knowledge of Python lists to organize some of your sales data.
'''

# To keep track of the kinds of pizzas you sell:
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
# To keep track of how much each kind of pizza slice costs:
prices = [2, 6, 1, 3, 2, 7, 2]

# Your boss wants you to do some research on $2 slices.
# Count the number of occurrences of 2 in the prices list:
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# 3

# Find the number of pizzas we sell:
num_pizzas = len(toppings)
print(f'We sell {num_pizzas} different kinds of pizza!')
# We sell 7 different kinds of pizza!

# Create a 2D list with toppings and prices. For this new list make sure the prices come before the topping name.
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7,'anchovies'], [2,'mushrooms']]
print(pizza_and_prices)
# [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_and_prices.sort()
print(pizza_and_prices)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]

# Find the cheapest pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# [1, 'cheese']

# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# [7, 'anchovies']

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. 
# Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.pop()
print(pizza_and_prices)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple']]

# Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings.
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple']]

# Three mice walk into the store. They don't have much money (they're mice), but they do each want different pizzas.
# Store the 3 lowest cost pizzas in a new list
three_cheapest = pizza_and_prices[:3]

# Great job! The mice are very pleased and will be leaving you a 5-star review.
print(three_cheapest)
# [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]