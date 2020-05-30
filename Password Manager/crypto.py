import random
from cryptography.fernet import Fernet

path = "/home/beowulf/Passwords/"

def genPassword(length):
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
				'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
				'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
				'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
				'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	symbols = ['@', '#', '$', '%', '?']

	combinedList = digits+lowerCase+upperCase+symbols

	tempPass = random.choice(digits)+random.choice(lowerCase)+random.choice(upperCase)+random.choice(symbols)

	for x in range(length-4):
		tempPass += random.choice(combinedList)

	password = list(tempPass)
	random.shuffle(password)
	password = ''.join(password)
	return password

def keyGen(table):
	key = Fernet.generate_key()
	file = open(path+table+".key", 'wb')
	file.write(key)
	file.close()

def readKey(table):
	file = open(path+table+".key", "rb")
	key = file.read()
	file.close()
	return key

def encryptPassword(password, key):
	password = password.encode()
	f = Fernet(key)
	encrypted = f.encrypt(password)
	return encrypted

def decryptPassword(password, key):
	f = Fernet(key)
	decrypted = f.decrypt(password)
	return decrypted