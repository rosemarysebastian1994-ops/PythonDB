# def add(n1, n2):
#     sum = n1 + n2
#     print("The sum is", sum)
#     return
#
# def sub(n1, n2):
#     diff = n1 - n2
#     print("The difference is", diff)
#     return
#
# def mul(n1, n2):
#     pro = n1 * n2
#     print("The product is", pro)
#     return
#
# def div(n1, n2):
#     quo = n1 / n2
#     print("The quotient is", quo)
#     return
#
# while(1):
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     c = int(input("Enter the choice: "))
#     if c in [1, 2, 3, 4]:
#         n1 = int(input("Enter the first number: "))
#         n2 = int(input("Enter the second number: "))
#     if c == 1:
#         add(n1, n2)
#     elif c == 2:
#         sub(n1, n2)
#     elif c == 3:
#         mul(n1, n2)
#     elif c == 4:
#         div(n1, n2)
#     else:
#         exit()

def add():
    n = int(input("Enter the id: "))
    if n in d:
        print("The book with this id", id, "is already present")
    else:
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        price = int(input("Enter the price: "))
        d[n]={"title":title, "author":author, "price":price}
    return

def show_all():
    for i in d:
        print(i, ":", d[i])
    return

def show():
    n = int(input("Entder the book id: "))
    if n in d:
        print(d[n])
    else:
        print("Not found")
    return

def update():
    n = int(input("Enter the id: "))
    if n in d:
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        price = int(input("Enter the price: "))
        d[n] = {"title": title, "author": author, "price": price}
    else:
        print("Not found")
    return

def delete():
    n = int(input("Enter the id: "))
    if n in d:
        d.pop(n)
        print("Deleted successfully")
    else:
        print("Not found")
    return

d = {}
while(1):
    print("1. Add a book")
    print("2. Show all books")
    print("3. Show a specific book")
    print("4. Update a specific book")
    print("5. Delete a specific book")
    c = int(input("Enter the choice: "))
    if c == 1:
        add()
    elif c == 2:
        show_all()
    elif c == 3:
        show()
    elif c == 4:
        update()
    elif c == 5:
        delete()
    else:
        exit()