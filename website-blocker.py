import datetime

blocked_websites = ['www.facebook.com','www.instagram.com','www.netflix.com','www.quora.com','www.youtube.com','www.linkedin.com']

file_path = "/etc/hosts"

local_host = "127.0.0.1"

def block():

	for website in blocked_websites:

		with open(file_path,'a') as f:
			clause = local_host+"	"+website+"\n"
			f.write(clause)

def unblock():

	with open(file_path,'r+') as f:
		lines = f.readlines()
		lines_to_delete = [local_host+"	"+site+"\n" for site in blocked_websites]
		f.seek(0)
		for line in lines:
			if line in lines_to_delete:
				pass
			else:
				f.write(line)
		f.truncate()

def block_checker():

	with open(file_path,'r') as f:
		lines = f.readlines()
		clause = local_host+"	"+blocked_websites[0]+"\n"
		if clause in lines:
			return True
		else:
			return False


if __name__ == "__main__":

	current_hour = datetime.datetime.now().hour
	if current_hour >=7 and current_hour<=20:

		if not block_checker():
			block()
	else:
		if block_checker():
			unblock()
