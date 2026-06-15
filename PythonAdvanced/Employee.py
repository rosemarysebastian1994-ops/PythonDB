# class Person:
#     def __init__(self):
#         self.name = input("Enter the name: ")
#         self.age = int(input("Enter the age: "))
#         self.gender = input("Enter the gender: ")
#     def show_details(self):
#         print("The name is ", self.name, "the age is", self.age, "the gender is", self.gender)
#
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.emp_id = int(input("Enter the employee id: "))
#         self.salary = int(input("Enter the salary: "))
#
#     def show_details(self):
#         super().show_details()
#         print("The employee id is", self.emp_id, "the salary is", self.salary)
#
# e = Employee()
# e.show_details()

# class Vehicle:
#     def __init__(self):
#         self.brand = input("Enter the brand: ")
#         self.model = input("Enter the model: ")
#         self.year = input("Enter the year: ")
#     def show_details(self):
#         print("The brand is", self.brand, "the model is", self.model, "the year is", self.year)
#
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.mileage = int(input("Enter the mileage: "))
#     def show_details(self):
#         super().show_details()
#         print("The mileage is", self.mileage)
#
# c = Car()
# c.show_details()

# class Student:
#     def __init__(self):
#         self.name = input("Enter the name: ")
#         self.roll_no = int(input("Enter the roll no.: "))
#     def display_info(self):
#         print("The name is", self.name, "the roll no. is", self.roll_no)
# class Marks(Student):
#     def __init__(self):
#         super().__init__()
#         self.marks1 = int(input("Enter the marks 1: "))
#         self.marks2 = int(input("Enter the marks 2: "))
#         self.marks3 = int(input("Enter the marks 3: "))
#     def display_info(self):
#         super().display_info()
#         print("The marks for three subjects are", self.marks1, self.marks2, self.marks3)
#     def total(self):
#         print(self.marks1 + self.marks2 + self.marks3)
# m = Marks()
# m.display_info()
# m.total()

# class Hospital:
#     def __init__(self):
#         self.hosp_name = input("Enter the hospital name: ")
#         self.location = input("Enter the location: ")
#         self.phone = int(input("Enter the phone no.: "))
#     def show_details(self):
#         print("The hospital name is ", self.hosp_name)
#         print("The location is", self.location)
#         print("The phone no. is", self.phone)
#
# class Department:
#     def __init__(self):
#         self.dept_name = input("Enter the department name: ")
#         self.doctor_name = input("Enter the doctor's name: ")
#     def show_details(self):
#         print("The department name is", self.dept_name)
#         print("The doctor's name is", self.doctor_name)
#
# class Patient(Hospital, Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name = input("Enter the patient's name: ")
#         self.age = int(input("Enter the age: "))
#         self.gender = input("Enter the gender: ")
#     def show_details(self):
#         Hospital.show_details(self)
#         Department.show_details(self)
#         print("The patient's name is", self.patient_name, "Age is", self.age, "Gender is", self.gender)
#
# p = Patient()
# p.show_details()

class Vehicle:
    def __init__(self):
        self.brand = input("Enter the brand name: ")
        self.model = input("Enter the model: ")
        self.year = int(input("Enter the year: "))
        self.color = input("Enter the color: ")
    def show_details(self):
        print("The brand is", self.brand, "the model is", self.model, "the year is", self.year, "the color is", self.color)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel_type = input("Enter the fuel type: ")
    def show_details(self):
        super().show_details()
        print("The fuel type is", self.fuel_type)

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc = int(input("Enter the cc: "))
    def show_details(self):
        super().show_details()
        print("The cc is", self.cc)

vehicles = []
while 1:
    print("1. Add car")
    print("2. Add bike")
    print("3. Show all vehicles")
    print("4. Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        c = Car()
        vehicles.append(c)
    elif ch == 2:
        b = Bike()
        vehicles.append(b)
    elif ch == 3:
        for i in vehicles:
            i.show_details()
    elif ch == 4:
        exit()
    else:
        pass
