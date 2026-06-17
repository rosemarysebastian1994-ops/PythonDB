import sqlite3
con = sqlite3.connect("shop.db")

# con.execute("create table product(p_id int primary key, p_name varchar(20), p_price int)")
#
# con.execute("""create table order_details(order_id int primary key,
#                                           p_id int,
#                                           quantity int,
#                                           date date,
#                foreign key (p_id) references product(p_id))""")
# print("Created two tables successfully")

# con.execute("insert into product(p_id,p_name,p_price) values(1,'prodA',200)")
# con.execute("insert into product(p_id,p_name,p_price) values(2,'prodB',500)")
# con.execute("insert into product(p_id,p_name,p_price) values(3,'prodC',300)")
# con.execute("insert into product(p_id,p_name,p_price) values(4,'prodD',700)")
# con.execute("insert into order_details(order_id,p_id,quantity,date) values(1,2,4,'2026-04-12')")
# con.execute("insert into order_details(order_id,p_id,quantity,date) values(2,3,10,'2026-05-02')")
# con.commit()
# print("data inserted successfully")

k = con.execute("select * from product inner join order_details on product.p_id=order_details.p_id where product.p_id=3")
print(k.fetchall())