# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
s = input()
l = s.split()
a = []
for j in l:
    a.append(int(j))
print(Counter(a))
N = int(input())
sum = 0
d = Counter(a)
k = Counter(a).keys()
m = Counter(a).values()
for i in range(0, N):
    s = input()
    l = s.split()
    b = []
    for j in l:
        b.append(int(j))
    if b[0] in k:
        sum += b[1]
        d[b[0]] -= 1
print(sum)