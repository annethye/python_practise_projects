'''
Basta Fazoolin'

You've started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin' with My Heart.
The restaurant has been doing fantastically and seen a lot of growth lately. You've been hired to keep things organised.
The restaurant Take a' Arepa also needs your help.
'''

# Class to create businesses by storing franchises
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
# Class to create franchises by storing menus and an address
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # Method to print out location of franchise
  def __repr__(self):
    return f'This franchise is located at {self.address}.'
  # Method that takes in a time parameter and returns a list of the Menu objects that are available at that time
  def available_menus(self, time):
    menus = []
    for menu in self.menus:
      if menu.start_time <= time < menu.end_time:
        menus.append(menu)
    return menus

#  Class to create menus, return information about the menu and calculate bills
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Method to print out menu availability
  def __repr__(self):
    return f'The {self.name} menu is available from {self.start_time} to {self.end_time}.'
  # Method that takes in a list of names of purchased items and calculates the total price of all items.
  def calculate_bill(self, purchased_items):
   bill = 0
   for item in purchased_items: 
    bill += self.items[item]
   return bill   
    

# Items for sale at Basta Fazoolin'
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caeser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# Items for sale at Aprea
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# Let's instantiate the menus with their name and the start and end time they're available at
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
kids_menu = Menu('Kids', kids_items, 1100, 2100)
arepas_menu = Menu('Take a\' Arepa', arepas_items, 1000, 2000)

# Print the available menus
print(brunch_menu)
print(early_bird_menu)
print(dinner_menu)
print(kids_menu)
print(arepas_menu)
# The Brunch menu is available from 1100 to 1600.
# The Early Bird menu is available from 1500 to 1800.
# The Dinner menu is available from 1700 to 2300.
# The Kids menu is available from 1100 to 2100.
# The Take a' Arepa menu is available from 1000 to 2000.

# Calculate the bill
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])) 
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
# 13.5
# 21.5

# Let's instantiate some franchises by specifying an address and the menus available at that franchise
flagship_store = Franchise('1232 West End Road', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise('12 East Mulberry Street', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
# Print the store locations
print(flagship_store)
print(new_installment)
print(arepas_place)
# This franchise is located at 1232 West End Road.
# This franchise is located at 12 East Mulberry Street.
# This franchise is located at 189 Fitzgerald Avenue.

# Print out available menus at certain times
print('-----------Menus available at 1200 at the flagship-----------')
for menu in flagship_store.available_menus(1200):
    print(menu)
print('-----------Menus available at 1700 at the flagship-----------')
for menu in flagship_store.available_menus(1700):
    print(menu)
print('-----------Menus available at 2100 at Arepas Place-----------')
for menu in arepas_place.available_menus(2100):
    print(menu)
# -----------Menus available at 1200 at the flagship-----------
# The Brunch menu is available from 1100 to 1600.
# The Kids menu is available from 1100 to 2100.
# -----------Menus available at 1700 at the flagship-----------
# The Early Bird menu is available from 1500 to 1800.
# The Dinner menu is available from 1700 to 2300.
# The Kids menu is available from 1100 to 2100.
# -----------Menus available at 2100 at Arepas Place-----------

# Instantiate our businesses. Basta Fazoolin has two franchises, Arepas just has the one.
basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas_business = Business("Take a' Arepa", [arepas_place])

# Lets test out our business by printing out the menu of the franchise at 1200
print(arepas_business.franchises[0].available_menus(1200)[0])
# The Take a' Arepa menu is available from 1000 to 2000.