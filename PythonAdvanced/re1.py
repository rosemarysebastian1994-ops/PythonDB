# s = "hello python"
# import re
# r = re.match(r'hello', s)
# if r:
#     print("Match found")
#     print(r.group())
# else:
#     print("Not found")

# s = "hi python hello python hello"
# import re
# r = re.search(r'hello', s)
# if r:
#     print("Match found", r.group())
# else:
#     print("Not found!")

# s = "mike@abc.com and john@pqr.com"
# import re
# r = re.sub(r'@[a-z]+', '@gmail', s)
# print(r)

# s = "python is a programming language"
# import re
# r = re.split(r'\s', s)
# print(r)

# Write a program to find the filenames with particular extensions
# s = "s.html, l.txt, m.jpeg, re1.py, a.jpeg"
# ext = input("Enter the extension: ")
# import re
# res = re.findall(r'[A-Za-z]+[0-9]*.'+ext, s)
# print(res)

# Write a program to find words containing 'z' from a string
# s = "abcdz abczd zabcd jkhj zzzz azbcbcza"
# import re
# res = re.findall('[a-z]*z[a-z]*', s)
# print(res)

# Check whether the given string contains only lowercase, uppercase, digits and _
# s = "sdfgbdtgd346546_09"
# import re
# res = re.match(r'^[\w]+$', s)
# if res:
#     print("Match found")
#     print(res.group())
# else:
#     print("Not found")

# Write a program to extract the year/month/date from a url
# s = "www.washingtonpost.com/news/football-insider/wp/2016/09/02"
# import re
# res = re.search('[0-9]{4}/[0-9]{2}/[0-9]{2}', s)
# print(res.group())

# Replace \n with space
# s = '''keep the blue flag
# flying high
# cheseas'''
# o/p s = "keep the blue flag high cheseas"
# import re
# res = re.sub(r'\n', " ", s)
# print(res)

# Replace dot, comma and space with :
# s = "python is a programming language."
# # o/p "python:is:a:programming:language:"
# import re
# res = re.sub(r'[.,\s]', ':', s)
# print(res)

# Remove all alphanumeric characters from the string
# s = "asdfg546 %$^&*!%^ sadfdfsg_sdfg"
# # o/p " %$^&*!%^ _"
# import re
# res = re.sub("[A-Za-z0-9]+", "", s)
# print(res)

# Find all the words starting with vowel and ends with vowel from the given string
# s = "red green orange"
# import re
# res = re.findall(r'\b[AEIOUaeiou][A-Za-z]*[AEIOUaeiou]\b', s)
# print(res)

# Find the count of numbers in the string
# s = "One 1 two 2 three 3 and 45676"
# import re
# res = re.findall('[0-9]', s)
# print(len(res))

# import re
#
# t = int(input())
# for i in range(t):
#     n = input()
#     res = re.match(r'^[-+\d]\d*[.]\d+$', n)
#     if not res:
#         res = re.match(r'^[.]\d+$', n)
#     if res:
#         print(True)
#     else:
#         print(False)
