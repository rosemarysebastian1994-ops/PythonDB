#Program to check whether the number is divisible by 7 or not
# n = int(input("Enter the number: "))
# if n%7 == 0:
#     print("The entered number", n, "is divisible by 7")
# else:
#     print("The entered number", n, "is not divisible by 7")

#Program to check whether the number is a multiple of 3 and 5
# n = int(input("Enter the number: "))
# if n%3 == 0 and n%5 == 0:
#     print("The entered number", n, "is a multiple of 3 and 5.")
# else:
#     print("The entered number", n, "is not a multiple of 3 and 5.")

#Write a program to find the maximum of two numbers
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# if n1>n2:
#     print(n1,"is greater")
# else:
#     print(n2,"is greater")

#Write a program to check whether the entered number is a 2-digit/3-digit/4-digit number
# n = int(input("Enter a number: "))
# if 10<=n<=99:
#     print("The entered number", n, "is a 2-digit number")
# elif 100<=n<=999:
#     print("The entered number", n, "is a 3-digit number")
# elif 1000<=n<=9999:
#     print("The entered number", n, "is a 4-digit number")
# else:
#     print("The entered number", n, "is neither 2/3/4 digit number")

#Write a basic calculator program to perform arithmetic operations(+, -, *, /)
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# op = input("Enter the choice (+. -, *, /):")
# if op == '+':
#     print("The sum is", n1 + n2)
# elif op == '-':
#     print("The difference is", n1 - n2)
# elif op == '*':
#     print("The product is", n1 * n2)
# elif op == '/':
#     print("The quotient is", n1 / n2)
# else:
#     print("Invalid operation")

#Write a program to print the number of days in a month
l1 = ["january", "march", "may", "july", "august", "october", "december"]
l2 = ["april", "june", "september", "november"]
l3 = ["february"]
s = input("Enter the month: ")
if s in l1:
    print("31 days")
elif s in l2:
    print("30 days")
elif s in l3:
    print("28 or 29 days")
else:
    print("Invalid month name")