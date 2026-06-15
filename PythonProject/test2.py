#Write a program to print all the numbers between 1 and 100 that are divisible by 3 or 5 but not both
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         if not(i % 3 == 0 and i % 5 == 0):
#             print(i)

# Take string input from the user and print the reverse using for loop without using slice operator
# s = input("Enter the string: ")
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)

#Given a number n write a program that uses for loop to compute the sum of its digits. example: n = 1, 2, 3, 4
# sum = 10
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

#Print the cumulative sum of a list
#Example list l = [1,2,3,4] output [1,3,6,10]
# l = [1, 2, 3, 4]
# k = []
# cum = 0
# for i in l:
#     cum += i
#     k.append(cum)
# print(k)

#Given two numbers a and b. Calculate the sum of all numbers between them using a for loop.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# sum = 0
# for i in range(a, b + 1):
#     sum += i
# print("The sum is", sum)

#Given a list sum only elements at even indexes. Example l = [10, 20, 30, 40, 50] sum = 90
# l = [10, 20, 30, 40, 50]
# i = 0
# sum = 0
# while i < len(l):
#     if i % 2 == 0:
#         sum += l[i]
#     i += 1
# print("The sum is", sum)

#Given a list sum the elements until a 0 is encountered. example l = [1, 3, 5, 0, 8, 10] sum = 9
# l = [1, 3, 5, 0, 8, 10]
# sum = 0
# for i in l:
#     if i == 0:
#         break
#     sum += i
# print("The sum is", sum)

#Loop from 1 to 100 and find the first number divisible by both 7 and 11. Use a break to stop once found.
# for i in range(1, 101):
#     if i % 7 == 0 and i % 11 == 0:
#         print(i)
#         break

#Given a list of strings. Print only those with length greater than or equal to 5. Use continue to skip shorter ones.
# l = ["apple", "orange", "kiwi", "grapes"]
# k = []
# for i in l:
#     if len(i) < 5:
#         continue
#     k.append(i)
# print(k)

#Loop from 1 to 30 and print all numbers except those divisible by 4. use continue.
# for i in range(1, 31):
#     if i % 4 == 0:
#         continue
#     print(i)

#From a list of numbers create a new list containing the square of each element. example: [1,2,3] output[1,4,9]
l = [1, 2, 3]
k = []
for i in l:
    k.append(i**2)
print(k)

#ismathilyas786@gmail.com