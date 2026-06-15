# # 1, 2, 3, 4, 5, 6
# i = 1
# while i <= 6:
#     print(i, end = " ")
#     i += 1
# print()
# for i in range(1,7):
#     print(i, end = " ")
# print()
#
# #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# i = 1
# while i <= 10:
#     print(i, end = " ")
#     i += 1
# print()
# for i in range(1, 11):
#     print(i, end=" ")
# print()
#
# #1, 3, 5, 7, 9, 11
# i = 1
# while i <= 11:
#     print(i, end = " ")
#     i += 2
# print()
# for i in range(1, 12, 2):
#     print(i, end=" ")
# print()
#
# # 5, 4, 3, 2, 1
# i = 5
# while i >= 1:
#     print(i, end = " ")
#     i -= 1
# print()
# for i in range(5, 0, -1):
#     print(i, end=" ")
# print()
#
# #-8, -6, -4, -2, 0
# i = -8
# while i <= 0:
#     print(i, end = " ")
#     i += 2
# print()
# for i in range(-8, 1, 2):
#     print(i, end=" ")
# print()
#
# # 4, 9, 14, 19, 24, 29, 34, 39
# i = 4
# while i <= 39:
#     print(i, end = " ")
#     i += 5
# print()
# for i in range(4, 40, 5):
#     print(i, end=" ")
# print()
#
# # 3, 6, 12, 24, 48, 96
# i = 3
# while i <= 96:
#     print(i, end = " ")
#     i *= 2
# print()
# j = 3
# for i in range(1, 7):
#     print(j, end=" ")
#     j *= 2
# print()
#
# # 1, 4, 9, 16, 25, 36, 49
# i = 1
# while i <= 7:
#     print(i**2, end = " ")
#     i += 1
# print()
# for i in range(1, 8):
#     print(i**2, end = " ")
# print()

#
# #10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# i = 10
# while i <= 100:
#     print(i, end = " ")
#     i += 10
# print()
# for i in range(1, 11):
#     print(i*10, end = " ")
# print()
#
# #1, 2, 4, 7, 11, 16, 22
# i = 1
# j = 1
# while i <= 22:
#     print(i, end = " ")
#     i += j
#     j += 1
# print()
# j = 1
# for i in range(1, 8):
#     print(j, end = " ")
#     j += i
# print()
#
# #Count all even numbers in the range 1 - 100
# count = 0
# i = 2
# while i <= 100:
#     print(i, end = " ")
#     count += 1
#     i += 2
# print()
# print(count)
# count = 0
# for i in range(2, 101, 2):
#     print(i, end = " ")
#     count += 1
# print()
# print(count)
#
# #Print those numbers that are divisible by 7 and 3 in the range 100-400
# i = 100
# while i <= 400:
#     if i % 3 == 0 and i % 7 == 0:
#         print(i, end = " ")
#     i += 1
# print()
# for i in range(100, 401):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i, end = " ")
# print()
#
# #Count of all 4-digit numbers that are divisible by 5
# count = 0
# i = 1000
# while i <= 9999:
#     if i % 5 == 0:
#         print(i, end = " ")
#         count += 1
#     i += 1
# print()
# print(count)
# count = 0
# for i in range(1000, 10000):
#     if i % 5 == 0:
#         print(i, end = " ")
#         count += 1
# print()
# print(count)
#
# # Sum of 1,2,3,4,5
# i = 1
# s = 0
# while i <= 5:
#     s += i
#     i += 1
# print("The sum is", s)
# s = 0
# for i in range(1, 6):
#     s += i
# print("The sum is", s)
#
# #Product of 1,2,3,4,5
# i = 1
# p = 1
# while i <= 5:
#     p *= i
#     i += 1
# print("The product is", p)
# p = 1
# for i in range(1, 6):
#     p *= i
# print("The product is", p)
#
# #Find the sum, count, product of two-digit numbers that are divisible by 3 and 5
# s = 0
# c = 0
# p = 1
# i = 10
# while i <= 99:
#     if i % 3 == 0 and i % 5 == 0:
#         s += i
#         c += 1
#         p *= i
#     i += 1
# print("The sum, count and product are", s, c, p, "respectively")
# s = 0
# c = 0
# p = 1
# for i in range(10, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         s += i
#         c += 1
#         p *= i
# print("The sum is", s, "The count is", c, "The product is", p)

#Factorial of a number
# n = int(input("Enter a number: "))
# fact = 1
# while n >= 1:
#     fact *= n
#     n -= 1
# print(fact)
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

#Print the multiplication table of a number till 10
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n*i)
#     i += 1
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "*", i, "=", n * i)

#Print the series 1, 9, 25, 49, 81, 121
# i = 1
# while i <= 11:
#     print(i**2, end = " ")
#     i += 2
# print()
# for i in range(1, 12, 2):
#     print(i**2, end = " ")
# print()

#Print the letters of a string
# s = input("Enter the string: ")
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
# s = input("Enter the string: ")
# for i in s:
#     print(i)

#Count the vowels in a string
# s = input("Enter the string: ")
# vowels = "AEIOUaeiou"
# count = 0
# i = 0
# while i < len(s):
#     if s[i] in vowels:
#         count += 1
#     i += 1
# print("The number of vowels is", count)
s = input("Enter the string: ")
vowels = "AEIOUaeiou"
count = 0
for i in s:
    if i in vowels:
        count += 1
print("The number of vowels is", count)