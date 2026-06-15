# k = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(k ** 2, end=" ")
#         k += 1
#     print()

# n = 4
# k = 3 * 2
# for i in range(1, n + 1):
#     for p in range(1, k + 1):
#         print(end = " ")
#     k -= 2
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()

# n = 3
# k = 0
# for i in range(n, 0, -1):
#     for p in range(1, k + 1):
#         print(end = " ")
#     k += 2
#     for j in range(1, i + 1):
#         print("*", end = " ")
#     print()

# n = 8
# for i in range(2, n + 1, 2):
#     for j in range(2):
#         for k in range(1, i + 1):
#             print("*", end = " ")
#         print()

# n = 7
# k = 3 * 2
# for i in range(1, n + 1, 2):
#     for p in range(1, k + 1):
#         print(end=" ")
#     k -= 2
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print('A', end=" ")
#         else:
#             print('1', end=" ")
#     print()

# s = "python"
# for i in range(0, len(s)):
#     for j in range(0, i + 1):
#         print(s[j], end = " ")
#     print()

# n = int(input("Enter the number: "))
# a = 0
# b = 1
# for i in range(1, n):
#     a, b = b, a + b
# print("The nth number in the Fibonacci series is", a)

# s = "python is a programming language"
# l = s.split()
# d = {}
# for i in l:
#     d[i]= len(i)
# print(d)

# s = "python is a programming language"
# vowels = "AEIOUaeiou"
# count = 0
# for i in s:
#     if i in vowels:
#         count += 1
# print("The no. of vowels is", count)

# l = [1,2,3,4,2,5,3,4]
# k = []
# for i in l:
#     if i in k:
#         print(i)
#         break
#     k.append(i)
# else:
#     print("There is no duplicate element")

# target = 6
# l = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] + l[j] == target:
#             print(l[i], l[j])

l = [12, -45, 2, 67, -82, -5]
k = list(filter(lambda x:x<0 and x%2!=0, l))
print(k)
import functools
sum = functools.reduce(lambda a, b: a + b, k)
print(sum)

# def smart_sub(func):
#     def wrapper(x, y):
#         if x < y:
#             x, y = y, x
#         return func(x, y)
#     return wrapper
#
# @smart_sub
# def sub(a, b):
#     diff = a - b
#     return diff
#
# print(sub(8, 1))
# print(sub(2, 9))
# print(sub(3, 8))

# def func(*args):
#     print(args)
#
# func(1, 2, 3)
#
# def func1(**kwargs):
#     print(kwargs)
#
# func1(a=1, b=2, c=3)

# def add_book():
#     book_id = int(input("Enter the book id: "))
#     t = input("Enter the title: ")
#     a = input("Enter the author: ")
#     p = input("Enter the price: ")
#     books[book_id] = {"title": t, "author": a, "price": p}
#     print("Book created successfully!")
#     return
#
# def show_all_books():
#     for i in books.items():
#         print(i)
#     return
#
# def show_book():
#     book_id = int(input("Enter the book id: "))
#     if book_id in books:
#         print(books[book_id])
#     else:
#         print("Book not found!")
#
# def update_book():
#     book_id = int(input("Enter the book id: "))
#     if book_id in books:
#         books[book_id]["title"] = input("Enter the title: ")
#         books[book_id]["author"] = input("Enter the author: ")
#         books[book_id]["price"] = int(input("Enter the price: "))
#         print("Book successfully updated!")
#     else:
#         print("Book not found!")
#
# def delete_book():
#     book_id = int(input("Enter the book id: "))
#     if book_id in books:
#         books.pop(book_id)
#         print("Book successfully deleted!")
#     else:
#         print("Book not found!")
#
# books = {}
# while(1):
#     print("1. Add books")
#     print("2. Show all books")
#     print("3. Show a specific book")
#     print("4. Update a specific book")
#     print("5. Delete a specific book")
#     print("6. Exit")
#     n = int(input("Enter the choice: "))
#     if n == 1:
#         add_book()
#     elif n == 2:
#         show_all_books()
#     elif n == 3:
#         show_book()
#     elif n == 4:
#         update_book()
#     elif n == 5:
#         delete_book()
#     elif n == 6:
#         exit()

# def smart_div(fun):
#     def wrapper(x, y):
#         if y < x:
#             x, y = y, x
#         return fun(x, y)
#     return wrapper
#
# @smart_div
# def div(x, y):
#     res = x / y
#     print(res)
#     return
#
# div(1, 5)
# div(5, 1)
# div(6, 0)

n = 4
k = 3 * 2
for i in range(1, n + 1):
    for p in range(1, k + 1):
        print(end=" ")
    k -= 2
    for j in range(1, i + 1):
        print("*", end="   ")
    print()
k = 2
for i in range(3, 0, -1):
    for p in range(0, k):
        print(end=" ")
    k += 2
    for j in range(1, i + 1):
        print("*", end="   ")
    print()