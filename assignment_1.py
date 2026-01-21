#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

# We make the assumption the lowest score possible is 0
HIGH_SCORE = 0
 
# Get the test scores.
# list makes iterating easier, casting to int assuming scores are not decimal
# Adding error handling for non-numeric types seems overkill, erroring out is an acceptable failure state
test_scores = []
test_scores.append(int(input('Enter the score for test 1: ')))
test_scores.append(int(input('Enter the score for test 2: ')))
test_scores.append(int(input('Enter the score for test 3: ')))

# Check if there is a new high score
for score in test_scores:
    if (score > HIGH_SCORE):
        HIGH_SCORE = score
# Calculate the average test score.
# Using functions to make things cleaner
average = sum(test_scores) / len(test_scores)
# Print the average.
# String addition is simple
print('The average score is: ' + str(average))
# If the average is a high score,
# congratulate the user.
# Fix the variable name
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
# Once again assuming integers for simplicity
len1 = int(input("Enter the length of the first rectangle: "))
wid1 = int(input("Enter the width of the first rectangle: "))
len2 = int(input("Enter the length of the second rectangle: "))
wid2 = int(input("Enter the width of the second rectangle: "))

# performing calculations inline since they are not getting reused
print("The area of the first rectangle is " + str(len1 * wid1))
print("The area of the second rectangle is " + str(len2 * wid2))

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name = input("Please enter your first name: ")
age = int(input("Please enter your age in years: "))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
# Using String interpolation, once again for simplicity
print(f"Happy birthday, {name}!  You are {age} years old today!")

