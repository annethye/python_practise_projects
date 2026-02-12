"""
Magic 8-Ball Simulator

The Magic 8-Ball is a classic toy for fortune-telling and advice. 
Ask any 'Yes' or 'No' question and receive a new fortune each time!
"""

# In order to generate random values random is imported
import random

# Welcome to magic 8-ball
print('''
╔══════════════════════════════════════╗
║ 🎱  WELCOME TO THE MAGIC 8-BALL  🎱  ║
╚══════════════════════════════════════╝
        Ask... if you dare.
      
''')

# Name of person asking the Magic 8-Ball
name = input('What is your name: ' )
print('\n' + 'The cosmos acknowledges your presence ' + name + '\n')

# Today's question in yes or no format 
question = input('Well? What burning nonsense do you need answered this time: ')
print('\n')

# Initialising the Magic 8-ball answer
answer = ''

# In order for the answer to be different each time we run the program, we will utilise randomly generated values.
# Generate a random number between 1 and 12
random_number = random.randint(1, 12)

# Testing if random numbers are being generated:
# print(random_number)

# Using if/elif/else statements to assign different magic 8 ball answers for each randomly generated value
# 12 fortunes defined
if random_number == 1:
    answer = 'Yes - definitely' 
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
elif random_number == 10:
    answer = 'You wish'
elif random_number == 11:
    answer = 'Your guess is as good as mine'
elif random_number == 12:
    answer = 'Signs point to yes'
else:
    # In case the number is accidentally assigned a value outside of our range.
    answer = 'Error'

# Print Statements
# We ideally want our output to have the following format: 
# [Name] asks: [Question]
# Magic 8-Ball’s answer: [Answer]
while not question:
    # The question is an empty string, so let's warn and force the user to provide a question
    print('Empty string detected: Outlook not verbose.')
    question = input('The spirits cannot answer what has not been asked. Ask again: ')
    print('\n')
if not name:
    # The name is an empty string, so let's format the answer
    print('Question: ' + question)
    print('\n')
    print('Magic 8-Ball\'s answer: ' + answer)
else:
    # Print statements with ideal format from above
    print(name + ' asks: ' + question)
    print('\n')
    print('Magic 8-Ball\'s answer: ' + answer)


'''
Ideas for improvement:
- Answers in list
- add functions
- f-string formatting
- Add more ascii art
- Import time and add theatrical pauses 

Slight difference in implementation between the above and the codecademy exercise. 
In codecademy name and question are not obtained by user input so this is how empty
strings are dealt with:

if not question:
    print('The Magic 8-Ball cannot provide a fortune unless you ask it something.')
elif not name:
    print('Question: ' + question)
    print('Magic 8-Ball\'s answer: ' + answer)
else:
    print(name + ' asks: ' + question)
    # Magic 8-Ball's answer: [Answer]
    print('Magic 8-Ball\'s answer: ' + answer)
'''