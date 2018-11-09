import smtplib
import getpass
import imapclient
import imaplib
import pprint

answer = input("Type S for sending an email or U for checking updates: ")
print("Email being sent from Gmail....")


EmailAddress = input("Enter Email: ")
Password = getpass.getpass("Enter Password: ")


if answer=='S' or answer=='s':
	#print("Email being sent from Gmail....")


	#EmailAddress = input("Enter Email: ")
	#Password = getpass.getpass("Enter Password: ")
	print("Connecting to gmail......")
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	request = server.ehlo()
	login = server.login(EmailAddress,Password)
	
	print(login)

	Recepient = input('Enter recepient address: ')
	Subject = input('Enter Subject: ')
	Body = input('Enter body: ')

	server.sendmail(EmailAddress,Recepient,'Subject: '+Subject+'\n'+Body)
	print("Email Sent")
else:
	print("Fetching Updates....")
	imaplib._MAXLINE = 10000000
	
	imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
	imapObj.login(EmailAddress,Password)
	imapObj.select_folder('INBOX',readonly=True)
	UIDs = imapObj.search(['UNSEEN'])
	rawMessages = imapObj.fetch(UIDs,['BODY[]'])