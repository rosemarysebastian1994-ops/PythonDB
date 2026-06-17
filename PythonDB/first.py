import sqlite3
con=sqlite3.connect("company.db")
#To create a table
#create table tablename(field1 type, field2 type...)
# sql_command = '''create table employee(empid int primary key,name varchar(20),place varchar(20),salary int,gender varchar(10))'''
# con.execute(sql_command)
# print("Table created successfully")
# sql_command = '''insert into employee(empid, name, place, salary, gender)
#               values(100, "arun", "ekm", 20000, "male")'''
# con.execute(sql_command)
# # con.commit()
# con.execute('''insert into employee(empid, name, place, salary, gender)
#               values(101, "amal", "tcr", 25000, "male")''')
# con.commit()
# con.execute('''insert into employee(empid, name, place, salary, gender)
#               values(102, "anu", "ksd", 20000, "female")''')
# con.commit()
# con.execute('''insert into employee(empid, name, place, salary, gender)
#               values(103, "athira", "ekm", 20000, "female")''')
# con.commit()
# To read all records from the table with all attributes
# k = con.execute("select * from employee")
# print(k.fetchall())
# #To read all records with specific attributes
# k = con.execute("select name, place, salary from employee")
# print(k.fetchall())
# #To read specific record with all attributes
# k = con.execute("select * from employee where empid=102")
# print(k.fetchall())
# #To read specific record with specific attribute
# k = con.execute("select name,gender from employee where empid=102")
# print(k.fetchall())

k=con.execute("select * from employee1 where salary>24000")
print(k.fetchall())
k=con.execute("select * from employee1 where id!=100")
print(k.fetchall())
k=con.execute("select * from employee1 where salary between 20000 and 24000")
print(k.fetchall())
k=con.execute("select name, place, gender from employee1 where name like 'a_u'")
print(k.fetchall())
#Records having salary 29000 or 30000
k = con.execute("select * from employee1 where salary in (29000, 30000)")
print(k.fetchall())
#Records having name starting with letter 'a'
k = con.execute("select * from employee1 where name like 'a%'")
print(k.fetchall())
#Records having place containing letter 'k'
k = con.execute("select * from employee1 where place like '%k%'")
print(k.fetchall())
#Records having name end with 'n'
k = con.execute("select * from employee1 where name like '%n'")
print(k.fetchall())
#Records having place end with 'm'
k = con.execute("select * from employee1 where place like '%m'")
print(k.fetchall())
#Records having 4 letter name ends with n
k = con.execute("select * from employee1 where name like '___n'")
print(k.fetchall())
#Records having 3 letter name ends with 'r'
k = con.execute("select * from employee1 where name like '__r'")
print(k.fetchall())
#Records having name start with letter 'k' and salary > 25000
k = con.execute("select * from employee1 where name like 'k%' and salary > 25000")
print(k.fetchall())
#Records having age is 25 or salary greater than 25000
k = con.execute("select * from employee1 where salary=20000 or salary>25000")
print(k.fetchall())
#Records having salary other than 25000 and 30000
k = con.execute("select * from employee1 where salary not in (25000, 30000)")
print(k.fetchall())
