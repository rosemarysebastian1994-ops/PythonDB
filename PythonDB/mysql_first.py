import mysql.connector
con = mysql.connector.connect(user="root", password="root", host="localhost")
c = con.cursor()
c.execute("create database mydb2")
print("database file created successfully")
