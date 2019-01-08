import cv2


if __name__ == "__main__":

	image_path = input("Enter path of encoded image: ")
	image = cv2.imread(image_path)

	start_width = 0
	start_height = 0

	while start_height < image.shape[0]:
		
		start_width = 0
		while start_width < image.shape[1]:
			total = image[start_height][start_width][0]+image[start_height][start_width][1]+image[start_height][start_width][2]
			#Odd means Black, Even means white

			if total%2==0:
				image[start_height][start_width][0] = 255
				image[start_height][start_width][1] = 255
				image[start_height][start_width][2] = 255
			else:
				image[start_height][start_width][0] = 0
				image[start_height][start_width][1] = 0
				image[start_height][start_width][2] = 0

			start_width+=1
		start_height+=1

	cv2.imwrite("decoded.png",image)
