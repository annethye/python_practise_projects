# Receipts for Lovely Loveseats
# We've decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats
# for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we're going to build a system 
# to help speed up the process of creating receipts for your customers.


# Our first item, the Lovely Loveseat, that is the store's name sake
lovely_loveseat_description ='Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
# Assigning a price to the Lovely Love Seat
lovely_loveseat_price = 254.00

# Adding Stylish Settee to our inventory
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
# Assigning a price to the Stylish Settee
stylish_settee_price = 180.50

# Adding Luxurious Lamp to our inventory 
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
# Assigning a price to the Luxurious Lamp
luxurious_lamp_price = 52.15

# Defining a sales tax of 8.8%
sales_tax = 0.088


# Initialising a variable to keep a running tally of the customer's expenses
customer_one_total = 0

# Initialising a list to keep descriptions of items purchased
customer_one_itemisation = ''

# Our customer has decided they are going to purchase our Lovely Loveseat! 
customer_one_total += lovely_loveseat_price
customer_one_itemisation += lovely_loveseat_description

# Our customer has decided to purchase the Luxurous Lamp!
customer_one_total += luxurious_lamp_price
# Adding the next item description on a new line
customer_one_itemisation += '\n' + luxurious_lamp_description

# The customer is ready to check out. Let's calculate the sales tax
customer_one_tax = customer_one_total * sales_tax
# Adding the tax to the total
customer_one_total += customer_one_tax

# Lets print out their receipt:
print('Customer One items:')
print(customer_one_itemisation)
print('Customer One Total:')
# Formatting total to only show 2 decimals
print((f'{customer_one_total:.2f}'))



