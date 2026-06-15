# n = int(input("Enter the number:"))
# if n>0:
#     if n%2 == 0:
#         print("The entered number is a positive multiple of 2")
#     else:
#         print("The entered number is positive but not divisible by 2")
# else:
#     if n%2 == 0:
#         print("The entered number is negative and divisible by 2")
#     else:
#         print("The entered number is negative and not divisible by 2")

# n = int(input("Enter a number: "))
# if n%2 == 0:
#     if n%3 == 0:
#         print("The entered number is divisible by 2 and 3")
#     else:
#         print("The entered number is divisible by 2 but not 3")
# else:
#     if n%3 == 0:
#         print("The entered number is divisible by 3 but not 2")
#     else:
#         print("The entered number is not divisible by 2 and 3")


# a toy vendor supplies three types of toys. Battery based toys, key based toys and electrical charging based toys.
# The vendor gives a discount of 10% for battery based toys if the order is for more than Rs. 1000. On orders of more
# than  Rs. 100 for key based toys, a discount of 5% is given and a discount of 10% is given on orders for electrical charging
#     toys of value more than Rs. 500.
# Assume that the numeric codes 1, 2 and 3 are used for battery, key and electrical charging based toys respectively.
#     Write a program that reads the product code and the order amount and prints out the net amount that the customer
# is required to pay after the discount.
n = int(input("Enter the product code: "))
amount = int(input("Enter the order amount: "))
if n == 1:
    if amount > 1000:
        dis = amount*10/100
        actual_amount = amount - dis
        print("The actual amount is ", actual_amount)
    else:
        print("The actual amount is ", amount)
elif n == 2:
    if amount > 100:
        dis = amount*5/100
        actual_amount = amount - dis
        print("The actual amount is ", actual_amount)
    else:
        print("The actual amount is ", amount)
elif n == 3:
    if amount > 500:
        dis = amount * 10 / 100
        actual_amount = amount - dis
        print("The actual amount is ", actual_amount)
    else:
        print("The actual amount is ", amount)
else:
    print("Invalid product code")
