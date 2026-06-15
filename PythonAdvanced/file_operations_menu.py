# import os
#
# def write_file():
#     file_name = input("Enter the file name: ")
#     f = open(file_name, 'w')
#     content = input("Enter the content: ")
#     f.write(content)
#     return
#
# def read_file():
#     file_name = input("Enter the file name: ")
#     try:
#         f = open(file_name, 'r')
#     except FileNotFoundError:
#         print("No such file")
#         return
#     content = f.read()
#     print(content)
#
# def append_file():
#     file_name = input("Enter the file name: ")
#     content = input("Enter the content: ")
#     f = open(file_name, "a+")
#     f.write(content)
#     return
#
# def search_word():
#     file_name = input("Enter the file name: ")
#     word = input("Enter the word to search: ")
#     f = open(file_name, "r")
#     s = f.read()
#     if word in s:
#         print("Word found")
#     else:
#         print("Word not found")
#     return
#
# def delete_file():
#     file_name = input("Enter the file name: ")
#     os.remove(file_name)
#     print(file_name, "deleted successfully")
#     return
#
# while 1:
#     print("1. Write content to a file")
#     print("2. Read content from a file")
#     print("3. Append content to a file")
#     print("4. Search word in a file")
#     print("5. Delete a file")
#     print("6. Exit")
#     ch = int(input("Enter the choice: "))
#     if ch == 1:
#         write_file()
#     elif ch == 2:
#         read_file()
#     elif ch == 3:
#         append_file()
#     elif ch == 4:
#         search_word()
#     elif ch == 5:
#         delete_file()
#     elif ch == 6:
#         exit()
#     else:
#         pass

class A:
    def __init__(self):
        self.n = int(input("Enter the number: "))
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n

x = A()
y = A()
print(x + y)
print(x - y)
print(x * y)
print(x / y)