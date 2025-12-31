'''
The Boredless Tourist

Welcome to The Boredless Tourist, an online application giving you the power to find the parts of the city that fit the pace of your life. 
We at The Boredless Tourist run a recommendation engine using Python. 
We first evaluate what a person's interests are and then give them recommendations in their area to venues, restaurants, and historical
destinations that we think they'll be engaged by.

'''

# git init
# git add script.py
# git commit -m "initial commit"

# Data used to test the functionality 
# Available destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. 
# Erin is in China right now, hopefully we can find some good places to show her.
test_traveller = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# git add script.py
# git commit -m "Added test objects"

# When a traveler arrives at a destination, we want to know where they are! We are going to identify each location based on its index
# in our destinations list. 
# The function takes the destination as a string and returns the index of the destination.
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Test the function:
# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# Returns 2 and 0 which is correct
# print(get_destination_index('Hyderabad, India'))
# Returns ValueError: 'Hyderabad, India' is not in list. As expected.

# Function to return traveller location
def get_traveller_location(traveller):
  traveller_destination = traveller[1]
  # Use previous function to retrieve the destination index
  traveler_destination_index = get_destination_index(traveller_destination)
  return traveler_destination_index

# Test the function:
# test_destination_index = get_traveller_location(test_traveller)
# print(test_destination_index)
# Returns 1 as expected

# git add script.py
# git commit -m "Added logic to find traveller destinations and convert to internal data"

# We want attractions to be an empty list for every destination in destinations
# Like so attractions = [[], [], [], [], []]
attractions = [[] for destination in destinations]
# print(attractions)
# Outputs [[], [], [], [], []] as it should

# Function to add attractions to a destination
def add_attraction(destination, attraction):
  # Use previous function to retrieve destination index
  destination_index = get_destination_index(destination)
  # If the destination exists we have a list for it in attractions.
  # Retrieve and save the list
  attractions_for_destination = attractions[destination_index]
  # Append new attraction
  attractions_for_destination.append(attraction)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
# print(attractions)
# Returns [[], [], [['Venice Beach', ['beach']]], [], []]

# Let's add a few more interesting places to go
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# git add script.py
# git commit -m "Created attractions and functionality for adding new attractions"

# We want to be able to help our travellers find the most interesting places in a new city for them. In order to do that we need to 
# match their interests with the possible locations in a city. Let write a function that does that.
def find_attractions(destination, interests):
  # Use previous function to retrieve destination index
  destination_index = get_destination_index(destination)
  # Retrieve and save attractions at the destination
  attractions_in_city = attractions[destination_index]
  # Create list to save attractions that match traveller's interests
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest


la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)
# Initially returns [['LACMA', ['art', 'museum']]] however we only want only want the name so we append only possible_attraction[0] 
# in the function.
# Returns ['LACMA']

# git add script.py
# git commit -m "Added interest finder logic"

# Now let's get to the main event, connecting people with the attractions that they are interested in.
def get_attractions_for_traveller(traveller):
  # Let's separate out the traveller's data
  traveller_destination = traveller[1]
  traveller_interests= traveller[2]
  # Call previous function
  traveller_attractions = find_attractions(traveller_destination, traveller_interests)
  # Creating string to return attractions at destination that correspon with traveller's interests
  interests_string = 'Hi '
  interests_string += traveller[0]
  interests_string += ', we think you\'ll like these places around '
  interests_string += traveller_destination
  interests_string += ': '
  # Concatenate each attraction to the string
  for attraction in traveller_attractions:
    interests_string += 'The '
    interests_string += attraction
    interests_string += '  '
  return interests_string

# Test traveller
smills_france = get_attractions_for_traveller(['Dereck Smill', 'Paris, France', ['monument']]
)
print(smills_france)
# Returns 'Hi Dereck Smill, we think you'll like these places around Paris, France: The Arc de Triomphe'

# git add script.py
# git commit -m "Added function to generate message for traveler and present attractions they might be interested in."