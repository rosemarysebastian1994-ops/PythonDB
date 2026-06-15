class Parent:
    def f1(self):
        print("in function 1")
    def f2(self):
        print("in function 2")

class Child(Parent):
    def f3(self):
        print("in function 3")
    def f1(self):
        print("in child class")
c = Child()
c.f3()
c.f1()
c.f2()