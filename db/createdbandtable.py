from mysql import connector

mydb = connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycur = mydb.cursor()
dbname = "MYDATABASE"
table = "STUDENTS"

mycur.execute(f'CREATE DATABASE {dbname}')

mydb = connector.connect(
    host="localhost",
    user="root",
    password="",
    database = dbname
)
mycur = mydb.cursor()
mycur.execute(f'CREATE TABLE {table} (NAME VARCHAR(50),ROLLNO VARCHAR(10),MARK1 INT(5),MARK2 INT(5),MARK3 INT(5),MARK4 INT(5),TOTAL INT(5),AVERAGE INT(5))')
