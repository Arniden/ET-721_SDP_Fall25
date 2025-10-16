"""
Arnaud Tadonkeng
lab 7, accessing data in a file (function)
Sept 29, 2025
"""

def testing():
    print("FATIMA NADEEM")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line in a file with a Phython code
    with open(filename, "r") as file1:
        filecontent = file1.read()
        print(filecontent)
    # check if the file is closed. If it is closed, it should return True
    print(f"Is the file closed? {file1.closed}")

# EXAMPLE 1: reading specific portion of a file
def read_up(filename):
    with open (filename,"r")as file1:
            #read the first 30 characters
            print(file1.read(30))
            #read the next 5 characters
            print(file1.read(5))
# EXAMPLE 2: Reading specific portion of a file
def read_up (filename):
     with open(filename,"r") as file1:
          #read the first 30 characters
          print(file1.read(30))
          #read the next 5 characters
          print(file1.read(5))

     print(file1.read(5))
# EXAMPLE 3: readline 
def read_readline(filename):
     with open(filename, "r") as file1:
          # read up to 30 characters of the first line
          print(file1.readline(30))
          #continues reading next line up to 5 characters
          print(file1.readlines()) 

# EXAMPLE 4: readline
def read_all(filename):
     with open (filename, "r")as file1:
          print(file1.readlines())

#EXAMPLE 5: loop through a readlines file
def read_each(filename):
     with open (filename, "r")as file1:
          filelines = file1.readlines()

          #loop through each item in 'filelines'
          for eachline in filelines:
            print(eachline.strip())
          #strip()removes the newline character \n

#EXAMPLE 6: create a new file
def new_file(filename):
     with open (filename, "w")as file:
          file.write("Python Basics for data analysis\n")
          file.write("student's full name")

#EXAMPLE 7: append data into an existing file
from datetime import datetime
def stamp_date(filename):
     with open(filename, "a") as file:
         file.write(f"\n\n{datetime.now()}")


# EXERCISE
def email_read(filename):
    """Read the file and return counts for @gmail, @yahoo, and @hotmail addresses.

    Returns a tuple: (gmail_count, yahoo_count, hotmail_count)
    In case of FileNotFoundError, prints an error and returns (0,0,0).
    """
    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0
    try:
        with open(filename, "r") as file1:
            filelines = file1.readlines()

            for eachline in filelines:
                line = eachline.strip()
                # count occurrences using simple substring matching
                if "@gmail" in line:
                    gmail_count += 1
                if "@yahoo" in line:
                    yahoo_count += 1
                if "@hotmail" in line:
                    hotmail_count += 1

        return gmail_count, yahoo_count, hotmail_count

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return 0, 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0, 0