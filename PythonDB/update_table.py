import sqlite3
con=sqlite3.connect("company.db")
# Update
# update table_name set field1=value, field2=value... where condition
# con.execute("update employee set name='fida', salary=45000 where empid=103")
# con.commit()
# print("Updated successfully")

#Aggregate functions avg(), sum(), count(), min(), max()
# k = con.execute("select count(*), sum(salary), avg(salary), max(salary), min(salary) from employee1")
# print(k.fetchall())

#Order by
# k = con.execute("select salary from employee order by salary desc")
# print(k.fetchall())

# Distinct - to remove duplicates
# k = con.execute("select distinct(place) from employee")
# print(k.fetchall())

# con.execute('''insert into employee(empid, name, place, salary, gender)
#               values(105, "Kiran", "tvm", 20000, "male")''')
# con.commit()
# con.execute('''insert into employee(empid, name, place, salary, gender)
#               values(106, "anju", "ksd", 40000, "female")''')
# con.commit()

# k = con.execute("select * from employee where salary>=20000 limit 1 offset 2")
# print(k.fetchall())
#
# k = con.execute("select * from employee order by salary desc limit 1 offset 2")
# print(k.fetchall())

# k = con.execute("select gender, sum(salary) from employee1 group by gender having gender='female'")
# print(k.fetchall())

# con.execute("alter table employee add column email varchar(30)")
# con.commit()

#Alter - to change the structure
#Add column, drop column
# con.execute("update employee set email='anju@gmail.com' where empid=106")
# con.commit()
# print("Updated successfully")
# con.execute("alter table employee drop column email")
# con.commit()

# Rename table name
# con.execute('alter table employee rename to employee1')
# con.commit()

# Rename column name
# con.execute("alter table employee1 rename empid to id")
# con.commit()

# con.execute("delete from employee1 where id=100")
# con.commit()
