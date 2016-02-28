from PIL import Image

def energy(pxls,x,y):
	e = 0
	try:
		e = ((pow(abs((pxls[(x-1),y][0]) - (pxls[(x+1),y][0])),2)) + (pow(abs((pxls[(x-1),y][1]) - (pxls[(x+1),y][1])),2)) + (pow(abs((pxls[(x-1),y][2]) - (pxls[(x+1),y][2])),2))) + ((pow(abs((pxls[x,(y+1)][0]) - (pxls[x,(y-1)][0])),2)) + (pow(abs((pxls[x,(y+1)][1]) - (pxls[x,(y-1)][1])),2)) + (pow(abs((pxls[x,(y+1)][2]) - (pxls[x,(y-1)][2])),2)))
	except Exception:
		pass
	return e

def getImage(filename):
	img = Image.open(filename)
	return img

def getPixels(img):
	pxls = img.load()
	return pxls

def saveEnergy(width,height,pxls):
	whole = []
	row = []
	for x in range(width):
		for y in range(height):
			en = energy(pxls,x,y)
			row.append(en)
			if(y == (height - 1)):
				whole.append(row)
				row = []
	return whole

def main():
	print("Starting Program...")
	img = getImage("images/lake.jpg")
	pxls = getPixels(img)
	width, height = img.size
	eMap = saveEnergy(width,height,pxls)
	print(eMap)

if __name__ == "__main__":
  main()

