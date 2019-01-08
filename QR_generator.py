import pyqrcode as pq 

if __name__ == "__main__":

	text = input("Enter text to be encoded: ")

	qr = pq.create(text)

	print(qr.terminal()) #This should print the qr code to the terminal
