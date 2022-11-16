from PIL import Image, ImageDraw

img = Image.open("shape.png")

img = img.convert("RBG")

target_pixel = (420, 270)
target_color = (255, 255, 0)

ImageDraw.floodfill(img, target_pixel, target_color, thresh=0.5)

img.show()
