import pymysql
con = pymysql.connect(user="root", password="root", host="localhost", database="mydb2")
print('database connected successfully')
c=con.cursor()
# c.execute('''CREATE TABLE department(dep_id int primary key,dep_name varchar(25),dep_head varchar(35))''')
# c.execute('''CREATE TABLE employee(emp_id int primary key, dep_id int, emp_name varchar(20),
#              emp_age int, emp_gender varchar(20), foreign key (dep_id) references department(dep_id))''')
# print('tables created successfully')

# i = int(input("Enter the dep_id: "))
# n = input("Enter the dep_name: ")
# h = input("Enter the dep_head: ")
# c.execute("insert into department values(%s,%s,%s)",(i,n,h))
# con.commit()
# print("data inserted successfully")

# i = int(input("Enter the emp_id: "))
# d = int(input("Enter the dep_id: "))
# n = input("Enter the emp_name: ")
# a = int(input("Enter the emp_age: "))
# g = input("Enter the emp_gender: ")
# c.execute("insert into employee values(%s,%s,%s,%s,%s)", (i,d,n,a,g))
# con.commit()
# print("data inserted successfully")

# c.execute("update employee set emp_name='Fida', emp_gender='Female' where emp_id=1")
# con.commit()
# print("Updated successfully")

c.execute("select count(*), sum(emp_age), avg(emp_age), max(emp_age), min(emp_age) from employee")