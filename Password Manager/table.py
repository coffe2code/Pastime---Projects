import sqlite3
import crypto
import os

path = "/home/beowulf/Passwords/"

def initFunc(tableName):
	conn = sqlite3.connect(path+tableName+".db")
	cur = conn.cursor()
	cur.execute('''CREATE TABLE PASSWORDLIST
				(NAME 	 TEXT NOT NULL,
				PASSWORD TEXT NOT NULL);''')
	conn.close()

	print("Created database " + tableName+".db"+" successfully")
	crypto.keyGen(tableName)
	print("Create Key "+ tableName+".key"+" successfully")

def setFunc(name, tableName, password):
	key = crypto.readKey(tableName)
	entry = crypto.encryptPassword(password, key)

	conn = sqlite3.connect(path+tableName+".db")
	cur = conn.cursor()
	cur.execute("INSERT INTO PASSWORDLIST (NAME, PASSWORD) VALUES (?, ?)",
				(name, entry))
	conn.commit()
	cur.close()
	conn.close()
	print("Added entry for "+name+" successfully")

def fetchFunc(tableName, name):
	conn = sqlite3.connect(path+tableName+".db")
	cur = conn.cursor()
	cur.execute("SELECT PASSWORD FROM PASSWORDLIST WHERE NAME = (?)",
				(name, ))

	password = cur.fetchall()[0][0]
	key = crypto.readKey(tableName)
	password = crypto.decryptPassword(password, key).decode()
	cur.close()
	conn.close()
	print("The name is: "+name)
	print("The password is: "+password)

def showFunc(tableName):
	conn = sqlite3.connect(path+tableName+".db")
	cur = conn.cursor()
	cur.execute("SELECT NAME FROM PASSWORDLIST")
	
	for row in cur.fetchall():
		print(row[0])
	cur.close()
	conn.close()