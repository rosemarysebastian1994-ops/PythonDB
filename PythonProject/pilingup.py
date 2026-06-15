# from collections import deque
#
# t = int(input())
# for i in range(0, t):
#     n = int(input())
#     sideLength = deque()
#     s = input()
#     l = s.split()
#     for j in l:
#         sideLength.append(float(j))
#     result = []
#     possible = True
#     for j in range(0, n):
#         if j < n - 1:
#             a = sideLength.popleft()
#             b = sideLength.pop()
#             if a > b:
#                 sideLength.append(b)
#                 r = a
#             else:
#                 sideLength.appendleft(a)
#                 r = b
#             if result == []:
#                 result.append(r)
#             else:
#                 if result[-1] < r:
#                     possible = False
#                     break
#                 else:
#                     result.append(r)
#         else:
#             a = sideLength.popleft()
#             if result == []:
#                 result.append(a)
#             else:
#                 if result[-1] < a:
#                     possible = False
#                     break
#                 else:
#                     result.append(a)
#     if possible:
#         print("Yes")
#     else:
#         print("No")

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
#
# # Complete the solve function below.
# def solve(s):
#     count = 0
#     t = ""
#     for i in s:
#         j = ""
#         if i == " ":
#             count = 0
#             j = i
#         elif count == 0:
#             j = i.capitalize()
#             count = 1
#         else:
#             j = i
#         t += j
#     return t
#
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     # fptr.write(result + '\n')
#
#     # fptr.close()
#     print(result)

def print_rangoli(size):
    # your code goes here
    k = (size - 1)* 2
    for i in range(1, size + 1):
        c = 97 + size - 1
        for p in range(1, k + 1):
            print("-", end="")
        for j in range(1, i + 1):
            print(chr(c), "-", end="", sep = "")
            c -= 1
        middle = False
        if c + 1 == 97:
            middle = True
        c += 2
        while c < 97 + size:
            if middle and c == 97 + size - 1:
                print(chr(c), end="", sep="")
            else:
                print(chr(c), "-", end="", sep="")
            c += 1
        for p in range(1, k):
            print("-", end = "")
        k -= 2
        print()
    k = 2
    for i in range(size, 1, -1):
        c = 97 + size - 1
        for p in range(1, k + 1):
            print("-", end="")
        for j in range(1, i):
            print(chr(c), "-", end="", sep = "")
            c -= 1
        middle = False
        if c + 1 == 97:
            middle = True
        c += 2
        while c < 97 + size:
            if middle and c == 97 + size - 1:
                print(chr(c), end="", sep="")
            else:
                print(chr(c), "-", end="", sep="")
            c += 1
        for p in range(1, k):
            print("-", end = "")
        k += 2
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)