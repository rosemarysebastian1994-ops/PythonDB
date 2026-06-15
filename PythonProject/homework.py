# s = input("Enter the string: ")
# letters_present = ""
# repeating_letters = ""
# for letter in s:
#     if letter not in letters_present:
#         letters_present += letter
#     elif letter not in repeating_letters:
#         repeating_letters += letter
#     else:
#         pass
# for letter in letters_present:
#     if letter not in repeating_letters:
#         print(letter)
#         break
# else:
#     print(None)

s = input("Enter the string: ")
for i in s:
    if s.count(i) == 1:
        print(i)
        break
else:
    print(None)