class A:
    def __init__(self):
        self.n = int(input("Enter the number: "))
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n

x = A()
y = A()
print(x + y)
print(x - y)
print(x * y)
print(x / y)