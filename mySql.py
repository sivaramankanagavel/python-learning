import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sivaraman@1996"
)

print(mydb)