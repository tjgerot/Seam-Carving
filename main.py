from PIL import Image
def energy(pxls,x,y):
	cr,cg,cb = pxls[x,y]
	lr,lg,lb = pxls[(x-1),y]
	rr,rg,rb = pxls[(x+1),y]
	tr,tg,tb = pxls[x,(y+1)]
	br,bg,bb = pxls[x,(y-1)]
	e = ((pow(abs(lr - rr),2)) + (pow(abs(lg - rg),2)) + (pow(abs(lb - rb),2))) + ((pow(abs(tr - br),2)) + (pow(abs(tg - bg),2)) + (pow(abs(tb - bb),2)))
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

