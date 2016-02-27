from PIL import Image
def main():
	print("Starting Program...")
	def getPixel(x,y):
		img = Image.open("images/lake.jpg")
		px = img.load()
		r,g,b = px[x,y]
		return (str(r) + "," + str(g) + "," + str(b))
	#height = Images.getHeight();
	#width = Images.getWidth();
	print(getPixel(5,88))
if __name__ == "__main__":
  main()
