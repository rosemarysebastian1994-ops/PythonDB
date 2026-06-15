# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)
s = input()
l = s.split()
n = int(l[0])
m = int(l[1])
for i in range(1, n + 1):
    d[input()].append(i)
for i in range(1, m + 1):
    a = input()
    if a not in d:
        print(-1, end = " ")
    else:
        b = d[a]
        for j in b:
            print(j, end = " ")
    print()


