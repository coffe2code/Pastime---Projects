from bs4 import BeautifulSoup
import cv2
import requests
import shutil
import random
import os

class LinkGenerator(object):

	downloadedList = []
	
	toDownloadList = []

	links = []

	def __init__(self):

		self.baseLink = "https://xkcd.com/"
		self.max = 2066
		self.loadList()
		self.createRandomList()
		self.linkCreator()
		self.writer()

	@classmethod
	def loadList(cls):
		with open("numberList.txt",'r') as f:
			for line in f:
				LinkGenerator.downloadedList.append(int(line))

	
	def createRandomList(self):
		counter = 0

		while counter<5:
			temp = random.randint(1,self.max)
			if(temp in LinkGenerator.downloadedList) or (temp in LinkGenerator.toDownloadList):
				pass
			else:
				LinkGenerator.toDownloadList.append(temp)
				counter+=1

		

	
	def linkCreator(self):
		counter = 0
		for item in LinkGenerator.toDownloadList:
			LinkGenerator.links.append(self.baseLink+str(LinkGenerator.toDownloadList[counter]))
			counter+=1

	@classmethod
	def writer(cls):
		with open("numberList.txt",'a') as f:
			for item in LinkGenerator.toDownloadList:
				f.write(str(item) + '\n')

class Downloader(LinkGenerator):

	pageContent = []
	imageData = []
	imagePaths = []

	def __init__(self):
		super(Downloader,self).__init__()
		self.getPageContent()
		self.imageData()


	@classmethod
	def getPageContent(cls):
		for link in Downloader.links:
			Downloader.pageContent.append(requests.get(link))

	@classmethod
	def imageData(cls):
		for item in Downloader.pageContent:
			souped = BeautifulSoup(item.content,"html.parser")
			image_link = souped.find(id = "middleContainer").find("img")["src"]
			image = requests.get("http:"+image_link,stream=True)

			Downloader.imagePaths.append(os.getcwd()+"/imageRepository/"+image_link[29:])
			
			with open(os.getcwd()+"/imageRepository/"+image_link[29:],'wb') as out_file:
				shutil.copyfileobj(image.raw,out_file)
			del image

	def view(self):
		counter = 1
		for item in self.imagePaths:
			image = cv2.imread(item)
			cv2.imshow(str(counter),image)
			cv2.waitKey(0)
			counter+=1



if __name__ == "__main__":


	downloadxkcd = Downloader()
	downloadxkcd.view()

#x = Downloader()

#print(x.downloadedList)


#page = requests.get("https://xkcd.com/235/")

#page_souped = BeautifulSoup(page.content,"html.parser")

#image_link = page_souped.find(id = "middleContainer" ).find("img")["src"]

#image = requests.get("http:"+image_link,stream=True)

#with open('image','wb') as out_file:
#	shutil.copyfileobj(image.raw,out_file)

#del image

