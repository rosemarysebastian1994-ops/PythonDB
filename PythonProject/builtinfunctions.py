#Find the minimum element from the list
# l1 = [12, 56, 44, 11, 32]
l = [1, 23, 45, 56, 23, 45]
# print(min(l))
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(min)

#Find the second minimum element from the list
# l.sort()
# print(l)
# print(l[1])
# m = min(l)
# l.remove(m)
# print(l)
# print(min(l))

#Display the largest element in a list
k = [22, 34, 56, 1, 24, 78, 78, 45, 45]
# largest = max(k)
# print(largest)
# largest = k[0]
# for i in k:
#     if i > largest:
#         largest = i
# print(largest)

#Find the second largest element from the list
# s = set(k)
# k = list(s)
# largest = max(k)
# k.remove(largest)
# second_largest = max(k)
# print(second_largest)

#Find the common element from the given sequence
# l1 = [12, 56, 44, 11, 32]
# l2 = [11, 25, 67, 32]
# s1 = set(l1)
# s2 = set(l2)
# print(s1 & s2)

#Find the maximum salary from the given data
# l = {1:["arun", 23, 20000], 2:["amal", 26, 30000], 3:["kiran", 25, 35000]}
#
# k = max([i[2] for i in l.values()])
# print(k)

# Global
# x = 20
# print(x)
# def fun():
#     print(x)
#     return
# fun()

# Local
# def fun():
#     x = 20
#     print(x)
# fun()

# def outer():
#     x = 20
#     print(x)
#     def inner():
#         print(x)
#
#     inner()
# outer()

# l = [1, 2, 3, 4]
# print(tuple(map(lambda x:x**2, l)))
# Find the square roots
# l = [16, 22, 81]
# print(list(map(lambda x:x**0.5, l)))
#
# colors = ["red", "yellow", "blue", "pink"]
# print(list(map(lambda x:len(x), colors)))
# print the first color
# s = lambda x:x[0]
# print(s(colors))

# sum = lambda a, b: a + b
# print(sum(1, 2))
# product = lambda a, b: a * b
# print(product(2, 4))
# diff = lambda a, b: a - b
# print(diff(2, 1))

# d = {"name":"arun", "age":24, "place":"ekm"}
# s = lambda x:x["name"]
# print(s(d))