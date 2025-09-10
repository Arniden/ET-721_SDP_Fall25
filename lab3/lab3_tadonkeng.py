"""
Arnaud Tadonkeng
Lab 3, Python conditional Statement and loops
Sep 8, 2025

"""
#Conditional Statement
print("\n ----- Example 1: if, elif,.... else -----")
# guess a number between 1 and 9
GUESS_NUM = 8
#collect the number
user_number = int(input("Guess a number: "))
# compare
if(user_number == GUESS_NUM):
    print(f"Great Job! {user_number} is the guess number.")
elif(user_number > GUESS_NUM):
    print(f"{user_number} should be lower")
elif(user_number < GUESS_NUM):
    print(f"{user_number} should be higher")
else:
    print(f"ERROR!")
    
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
for n in range(3):
    print(n)