import sqlite3
con = sqlite3.connect("my.db")
# con.execute("create table person(id int primary key, name varchar(20), place varchar(20), age int)")

# i = int(input("Enter the id: "))
# n = input("Enter the name: ")
# p = input("Enter the place: ")
# a = int(input("Enter the age: "))
# con.execute("insert into person(id, name, place, age)  values(?,?,?,?)", (i, n, p, a))
# con.commit()
# print("Inserted successfully")

i = int(input("Enter the id: "))
k=con.execute("select * from person where id = (?)", (i,))
print(k.fetchall())