for i in range(0,4):
    c = 65
    for j in range(0, i + 1):
        print(chr(c), end=" ")
        c += 1
    print()

for i in range(0, 4):
    c = 65
    for j in range(0, 4 - i):
        print(chr(c), end=" ")
        c += 1
    print()