# 1. Create a multiplication table for a number. Stop printing once the result exceeds 50.

# n = int(input("Enter the number: "))
# i = 1
# while n * i <= 50:
#     print(n, "*", i, "=", n * i)
#     i += 1

# 2. Define a function to check whether a number is perfect number or not. hint: A perfect number is a positive
# integer that is equal to the sum of its positive proper divisors, excluding the number itself. For example, the number
# 6 has divisors 1, 2 and 3 and 1 + 2 + 3 = 6, making it a perfect number. the first few perfect numbers are 6, 28, 496
# and 8128

n = int(input("Enter the number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

# 3. Loop through a list of numbers. Break when you find a number that is a multiple of both 4 and 6.
# nums = [5, 9, 12, 18, 24, 30]
# nums = [5, 9, 12, 18, 24, 30]
# for i in nums:
#     if i % 4 == 0 and i % 6 == 0:
#         break
#     print(i)

# 4. Print the fibonacci series(count:10)
# a = 0
# b = 1
# for i in range(1, 11):
#     print(a, end = " ")
#     a, b = b, a + b

# 5. Write a python program that takes a sentence and returns a dictionary where:
# Keys are words in the sentence.
# Values are dictionaries with:
# "length" -> Length of the word
# "is_palindrome" -> True if the word is palindrome, otherwise false
# "count" -> no. of occurrences of the word
# Sample Input:
# Sentence = "madam and racecar are level racecar madam"
# Sample Output:
# {"madam": {"length":5, "is_palindrome":True, "count":2},
# "and":{"length":3,"is_palindrome":False, "count":1},
# "racecar:{"length":7, "is_palindrome":True,"count":2},
# "are":{"length":3, "is_palindrome":False, "count":1},
# "level":{"length":5, "is_palindrome":True, "count":1}}

# def create_dictionary(k):
#     for i in k:
#         if i not in d:
#             length = len(i)
#             is_palindrome = False
#             if i == i[::-1]:
#                 is_palindrome = True
#             c = k.count(i)
#             d[i] = {"length": length, "is_palindrome": is_palindrome, "count": c}
#     for i in d.items():
#         print(i)
#
# d = {}
# sentence = input("Enter the sentence: ")
# l = sentence.split()
# create_dictionary(l)

# 6. Given a s = "Python makes coding fun & easy"
# Print each character in the string upto a specific
# character including that character.
# s = "Python makes coding fun & easy"
# c = input("Enter the character: ")
# for i in s:
#     print(i, end = " ")
#     if i == c:
#         break

# 7. Check whether a number is an Armstrong or not.
# n = int(input("Enter the number: "))
# s = str(n)
# res = 0
# l = len(s)
# for i in s:
#     res += int(i) ** l
# if res == n:
#     print("The number", n, "is an Armstrong number")
# else:
#     print("The number", n, "is not an Armstrong number")

# 8. Write a menu driven code (using function)
# 1. Add Recipe details
# (recipename, description, ingredients, cuisine, meal_type)
# 2. Show all recipes
# 3. Delete a recipe

# def add_recipe():
#     r = input("recipe name: ")
#     if r in recipes:
#         print("Recipe already present!")
#         return
#     d = input("description: ")
#     i = input("ingredients: ")
#     c = input("cuisine: ")
#     m = input("meal_type: ")
#     recipes[r] = {"description":d, "ingredients":i, "cuisine": c, "meal_type":m}
#     return
#
# def show_all():
#     for i in recipes.items():
#         print(i)
#     return
#
# def delete_recipe():
#     r = input("Enter the recipe name: ")
#     if r in recipes:
#         recipes.pop(r)
#         print("Recipe deleted successfully!")
#     else:
#         print("Recipe not found!")
#
# recipes = {}
# while 1:
#     print("1. Add recipe details")
#     print("2. Show all recipes")
#     print("3. Delete a recipe")
#     print("4. Exit")
#     ch = int(input("Enter the choice: "))
#     if ch == 1:
#         add_recipe()
#     elif ch == 2:
#         show_all()
#     elif ch == 3:
#         delete_recipe()
#     elif ch == 4:
#         exit()
#     else:
#         pass

# 9. Print the pattern
#       1
#     1   2
#   1   2   3
# 1   2   3   4
#   1   2   3
#     1   2
#       1

# n = 4
# k = 3 * 2
# for i in range(1, n + 1):
#     for p in range(1, k + 1):
#         print(end=" ")
#     k -= 2
#     for j in range(1, i + 1):
#         print(j, end = "   ")
#     print()
# k = 2
# for i in range(n - 1, 0, -1):
#     for p in range(1, k + 1):
#         print(end=" ")
#     k += 2
#     for j in range(1, i + 1):
#         print(j, end="   ")
#     print()

# 10. What are the advantages of sets in python?
# A set is an unordered collection of elements. There is no duplicate element in a set. It starts and ends with curly
# brackets '{' and '}'. It is a mutable data type. A set can be modified or updated. The following operations can be
# performed on a set: union, intersection, difference and symmetric intersection.

# 11. Difference between list and tuple.
# A list is a heterogeneous collection of elements. It starts and ends with square brackets '[' and ']'.
# A tuple starts and ends with parentheses '(' and ')'
# A list is a mutable data type. It can be modified or updated.
# A tuple is an immutable data type. It cannot be modified or updated.

# 12. What is a decorator function? Write with example.
# A decorator function is a function which changes the behaviour of an existing function without changing its code/
# definition. Example:
# def smart_sub(func):
#     def wrapper(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return wrapper
#
# @smart_sub
# def sub(x, y):
#     diff = x - y
#     print(diff)
#     return
#
# sub(5, 3)
# sub(3, 5)

# 13. What is comprehension? Write with example.
# A comprehension is a simple and easy syntax used to create a new sequence from an existing sequence.
# Its syntax is:
# new = [output/expression for item in iterable if condition]
# Example: To create a list of squares of even numbers from the list [1, 2, 3, 4], we write
# l = [1, 2, 3, 4]
# new_l = [i**2 for i in l if i % 2 == 0]
# print(new_l)

# 14. What are functions? Explain different types of functions with example.
# A function is a block statement used to perform a task or operation.
# It has the following syntax:
# def function_name(parameters):
#   function_body
#   return expression/value
# function_name(arguments)
# parameters - the variables listed in the function definition
# arguments - the values/variables passed to a function when it is called
# return - to terminate from the execution process or optionally it sends the result back to the caller part.
# Different types of functions are:
# a) Built-in functions - These are pre-defined functions already present in python. Examples: input(), print(), len(),
# count().
# b) User-defined functions - These are defined using the def keyword. Examples:
# def add(a, b):
#     return a + b
# c) Lambda functions - They are called anonymous functions or nameless functions. It starts with the keyword lambda.
# It's an inline function. Its syntax is:
# lambda arguments: expression
# A lambda function can take n number of arguments and it has a single expression.
# It's mainly used in higher order functions. Higher order functions take another function as argument. They include:
# 1) Map
# 2) Filter
# 3) Reduce
# Example of lambda function:
# l = [1, 2, 3, 4]
# new_l = list(map(lambda x: x**2, l))
# print(new_l)

# 15. What are modules and packages?
# A module is a python file containing variables, functions and classes.
# A package is a directory/folder containing multiple python files and an __init__.py file.

# 16. Why use import statements?
# Import statements are used to include the variables, functions/classes from another file to our file.

# 17. What are access modifiers? With examples.
# Global - The variables declared in the main part of the program or outside the function.
# a = 10
# b = 20
# c = a + b
# Local - The variable declared inside the function.
# def add(a, b):
#     c = a + b
#     return c
# Enclosing - The scope of the variables declared in an enclosing function.
# def outer():
#     x = 10
#     print(x)
#     def inner():
#         print(x)
#         return
#     inner()
#     return
# outer()
# Built-in - The scope of the variables declared in a built-in function.

# 18. Explain feature of python
# 1) It's a high-level programming language
# 2) It's a machine-independent language
# 3) It has a user-friendly syntax. Indentation is used to differentiate different parts of the program.
# 4) It is a general-purpose language. It is used for many purposes like game development, networking field, data science,
# software testing, web applications, AI and machine learning.
# 5) It is an interpreted language - It has line by line execution. The interpreter converts the high level language
# to byte code.
# 6) It's a portable language. The same code can be run in any operating system(e.g., Ubuntu, Windows, Mac) with the same result.
# 7) It's a dynamic type language. We don't have to declare the data type of the variable explicitly. Durint the runtime
# with the help of the interpreter it detects the data type of the variable according to the value assigned to the variable.
# 8) It's a multi-programming paradigm-supporting language. It supports both function oriented programming and object-
# oriented programming.
# 9) It's an open source language. It is free of cost.
# 10) It's a large community supported language. It was invented by Guido van Rossum, a Dutch programmer. It has experts
# with over 30 years of experience. Documentation is available which helps us to resolve small error or complex error.
# The current version is 3.14.3.
# 11) It has a large library support. Examples of libraries include NumPy, Pandas and Pillow.

# 19. What are different types of functional arguments
# Different types of functional arguments are
# 1) Positional arguments: The arguments passed to a function in the exact order in which they are declared in the
# function
# 2) Keyword arguments: The arguments that are passed to a function by using the parameter name. Here, order does not
# matter
# 3) Default arguments: During the function definition, a default value is given along with the parameter. Even if
# no argument is passed the default value is used.
# 4) Arbitrary arguments: Also known as variable length arguments. It allows us to pass multiple number of arguments.
# There are two types of arbitrary arguments:
# a) Arbitrary non-keyword arguments: represented by *args. It is a tuple sequence.
# b) Arbitrary keyword arguments: represented by **kwargs. It is a dictionary sequence.


# 20. What is the use of OS module in python?
# The OS module in python is used to remove a file. The remove function is invoked by os.remove(file_name).