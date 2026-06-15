#Print only the vowels in the string
# s = input("Enter the string: ")
# k = ""
# vowels = "AEIOUaeiou"
# for i in s:
#     if i in vowels:
#         k += i
# print(k)

#Print the colours starting with letter 'b'
# l = ["red", "green", "blue", "white", "black"]
# k = []
# for i in l:
#     if i[0] == 'b':
#         k.append(i)
# print(k)

#Print each word in a string
# s = "python is a programming language"
# l = s.split()
# print(l)

#Print all even values in the list
# l = [12, 13, 15, 16, 19, 20]
# for i in l:
#     if i % 2 == 0:
#         print(i)

#L=["arun", 23, "ekm", 40000] print only the string values
# L = ["arun", 23, "ekm", 40000]
# for i in L:
#     if type(i) == str:
#         print(i)

#L=[1,3,5,7,9,11] print the square of each element
# L=[1,3,5,7,9,11]
# k = []
# for i in L:
#     k.append(i**2)
# print(k)

#L=["apple", "orange", "pineapple", "apricot", "pomegranate"] create a new list with all fruit names whose length is
#greater than 6
# L=["apple", "orange", "pineapple", "apricot", "pomegranate"]
# k = []
# for i in L:
#     if len(i) > 6:
#         k.append(i)
# print(k)

#L=[123,789,567,453, 908, 321] create a new list with numbers which contain the number '3'
# L=[123,789,567,453, 908, 321]
# k = []
# for i in L:
#     if '3' in str(i):
#         k.append(i)
# print(k)

#Palindrome
# s = input("Enter the string: ")
# rev = ""
# for i in s:
#     rev = i + rev
# if rev == s:
#     print("Palindrome")
# else:
#     print("Not palindrome")

#l = [23, 56, 89, 31] Create a new list that contains numbers that are greater than 50
# l = [23, 56, 89, 31]
# k = []
# for i in l:
#     if i > 50:
#         k.append(i)
# print(k)

#l = ["red", "green", "yellow", "blue", "black"] Print a new list with reverse value of each colour
# l = ["red", "green", "yellow", "blue", "black"]
# k = []
# for i in l:
#     k.append(i[::-1])
# print(k)

#sum of list
# l = [1, 2, 3, 4, 5]
# s = 0
# for i in l:
#     s += i
# print(s)

#sum of dictionary
# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# s = 0
# for i in d.values():
#     s += i
# print(s)

#Factorial of a number
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print("The factorial is", fact)

#Factors of a number
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

#d = {101:["amal", 23, "ekm"], 102:["arun", 25, "tvm"], 103:["anu", 27, "ekm"], 104:["kiran", 30, "tcr"]}
#Print all the names from the given data. Print the average age of all students. Print the details of students whose
#place is "ekm"
# d = {101:["amal", 23, "ekm"], 102:["arun", 25, "tvm"], 103:["anu", 27, "ekm"], 104:["kiran", 30, "tcr"]}
# for i in d.values():
#     print(i[0])
# s = 0
# for i in d.values():
#     s += i[1]
# print("The average is", s/len(d))
# for i in d.values():
#     if i[2] == "ekm":
#         print(i)

#Print the string up to a specific character including that character
# s = "Python is a programming language"
# for i in s:
#     print(i)
#     if i == 'a':
#         break

#l = ["red", "green", "yellow", "blue", "black"] print the first occurrence of color value starting with "b"
# l = ["red", "green", "yellow", "blue", "black"]
# for i in l:
#     if i[0] == 'b':
#         print(i)
#         break

#Skip the even values and print the odd values
# l = [23, 45, 64, 31, 22]
# for i in l:
#     if i % 2 == 0:
#         continue
#     print(i)

#Print those numbers that are not divisible by 3 in the range (100-300)
# for i in range(100, 301):
#     if i % 3 == 0:
#         continue
#     print(i)

#To check a number is prime or not
# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not prime number")

#To check a number is Armstrong number or not
# n = int(input("Enter the number: "))
# sum = 0
# s = str(n)
# l = len(s)
# for i in s:
#     sum = sum + int(i)**l
# if(sum == n):
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")