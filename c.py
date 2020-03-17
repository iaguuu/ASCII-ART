import sys
from PIL import Image

image_path = sys.argv[0]
img = Image.open("f6fed15a-8175-4875-b9d9-a64910d33b70.png")


width, height = img.size
aspect_ratio = height/width
newWidth = 120
newHeight = aspect_ratio * newWidth * 0.55
img = img.resize((newWidth, int(newHeight)))

img = img.convert('L')
pixels = img.getdata()

chars = ["B","S","#","&","@","$","%","*","!",":","."]
newPixels = [chars[pixel//25] for pixel in pixels]
newPixels = ''.join(newPixels)

newPixelsCount = len(newPixels)
asciiArt = [newPixels[index:index + newWidth] for index in range(0, newPixelsCount, newWidth)]
asciiArt = "\n".join(asciiArt)
print(asciiArt)
