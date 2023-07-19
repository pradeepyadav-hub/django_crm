import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '',

	)

#prepare 
cursorObject = dataBase.cursor()



cursorObject.execute("CREATE DATABASE django_db1")

print("ALL Done")