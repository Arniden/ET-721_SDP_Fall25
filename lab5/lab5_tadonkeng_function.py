"""
Arnaud Tadonkeng
function file
Sep 15, 2025
lab 5, function
"""
# example 1: Define a function that passes two numbers and reutrn the product of it
def product(a=0,b=0):
    c = a*b
    return c

#Example 2: function to calculate the hypotenuse
def hypotenuse(side1, side2):
    return (side1**2 + side2**2)**0.5

# Example 3: function to check if the number is postive, negative, or zero. 
# The function returns a string
def check_number(num):
    if(num>0):
        return "POSITIVE"
    elif (num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
# Example 4: function to calculate the average of a list of grades, and return 'true' if the average is greater than 60, otherwise, it returns 'false'
 
def check_grades(grades):
 # Initialize the average grade value
    avg = 0
#sum the individual 'g' from list 'grades' into 'avg'
    for g in grades:
        avg +=g
# find the average grade
        avg /= len(grades)
        return avg
    
def check_pass(avg_grade):
# check if the average is greather than 60
    if avg_grade >= 60:
        return True
    else:
        return False
    
    #LAB EXERCISE

# Function to generate a random integer between min_num and max_num (inclusive)
import random
def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

# Function to compare a guess number with the random number
def compare_guess(random_num, guess_num):
    if random_num < guess_num:
        print("The number is smaller than the guess number")
    elif random_num > guess_num:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")
