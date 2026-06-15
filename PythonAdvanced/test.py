# 1. Write a program to reverse the lines in a file.
# f = open("k.txt", "r")
# l = f.readlines()
# l[-1] = l[-1] + "\n"
# k = l[::-1]
# f = open("l.txt", "w+")
# f.writelines(k)

# 2. Given a string
# s = "mobile numbers are 9867354671 and 8589678991"
# # Write a program to extract mobile numbers
# import re
# result = re.findall(r'\d{10}', s)
# print(result)

# 3. Write a program to check whether the entered number is a valid mobile number.
# import re
# mobile_number = input("Enter the mobile number: ")
# result = re.match(r'^[6789]\d{9}$', mobile_number)
# if result:
#     print("Match found")
# else:
#     print("Not found")

# 4. Create a class Category with attributes category_name and method display() and create a sub-class Product
# with attributes product_name, price, quantity, description and methods display() and total_price().

# class Category:
#     def __init__(self):
#         self.category_name = input("Enter the category name: ")
#     def display(self):
#         print("The category name is", self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name = input("Enter the product name: ")
#         self.price = int(input("Enter the price: "))
#         self.quantity = int(input("Enter the quantity: "))
#         self.description = input("Enter the description: ")
#     def display(self):
#         super().display()
#         print("The product name is", self.product_name)
#         print("The price is", self.price)
#         print("The quantity is", self.quantity)
#         print("The description is", self.description)
#     def total_price(self):
#         print("The total price is", self.price * self.quantity)
#
# p = Product()
# p.display()
# p.total_price()

# 5. Given a list convert each element into int and print element. if an exception occurs
# handle with try-except handling block.
l = ['10', '20', 'abc', '30']
# k = []
for i in l:
    try:
        a = int(i)
        print(a)
    except ValueError:
        print("String", i, "cannot be converted to int")
    # else:
    #     print(i)
    # finally:
    #     print(k)