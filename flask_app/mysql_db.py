import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", password="9944394985",database="users")

my_db = dataBase.cursor()

# my_db.execute("delete from user where user_id = 1")
# my_db.execute("create table user(user_id int auto_increment primary key, Name varchar(200), Email varchar(200))")
# my_db.execute("insert into user (Name ,Email) values ('sharook', 'aydensharu@gmail.com')")
my_db.execute("select * from user")
for i in my_db:
    print(i)