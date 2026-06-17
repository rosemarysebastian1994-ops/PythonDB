import pymysql

con = pymysql.connect(host="localhost", user="root", password="root")
print("Connected successfully")
c = con.cursor()
# c.execute("create database mydb2")

print("database file created successfully")
con.close()