"""
Arnaud Tadonkeng
Lab 3, Python conditional Statement and loops
Sep 8, 2025

"""

"""
Modify example 1
- use while loop to validate if the user_number is between 1 and 9
- user can only guess three times. This can be done using a for loop or a while
"""
#Conditional Statement
print("\n ----- Example 1: if, elif,.... else -----")

# Validate user_number between 1 and 9
while True:
    try:
        user_number = int(input("Enter a number between 1 and 9: "))
        if 1 <= user_number <= 9:
            break
        else:
            print("Number must be between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Guessing loop (3 attempts)
target_number = user_number  # The number to guess
for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}: Guess the number: "))
    if guess == target_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Incorrect guess.")
else:
    print(f"Sorry, you've used all attempts. The number was {target_number}.")
    
print("End of guessing!")

print("\n ----- Example 2: controll flow with logical operators -----")
# 'and', 'or', 'not' operators.
# 'and' operator returns TRUE ONLY if all statements are true
# 'or' operator returns TRUE if at least one of the statement is true
# 'not' operator  returns the invert of the logic. True --> not operator --> false

"""
example 2:
- children from age 5 to 9 are only given milk for breakfast
- children from 10 to 14 are given sandwich
- children 15 and older are given a burger
"""
age_student = int(input("Enter an age: "))
lunch ="None"
if age_student <=9 and age_student>=5:
    lunch = "milk"
elif age_student>=10 and age_student<=14:
    lunch = "sandwich"
elif age_student>=15 and age_student<=17:
    lunch = "burger"
else:
    lunch = "None"
    
print(f"At age {age_student}, the food is {lunch}")

print("\n ----- Example 3: for loop as a counter-----")
# 'for' loop enables the program to execute a code block multiple times.
for n in range(2,10):
    print(n)
    
print("\n ----- Example 4: for loop in a list -----")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)
    
for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")
    
print("\n ----- Example 5: while loop as a counter -----")
count = 1
while count<=5:
    print
    count += 1
    
print("\n ----- Example 6: while loop to validate a number -----")
#validate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
while num<-5 or num>5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))
    
print(f"Entered number = {num} ")