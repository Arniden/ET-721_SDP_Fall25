"""
Arnaud Tadonkeng
lab 7, accessing data in a file (function)
Sept 29, 2025
"""

from lab7_function import *
testing()
print("\n ---- example 1: reading file -----")
read_data("phrase.txt")

print("\n ---- example #2: Reading specific portion of a file-----")
read_up("phrases.txt")

print("\n --- example 3: reading specific portion using readline----")
read_readline("phrases.txt")

print("\n-----example 4: reading specific portion using readlines----")
read_all("phrases.txt")

print("\n-----example 5: loop through each line ----")
read_each("phrases.txt")

print("\n---- example 6: creating a new file -----")
new_file("last_name.txt")

print("\n---- example 7: append data into an existing file -----")
new_file("last_name.txt")

print("\n ---- EXERCISE -----")
gmail_count, yahoo_count, hotmail_count = email_read("user_email.txt")
with open("reportemail.txt", "w") as report:
    # Write the Gmail count into the file
    report.write(f"gmail = {gmail_count}\n")
    # Write the Yahoo count into the file
    report.write(f"yahoo = {yahoo_count}\n")
    # Write the Hotmail count into the file
    report.write(f"hotmail = {hotmail_count}\n")

print("Report has been generated: 'reportemail.txt'.")