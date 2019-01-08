import png
import pyqrcode as pq
import cv2
import numpy as np


def QR_Code_Generator():
	text = input("Enter text to be encoded: ")
	qr = pq.create(text)
	qr.png("QR.png",scale=15)

def Steganographer(imagepath):
	qr = cv2.imread("QR.png")
	image = cv2.imread(imagepath)

	if(qr.shape[0]>image.shape[0] or qr.shape[1]>image.shape[1]):
		print("Unable to hide as sample image is too small")
	else:
		width_index = 0
		height_index = 0

		while width_index < qr.shape[0]:
			height_index=0
			while height_index < qr.shape[1]:
				#Black needs to have odd total, White needs to have even total
				total = np.sum(image[width_index][height_index])
				if qr[width_index][height_index][0] == 0:
					#Black
					if total%2 == 0:
						if(image[width_index][height_index][0]>0):
							image[width_index][height_index][0]-=1
						elif(image[width_index][height_index][1]>0):
							image[width_index][height_index][1]-=1
						elif(image[width_index][height_index][2]>0):
							image[width_index][height_index][2]-=1
						else:
							image[width_index][height_index][0]+=1;

				else:
					#White
					if total%2 != 0:
						if(image[width_index][height_index][0]>0):
							image[width_index][height_index][0]-=1
						elif(image[width_index][height_index][1]>0):
							image[width_index][height_index][1]-=1
						elif(image[width_index][height_index][2]>0):
							image[width_index][height_index][2]-=1
						else:
							image[width_index][height_index][0]+=1;
				height_index+=1
			width_index+=1

		cv2.imwrite("encoded.png",image)


if __name__ == "__main__":
	
	QR_Code_Generator()
	imagepath = input("Enter image path: ")
	Steganographer(imagepath)

