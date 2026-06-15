x = 2
y = 3

# temp = x
# x=y
# y = temp

# x,y = y,x

x = x + y
y = x - y
x = x - y
print("After swapping x = ", x, " y = ", y)

l = [1,2,3,4,5,6,7,8]
l[2], l[5] = l[5], l[2]
print(l)