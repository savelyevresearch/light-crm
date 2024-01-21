import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123'
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE light-crm")

print('All Done!')