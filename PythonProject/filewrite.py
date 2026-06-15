# f = open("k.txt", 'w')
# f.write("python\n")
# f.write("django")
# f = open("m.txt", 'r')
# s = f.readline()
# print(s)
# s = f.readline()
# print(s)
# l = f.readlines()
# print(l)

# Write a program to print the number of lines in a file
# f = open("m.txt", "r")
# l = f.readlines()
# print(len(l))

# Write a program to print the number of words in a file
# f = open("m.txt", "r")
# s = f.read()
# l = s.split()
# print(len(l))

# Write a program to print the last 5 lines from a file
# f = open("m.txt", "r")
# l = f.readlines()
# for i in range(-5, 0):
#     print(l[i])
# print(l[-5:])

# Write a program to change the second line in a file
# f = open("m.txt", "r")
# l = f.readlines()
# l[1] = "hello world\n"
# f = open("m.txt", "w")
# f.writelines(l)

# Write a program to find the total number of digits, letters and spaces in a file
# f = open("m.txt", "r")
# s = f.read()
# count_digits = 0
# count_letters = 0
# count_spaces = 0
# for i in s:
#     if i.isdigit():
#         count_digits += 1
#     elif i.isalpha():
#         count_letters += 1
#     elif i.isspace():
#         count_spaces += 1
#     else:
#         pass
# print("The no. of digits: ", count_digits)
# print("The no. of letters: ", count_letters)
# print("The no. of spaces: ", count_spaces)

# Write a program to read from a text file and write to another file
# f = open("k.txt", "r")
# s = f.read()
# f = open("l.txt", "w")
# f.write(s)

# f = open("l.txt", "a+")
# f.write("hello")
# print(f.tell()) # Returns the current file pointer position value
# f.seek(5, 0) # To change the file pointer position
# s = f.read()
# print(s)
# From - means the reference point from which the offset is applied
# Offset - the no. of characters to move the file pointer

# import os
# os.remove("k.txt")
# print("Successfully deleted")

# def write_file():
#     file_name = input("Enter the file name: ")
#     s = input("Enter the content: ")
#     f = open(file_name, "w")
#     f.write(s)
#
# while(1):
#     print("1. Write a content to a file")
#     print("2. Read a content from a file")
#     print("3. Append a content in to a file")
#     print("4. Search a word is present in a file")
#     print("5. Delete a file")
#     print("6. Exit")
#     n = int(input("Enter the choice: "))
#     if n == 1:
#         write_file()
#     elif n == 6:
#         exit()
#     else:
#         pass