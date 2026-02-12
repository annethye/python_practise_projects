'''
Gradebook

You are a student and you are trying to organize your subjects and grades using Python. 
Let's explore what we've learned about lists to organize your subjects and scores.
'''

# Gradebook last semester
last_semester_gradebook = [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65]]

# A list containing the classes taken
subjects = ['physics', 'calculus', 'poetry', 'history']

# A list of corresponding grades
grades = [98, 97, 85, 88]

# Manually create a 2D list to combine subjects and grades
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

# Your grade for visual arts just came in! You got a 93!
gradebook.append(['visual arts', 93])
print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['visual arts', 93]]

# Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.
gradebook[4][1] += 5
print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['visual arts', 98]]

# You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.
# Find the grade value and remove it
gradebook[2].remove(85)
print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry'], ['history', 88], ['visual arts', 98]]

# Add a new 'Pass' value to the poetry class
gradebook[2].append('Pass')
print(gradebook)
# [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['visual arts', 98]]

# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
# [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65], ['physics', 98], ['calculus', 97], 
# ['poetry', 'Pass'], ['history', 88], ['visual arts', 98]]