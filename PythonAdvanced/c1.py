# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#     def show_details(self):
#         print(self.name, self.age)
#
# p1 = Person("amal", 24)
# p1.show_details()
# p2 = Person("anu", 30)
# p2.show_details()

# class Person:
#     def __init__(self):
#         self.name = input("Enter the name: ")
#         self.age = int(input("Enter the age: "))
#     def show_details(self):
#         print(self.name, self.age)
#
# p1 = Person()
# p1.show_details()

# define class name Employee with attributes - emp_id, name, designation, place, salary
# and method to show_details()
# class Employee:
#     def __init__(self):
#         self.emp_id = int(input("Enter the emp_id: "))
#         self.name = input("Enter the name: ")
#         self.designation = input("Enter the designation: ")
#         self.place = input("Enter the location: ")
#         self.salary = int(input("Enter the salary: "))
#     def show_details(self):
#         print("The emp_id is", self.emp_id, "the name is", self.name,
#               "the designation is", self.designation, "the location is", self.place,
#               "the salary is", self.salary)
#
# e1 = Employee()
# e1.show_details()

# define a class name Book with attributes book_no, title, author, price
# and methods show_title(), show_author(), show_price(), set_title(), set_author(), set_price()
# class Book:
#     def __init__(self):
#         self.book_no = int(input("Enter the book no.: "))
#         self.title = input("Enter the title: ")
#         self.author = input("Enter the author: ")
#         self.price = int(input("Enter the price: "))
#     def show_title(self):
#         print("The title is", self.title)
#     def show_author(self):
#         print("The author is", self.author)
#     def show_price(self):
#         print("The price is", self.price)
#     def set_title(self):
#         self.title = input("Enter the title: ")
#         self.show_title()
#     def set_author(self):
#         self.author = input("Enter the author: ")
#         self.show_author()
#     def set_price(self):
#         self.price = int(input("Enter the price: "))
#         self.show_price()
# b1 = Book()
# b1.show_title()
# b1.show_author()
# b1.show_price()
# b1.set_title()
# b1.set_author()
# b1.set_price()

# Define a class named circle with attributes radius and methods getarea() and getperimeter()
# Create two objects c1 and c2 and print area and perimeter of each circle object.
# class Circle:
#     def __init__(self):
#         self.radius = int(input("Enter the radius: "))
#     def getarea(self):
#         return 3.14 * (self.radius ** 2)
#     def getperimeter(self):
#         return 2 * 3.14 * self.radius
# c1 = Circle()
# print("The area is", c1.getarea())
# print("The perimeter is", c1.getperimeter())
# c2 = Circle()
# print("The area is", c2.getarea())
# print("The perimeter is", c2.getperimeter())

# Define a class named Account with attributes account_number, account_name, balance and methods
# withdraw(), deposit(), show_balance(). Create the account object and call each method.
# class Account:
#     def __init__(self):
#         self.no=int(input("enter the account number:"))
#         self.acct_name=input("enter the name:")
#         self.balance=int(input("enter the balance:"))
#     def withdraw(self):
#         self.amount=int(input("enter the amount:"))
#         self.balance-=self.amount
#     def deposit(self):
#         self.amount=int(input("enter the amount:"))
#         self.balance+=self.amount
#     def show_balance(self):
#         print("the current balance is:",self.balance)
# a=Account()
# a.withdraw()
# a.deposit()
# a.show_balance()
