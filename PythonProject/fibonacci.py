# a = 0
# b = 1
# for i in range(1, 11):
#     print(a)
#     a, b = b, a + b

# Print a string with no vowel
# s = "python is a programming language"
# k = ""
# vowels = "AEIOUaeiou"
# for i in s:
#     if i not in vowels:
#         k += i
# print(k)

# Print a string with no duplicate
# s = "python is a programming language"
# k = ""
# for i in s:
#     if i not in k:
#         k += i
# print(k)

# Remove duplicate elements in a list
l = [1, 2, 3, 5, 1, 2, 7, 8, 5]
j = set(l)
k = list(j)
print(k)