# x = int(input("Enter the number: "))
# print(x)

# try:
#     n1 = int(input("Enter the number: "))
#     n2 = int(input("Enter the number: "))
#     result = n1/n2
#     print(result)
# except ValueError as e1:
#     print(e1)
# except ZeroDivisionError as e2:
#     print(e2)
# else:
#     pass

# try:
#     f = open("l.txt", "r")
#     s = f.read()
#     print(s)
# except FileNotFoundError as e1:
#     print(e1)
# else:
#     pass

# while 1:
#     try:
#         import math
#         n = int(input("Enter the number: "))
#         result = math.factorial(n)
#         print(result)
#     except ValueError as e1:
#         print(e1)
#     except:
#         print("Error occurs")
#     else:
#         break

# def fact():
#     try:
#         import math
#         n = int(input("Enter the number: "))
#         result = math.factorial(n)
#         print(result)
#     except:
#         print("Error occurs")
#         fact() # recursive function
#     else:
#         pass
# fact()

age = int(input("Enter the age: "))
if age < 18:
    raise ValueError("age should be greater than 18")
