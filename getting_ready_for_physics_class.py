'''
Getting Ready for Physics Class

You are a physics teacher preparing for the upcoming semester. You want to provide your students 
with some functions that will help them calculate some fundamental physical properties.

'''

# Function to convert Fahrenheit to Celcius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Function to convert Celcius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

# Test functions
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
print(f100_in_celsius, c0_in_fahrenheit)
# Outputs 37.77777777777778 32.0
# We could fix this with Decimal module

# Variables to test our functions with
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function to calculate the force of an object
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

# Calculate the force of the train
train_force = get_force(train_mass, train_acceleration)
print(train_force)
# Outputs 226800
# Let make it more readable
print(f'The GE train supplies {train_force} Newtons of force.')
# Outputs: The GE train supplies 226800 Newtons of force.

# Function to calculate the energy of an object: E = m*c**2
# Set c to a default value
def get_energy(mass, c=3*10**8):
  energy = mass * c ** 2
  return energy

# Calculate the energy of a bomb  
bomb_energy = get_energy(bomb_mass)
print(f'A 1kg bomb supplies {bomb_energy} Joules')
# Outputs: A 1kg bomb supplies 90000000000000000 Joules
# Future: Implement scientific notation

# Function to calculate work done by the object
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

# Calculate the work done by the train
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f'The GE train does {train_work} Joules of work over {train_distance} meters.')
# Outputs: The GE train does 22680000 Joules of work over 100 meters.
# Future: Implement scientific notation