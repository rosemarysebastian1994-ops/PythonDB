class Book:
    def __init__(self):
        self.book_id = int(input("Enter the book id: "))
        for i in l:
            if i.book_id == self.book_id:
                print("Book already present")
                break
        else:
            self.title = input("Enter the title: ")
            self.author = input("Enter the author: ")
            self.price = int(input("Enter the price: "))
            l.append(self)
            print("Book added successfully")
    def show_details(self):
        print("The details are: ", self.book_id, self.title, self.author, self.price)
        return
    def update_book(self):
        self.title = input("Enter the new title: ")
        self.author = input("Enter the new author: ")
        self.price = int(input("Enter the new price: "))
        return
    def delete_book(self):
        l.remove(self)
        print("Book deleted successfully")
        return

l = []
while 1:
    print("1. Add book")
    print("2. Book list")
    print("3. Book details")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        b = Book()
    elif ch == 2:
        for i in l:
            i.show_details()
    elif ch == 3:
        b_id = int(input("Enter the book id: "))
        for i in l:
            if b_id == i.book_id:
                i.show_details()
                break
        else:
            print("No book found!")
    elif ch == 4:
        b_id = int(input("Enter the book id: "))
        for i in l:
            if b_id == i.book_id:
                i.update_book()
                break
        else:
            print("Book not present")
    elif ch == 5:
        b_id = int(input("Enter the book id: "))
        for i in l:
            if b_id == i.book_id:
                i.delete_book()
                break
        else:
            print("Book not present")
    elif ch == 6:
        exit()
    else:
        pass

