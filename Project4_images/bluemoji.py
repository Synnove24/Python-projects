#import image and create an image
import image
img = image.EmptyImage(50,50)
#define colors
blue_pixel = image.Pixel(0, 0, 255)
black_pixel = image.Pixel(0, 0, 0)
red_pixel = image.Pixel(255, 0, 0)
#creat background and make it blue
for col in range(50):
    for row in range(50):
        img.setPixel(col, row, blue_pixel)
win = image.ImageWin("blue",50, 50)
#create mouth
for col in range(10,40):
    for row in range(34,40):
        img.setPixel(col, row, red_pixel)

#create left eye
for col in range(8,22):
    for row in range(8,22):
        img.setPixel(col, row, black_pixel)

#create right eye
for col in range(28,42):
    for row in range(8,22):
        img.setPixel(col, row, black_pixel)

#draw image
img.draw(win)
win.exitonclick()
    
