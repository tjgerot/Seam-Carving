from PIL import Image
def energy(pxls,x,y):
	cr,cg,cb = pxls[x,y]
	lr,lg,lb = pxls[(x-1),y]
	rr,rg,rb = pxls[(x+1),y]
	tr,tg,tb = pxls[x,(y+1)]
	br,bg,bb = pxls[x,(y-1)]
	e = ((pow(abs((pxls[(x-1),y][0]) - (pxls[(x+1),y][0])),2)) + (pow(abs((pxls[(x-1),y][1]) - (pxls[(x+1),y][1])),2)) + (pow(abs((pxls[(x-1),y][2]) - (pxls[(x+1),y][2])),2))) + ((pow(abs((pxls[x,(y+1)][0]) - (pxls[x,(y-1)][0])),2)) + (pow(abs((pxls[x,(y+1)][1]) - (pxls[x,(y-1)][1])),2)) + (pow(abs((pxls[x,(y+1)][2]) - (pxls[x,(y-1)][2])),2)))
	return e

def getImage(filename):
	img = Image.open(filename)
	return img

def getPixels(img):
	pxls = img.load()
	return pxls

def main():
	print("Starting Program...")
	img = getImage("images/lake.jpg")
	pxls = getPixels(img)
	print(energy(pxls,50,50))

if __name__ == "__main__":
  main()

