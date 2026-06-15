# s = '''Mike is 16 and John is 24
#        Sam is 23 and James is 36'''
# import re
# names = re.findall('[A-Z][a-z]+', s)
# print(names)
# age = re.findall('[0-9]{2}', s)
# print(age)

# s = "abd abcd abccd abcccd abed"
# import re
# res = re.findall('abc{1,4}d', s)
# print(res)

# Find all the words starting with s,p,r and ends at 'at'
# s = "mat pat cat rat bat"
# import re
# res = re.findall('[spr]at', s)
# print(res)

#Find all words starting with except s,p,r and ends at 'at'
# k = "mat pat cat rat bat"
# import re
# res = re.findall('[^spr]at', k)
# print(res)

# Find all 3, 4, 5-letter words from the string
# l = "python was a high level language"
# import re
# res = re.findall(r'\b[a-z]{3,5}\b', l)
# print(res)

# Find all 3digit/4digit/5digit numbers from the string
m = "131 57777782 4356 0986756 87879"
import re
res = re.findall(r'\b[0-9]{3,5}\b', m)
print(res)