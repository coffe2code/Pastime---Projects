#!/usr/bin/env python3
import argparse
import table
import crypto

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("function")

	parser.add_argument("-t","--table", default="main")
	parser.add_argument("-p","--password")
	parser.add_argument("-n","--name")

	args = parser.parse_args()
	if(args.name != None):
		args.name = args.name.lower()

	if(args.function == "init"):
		table.initFunc(args.table)

	elif(args.function == "set"):
		if(args.name == None):
			print("ERROR: name required for set")
			return
		else:
			args.password = crypto.genPassword(12) if args.password==None else args.password
			table.setFunc(args.name, args.table, args.password)

	elif(args.function == "show"):
		table.showFunc(args.table)

	elif(args.function == "fetch"):
		if(args.name == None):
			print("ERROR: name required for fetch")
			return
		else:
			table.fetchFunc(args.table, args.name)


if __name__ == "__main__":
	main()