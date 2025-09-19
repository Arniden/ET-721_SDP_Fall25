"""
Arnaud Tadonkeng
Sep 17, 2025
Lab 6: object and classes
"""
print("\n ------- Example 1: create a class -------")
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        

    #method
    def add_radius(self, r):
        self.radius += r
        return self.radius
        
class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        
    # method to calculate the area
    def area(self):
        return self.width * self.height
    
    #method to calculate the perimeter
    def perimeter(self):
        # perimeter = 2 * (width + height)
        return 2 * (self.width + self.height)
# Creating an instance of the class, which is an object
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2, 5, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

#accessing the information in an object
print(f"The color of circle2 = {circle2.color}")

print(f"The width of rectangle1 = {rectangle1.width}")

#update data in an object
#change circle1 color from 'red to 'yellow'
print(f"The color of circle1 before update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle1 after update = {circle1.color}")

# accessing a method
print(f"Radius of circle2 = {circle2.radius}")
# update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# accessing methods in rectangle
print(f"The area of the rectangle1 with width = {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"The perimeter of the rectangle2 = {rectangle2.perimeter()}")

print("\n ------- EXERCISE -------")


class BankAccount:
    """A simple bank account class.

    Properties:
    - account_number: int
    - account_holder: str
    - balance: float (starts at 0.0)
    """
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds: cannot withdraw {amount:.2f}. Current balance: {self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")


# Creating an instance of the BankAccount class
useraccount = BankAccount(123456789, "Student's name")

# Demonstrating deposits and withdrawals per prompt
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

# prompt result
print(f"Final balance {useraccount .balance}")