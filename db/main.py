from mysql import connector
import math

mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MYDATABASE"
)

mycur = mydb.cursor()

name = input("Enter Student Name : ")
rollno = input("Enter RollNo  : ")
m1 = int(input("Enter Mark 1  : "))
m2 = int(input("Enter Mark 2  : "))
m3 = int(input("Enter Mark 3  : "))
m4 = int(input("Enter Mark 4  : "))

insert_query = "INSERT INTO STUDENTS (NAME,ROLLNO,MARK1,MARK2,MARK3,MARK4) VALUES(%s,%s,%s,%s,%s,%s)"
values = (name,rollno,m1,m2,m3,m4)
mycur.execute(insert_query,values)

total = m1+m2+m3+m4
avg = math.floor(total/4)
update_query = f'UPDATE STUDENTS SET TOTAL = {total} ,AVERAGE= {avg} WHERE ROLLNO = {rollno} '
mycur.execute(update_query)

select_query = f'SELECT * FROM STUDENTS'
mycur.execute(select_query)
result = mycur.fetchall()

mydb.commit()

for x in result:
    print(x)