from PIL import Image
def getImage(filename):
	img = Image.open(filename)
	return img

def getPixel(img,x,y):
	px = img.load()
	return px[x,y]

def strPixel(img,x,y):
	r,g,b = getPixel(img,x,y)
	return ("(" + str(r) + ", " + str(g) + ", " + str(b) + ")")

def main():
	print("Starting Program...")
	print(strPixel(getImage("images/lake.jpg"), 12, 18))

if __name__ == "__main__":
  main()
