# add = lambda a, b: a + b
# print(add(5, 3))
#
# square = lambda a: a ** 2
# print(square(5))
#
# max_value = lambda a, b: a if a > b else b
# print(max_value(10, 20))
#
# students = [("Alice", 25), ("Bob", 22), ("Charlie", 30)]
# sorted_students = sorted(students, key= lambda student:student[1])
# print(sorted_students)
#
# numbers = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, numbers))
# tripled = list(map(lambda x: x * 3, numbers))
# print(doubled)
# print(tripled)
#
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# def func(n):
#     return lambda a: a * n
# mydoubler = func(2)
# mytripler = func(3)
# print(mydoubler(11))
# print(mytripler(11))

# fruits = ["apple", "banana", "kiwi", "orange", "cherry"]
# sorted_fruits = sorted(fruits, key=lambda x:len(x))
# print(sorted_fruits)

#Create a list of names
# d=[{"name":"arun", "age":23},{"name":"amal","age":25},{"name":"anu", "age":30}]
# print(list(map(lambda x:x["name"], d)))

#Create a list of authors
# l=[["book1", "john", 300], ["book2", "sam", 350], ["book3", "mike", 200]]
# print(list(map(lambda x:x[1], l)))

#Create a list of length
# s=["red", "green", "blue", "orange", "yellow", "violet"]
# print(list(map(lambda x:len(x), s)))

#Create a list of square roots
# k = [16, 25, 81, 100, 4]
# print(list(map(lambda x:x**0.5, k)))

# Filter the even numbers
# y = [1, 2, 3, 4, 5, 6, 78]
# print(list(filter(lambda x:x%2==0, y)))

# Filter the odd numbers
# y = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list(filter(lambda x:x%2==1, y)))

# Filter the positive numbers
# y = [-5, 67, -23, 10, 27, -81]
# print(list(filter(lambda x:x > 0, y)))

# Filter the negative numbers
# y = [-5, 67, -23, 10, 27, -81]
# print(list(filter(lambda x:x<0, y)))

# Given a sequence
# l = ["apple", "orange", "pineapple", "avocado"]
# Filter the elements whose length is greater than 5
# print(list(filter(lambda x:len(x)>5, l)))

# y = [1, 2, 3, 4, 5, 6, 78]
# import functools
# print(functools.reduce(lambda a,b:a+b, y))

#Given a sequence
m = [-12, 9, 56, 11, -7, -3, -1, 90, 45, 22, -16]
# Sum of positive odd numbers
x = list(filter(lambda x:x>0 and x%2!=0, m))
print(x)
import functools
print(functools.reduce(lambda a, b: a + b, x))

# Sum of negative odd numbers
y = list(filter(lambda x:x < 0 and x % 2 != 0, m))
print(y)
print(functools.reduce(lambda a, b: a + b, y))

# Sum of positive even numbers
z = list(filter(lambda x:x>0 and x%2==0, m))
print(z)
print(functools.reduce(lambda a, b: a + b, z))

# Sum of negative even numbers
w = list(filter(lambda x:x < 0 and x % 2 == 0, m))
print(w)
print(functools.reduce(lambda a, b: a + b, w))

# Count of positive numbers
f = list(filter(lambda x: x > 0, m))
print("The count of positive numbers is", len(f))

# Count of negative numbers
g = list(filter(lambda x: x < 0, m))
print("The count of negative numbers is", len(g))