'''
Arnaud Tadonkeng
Oct 15, 2025
Lab #10: File Operation Test
'''
def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)

def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()

def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")

# function from exercise lab 7 (yesterday)
"""
Create a function, named email_read(),
that reads a txt file and returns the number of users that have&nbsp;@gmail,
@yahoo, and @hotmail email address, The function should have&nbsp; try-exception&nbsp;statement.
You can test the function using the file&nbsp;user email.txt file.
"""
def email_read(filename, report):
    try:
        count_yahoo = 0
        count_gmail = 0
        count_hotmail = 0

        with open(filename, "r") as file1:
            for eachline in file1:
                email = eachline.lower().strip()

                if "@yahoo.com" in email:
                    count_yahoo += 1

                elif "gmail.com" in email:
                    count_gmail += 1 

                elif "hotmail.com" in email:
                    count_hotmail += 1

        with open(report, "w") as file:
            file.write(f"yahoo = {count_yahoo}\n")
            file.write(f"gmail = {count_gmail}\n")
            file.write(f"hotmail = {count_hotmail}\n")
    
    except FileNotFoundError:
        print("'user_email.txt' was not found")