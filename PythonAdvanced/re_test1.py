# Write a program to find the filenames with particular extensions
# s = "s.html, l.txt, m.jpeg, re1.py, a.jpeg"
# import re
# res= re.findall(r'[a-z]+[0-9]*.jpeg', s)
# print(res)

# Write a program to find words containing 'z' from a string
# s = "abcdz abczd zabcd jkhj zzzz"
# import re
# res = re.findall(r'[a-z]*z[a-z]*', s)
# print(res)

# Check whether the given string contains only lowercase, uppercase, digits and _
# s = "sdfgbdtgd346546_09"
# import re
# res = re.match(r'^[\w]+$', s)
# if res:
#     print("Match found")
# else:
#     print("Match not found")

# Write a program to extract the year/month/date from a url
# s = "www.washingtonpost.com/news/football-insider/wp/2016/09/02"
# import re
# res = re.search(r'[\d]{4}/[\d]{2}/[\d]{2}', s)
# print(res.group())

# Replace \n with space
# s = '''keep the blue flag
# flying high
# cheseas'''
# o/p s = "keep the blue flag high cheseas"
# import re
# res = re.sub(r'\s', " ", s)
# print(res)

# Replace dot, comma and space with :
# s = "python is a programming language."
# # o/p "python:is:a:programming:language:"
# import re
# res = re.sub(r'[.,\s]', ":", s)
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
# res = re.findall(r"[\d]", s)
# print(len(res))

# Write a program to check whether a string is a floating point number
import re
t = int(input())
for i in range(t):
    n = input()
    res = re.match(r'^[-+\d]\d*[.]\d+$', n)
    if not res:
        res = re.match(r'^[.]\d+$', n)
    if res:
        print(True)
    else:
        print(False)