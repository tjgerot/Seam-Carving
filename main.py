from PIL import Image
def energy(pxls,x,y):
	cr,cg,cb = pxls[x,y]
	# (255,153,51)
	lr,lg,lb = pxls[(x-1),y]
	rr,rg,rb = pxls[(x+1),y]
	tr,tg,tb = pxls[x,(y+1)]
	br,bg,bb = pxls[x,(y-1)]

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
	energy(pxls,50,50)

if __name__ == "__main__":
  main()

