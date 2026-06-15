# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, end = " ")
#     print()
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(j, end = " ")
#     print()

# print * for a 3*3 grid
# for i in range(1, 4):
#     for j in range(1, 4):
#         print("*", end = " ")
#     print()

# 1, 2, 3, ... 10
# 2, 4, 6, ... 20
# .
# .
# .
# 10, 20, 30, ... 100
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end = " ")
#     print()

#* * * *
#* * * *
#* * * *
#* * * *
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end = " ")
#     print()

#*
#* *
#* * *
#* * * *
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()

#1
#2 2
#3 3 3
#4 4 4 4
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(i, end = " ")
#     print()

#1
#1 2
#1 2 3
#1 2 3 4
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

#1
#2 3
#4 5 6
#7 8 9 10
# k = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(k, end = " ")
#         k += 1
#     print()

#1
#4 9
#16 25 36
#49 64 81 100
# k = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(k ** 2, end = " ")
#         k += 1
#     print()

#4 4 4 4
#3 3 3
#2 2
#1
# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print(i, end = " ")
#     print()

#1
#2 1
#3 2 1
#4 3 2 1
# for i in range(1, 5):
#     for j in range(i, 0, -1):
#         print(j, end = " ")
#     print()

#A
#B C
#D E F
#G H I J
# k = 65
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(k), end = " ")
#         k += 1
#     print()

#1
#3 3 3
#5 5 5 5 5
#7 7 7 7 7 7 7
# for i in range(1, 8, 2):
#     for j in range(1, i + 1):
#         print(i, end = " ")
#     print()

#2 2
#4 4 4 4
#6 6 6 6 6 6
#8 8 8 8 8 8 8 8
# for i in range(2, 9, 2):
#     for j in range(1, i + 1):
#         print(i, end = " ")
#     print()

#1
#1 2
#1 2 1
#1 2 1 2
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print('2', end = " ")
#         else:
#             print('1', end = " ")
#     print()

#create a new list which contains only prime numbers
# l = [1, 23, 13, 24, 56, 5]
# k = []
# for i in l:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             k.append(i)
# print(k)

#find the product of two numbers without performing * operation
# n = int(input("Enter the first number: "))
# m = int(input("Enter the second number: "))
# product = 0
# for i in range(1, m + 1):
#     product += n
# print(product)

#A
#A B
#A B C
#A B C D
# for i in range(1, 5):
#     k = 65
#     for j in range(1, i + 1):
#         print(chr(k), end = " ")
#         k += 1
#     print()

#A
#B B
#C C C
#D D D D
# k = 65
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(k), end = " ")
#     k += 1
#     print()

#A
#A B
#A C D
#A E F G
# k = 66
# for i in range(1, 5):
#     print('A', end = " ")
#     for j in range(2,i + 1):
#         print(chr(k), end = " ")
#         k += 1
#     print()

# d = {1:["lion", "tiger", "bear"], 2:["cat", "sheep", "goat"]}
# for i in d.values():
#     for j in i:
#         print(j)

#       *
#     * *
#   * * *
# * * * *
n = 4
k = 3 * 2
for i in range(1, n + 1):
    for p in range(1, k + 1):
        print(end = " ")
    k -= 2
    for j in range(1, i + 1):
        print("*", end = "   ")
    print()

# * * *
#   * *
#     *
k = 2
for i in range(3, 0, -1):
    for p in range(1, k + 1):
        print(end = " ")
    k += 2
    for j in range(1, i + 1):
        print("*", end = "   ")
    print()

#* *
#* *
#* * * *
#* * * *
#* * * * * *
#* * * * * *
#* * * * * * * *
#* * * * * * * *
# for i in range(2, 9, 2):
#     for p in range(2):
#         for j in range(1, i + 1):
#             print("*", end = " ")
#         print()

#       1
#     1 A 1
#   1 A 1 A 1
# 1 A 1 A 1 A 1
# k = 3 * 2
# for i in range(1, 8, 2):
#     for p in range(1, k + 1):
#         print(end = " ")
#     k -= 2
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print('A', end = " ")
#         else:
#             print('1', end = " ")
#     print()

#print the series
#3, 6, 9, 12, 15, ... 30
# for i in range(1, 11):
#     print(3 * i, end = " ")

#print the pattern
#2
#2 2
#2 2 2
#2 2 2 2
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print('2', end = " ")
#     print()

#print the pattern
#p
#p y
#p y t
#p y t h
#p y t h o
#p y t h o n
# s = "python"
# for i in range(1, len(s) + 1):
#     for j in range(1, i + 1):
#         print(s[j - 1], end = " ")
#     print()

#Given a list of fruits
#l = ["orange", "banana", "apple", "pineapple", "avocado"]
#print the first fruit name starting with letter 'a'
# l = ["orange", "banana", "apple", "pineapple", "avocado"]
# for i in l:
#     if i[0] == 'a':
#         print(i)
#         break

#Check whether a number is spy number, means sum of digits equal to the product of digits
#eg: 1124
# n = int(input("Enter the number: "))
# s = str(n)
# sum = 0
# pr = 1
# for i in s:
#     sum += int(i)
#     pr *= int(i)
# if sum == pr:
#     print("The entered number", n, "is a spy number")
# else:
#     print("The entered number", n, "is not a spy number")

#Find the nth element in the Fibonacci series
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# n = int(input("Enter the number: "))
# a = 0
# b = 1
# for i in range(1, n):
#     a, b = b, a + b
# print("The nth element is", a)

#Given a string
#s = "python is a programming language"
#Create a dictionary with keys as each word in the given string and values as its length
# s = "python is a programming language"
# l = s.split()
# d = {}
# for i in l:
#     d[i] = len(i)
# print(d)

#Find the count of vowels in the string
# s = "python is a programming language"
# vowels = "AEIOUaeiou"
# count = 0
# for i in s:
#     if i in vowels:
#         count += 1
# print(count)

#Find the first duplicate element in a list
# l = [1,2,3,4,2,5,3,4]
# k = []
# for i in l:
#     if i in k:
#         print(i)
#         break
#     k.append(i)

#Find all the pairs in a list whose sum is equal to the target number
# Target = 6
# l = [1, 2, 3, 4, 5]
# n = len(l)
# for i in range(0, n):
#     for j in range(i + 1, n):
#         if l[i] + l[j] == Target:
#             print(l[i], l[j])