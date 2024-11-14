#I didn't realize that the image was in Moodle, so I created it.
#import image and create an image
import image
img = image.EmptyImage(120,160)

#define colors
blue_pixel = image.Pixel(0, 0, 255)
black_pixel = image.Pixel(0, 0, 0)
red_pixel = image.Pixel(255, 0, 0)
green_pixel = image.Pixel(0, 255, 0)
orange_pixel = image.Pixel(255, 164, 0)
brown_pixel = image.Pixel(101, 67, 33)
purple_pixel = image.Pixel(159 ,32 ,240) 
yellow_pixel = image.Pixel(255, 255, 0)
white_pixel = image.Pixel(255, 255, 255)
skin_pixel = image.Pixel(232, 190, 172)

#user picks a color
color = input("What color would you like Mario's shirt and hat?")


#turns input color to defined color
if color == 'purple':
    color_pixel = purple_pixel
elif color == 'red':
    color_pixel = red_pixel
elif color == 'green':
    color_pixel = green_pixel
elif color == 'blue':
    color_pixel = blue_pixel
elif color == 'yellow':
    color_pixel = yellow_pixel   
elif color == 'orange':
    color_pixel = orange_pixel 

#creat background and make it white
for col in range(120):
    for row in range(160):
        img.setPixel(col, row, white_pixel)
win = image.ImageWin("white",120 , 160)

#creates mario
for col in range(30,90):
    for row in range(0,10):
        img.setPixel(col, row, color_pixel)
for col in range(20,110):
    for row in range(10,20):
        img.setPixel(col, row, color_pixel)
for col in range(20,50):
    for row in range(20,30):
        img.setPixel(col, row, brown_pixel) 
for col in range(50,70):
    for row in range(20,30):
        img.setPixel(col, row, skin_pixel)
for col in range(70,80):
    for row in range(20,30):
        img.setPixel(col, row, black_pixel)
for col in range(80,90):
    for row in range(20,30):
        img.setPixel(col, row, skin_pixel)    
for col in range(10,20):
    for row in range(30,40):
        img.setPixel(col, row, brown_pixel)
for col in range(20,30):
    for row in range(30,40):
        img.setPixel(col, row, skin_pixel)
for col in range(30,40):
    for row in range(30,40):
        img.setPixel(col, row, brown_pixel)
for col in range(40,70):
    for row in range(30,40):
        img.setPixel(col, row, skin_pixel)
for col in range(70,80):
    for row in range(30,40):
        img.setPixel(col, row, black_pixel)
for col in range(80,110):
    for row in range(30,40):
        img.setPixel(col, row, skin_pixel)
for col in range(10,20):
    for row in range(40,50):
        img.setPixel(col, row, brown_pixel)
for col in range(20,30):
    for row in range(40,50):
        img.setPixel(col, row, skin_pixel)
for col in range(30,50):
    for row in range(40,50):
        img.setPixel(col, row, brown_pixel)
for col in range(50,80):
    for row in range(40,50):
        img.setPixel(col, row, skin_pixel)
for col in range(80,90):
    for row in range(40,50):
        img.setPixel(col, row, black_pixel)
for col in range(90,120):
    for row in range(40,50):
        img.setPixel(col, row, skin_pixel)
for col in range(10,30):
    for row in range(50,60):
        img.setPixel(col, row, brown_pixel)  
for col in range(30,70):
    for row in range(50,60):
        img.setPixel(col, row, skin_pixel)
for col in range(70,110):
    for row in range(50,60):
        img.setPixel(col, row, black_pixel)
for col in range(30,100):
    for row in range(60,70):
        img.setPixel(col, row, skin_pixel)  
for col in range(20,40):
    for row in range(70,80):
        img.setPixel(col, row, color_pixel)
for col in range(40,50):
    for row in range(70,80):
        img.setPixel(col, row, blue_pixel)
for col in range(50,80):
    for row in range(70,80):
        img.setPixel(col, row, color_pixel)
for col in range(10,40):
    for row in range(80,90):
        img.setPixel(col, row, color_pixel)  
for col in range(40,50):
    for row in range(80,90):
        img.setPixel(col, row, blue_pixel)
for col in range(50,70):
    for row in range(80,90):
        img.setPixel(col, row, color_pixel)
for col in range(70,80):
    for row in range(80,90):
        img.setPixel(col, row, blue_pixel)
for col in range(80,110):
    for row in range(80,90):
        img.setPixel(col, row, color_pixel)  
for col in range(0,40):
    for row in range(90,100):
        img.setPixel(col, row, color_pixel)
for col in range(40,80):
    for row in range(90,100):
        img.setPixel(col, row, blue_pixel)
for col in range(80,120):
    for row in range(90,100):
        img.setPixel(col, row, color_pixel)
for col in range(0,20):
    for row in range(100,110):
        img.setPixel(col, row, skin_pixel)  
for col in range(20,30):
    for row in range(100,110):
        img.setPixel(col, row, color_pixel)
for col in range(30,40):
    for row in range(100,110):
        img.setPixel(col, row, blue_pixel)
for col in range(40,50):
    for row in range(100,110):
        img.setPixel(col, row, yellow_pixel)
for col in range(50,70):
    for row in range(100,110):
        img.setPixel(col, row, blue_pixel)  
for col in range(70,80):
    for row in range(100,110):
        img.setPixel(col, row, yellow_pixel)
for col in range(80,90):
    for row in range(100,110):
        img.setPixel(col, row, blue_pixel)
for col in range(90,100):
    for row in range(100,110):
        img.setPixel(col, row, color_pixel)
for col in range(100,120):
    for row in range(100,110):
        img.setPixel(col, row, skin_pixel)  
for col in range(0,30):
    for row in range(110,120):
        img.setPixel(col, row, skin_pixel)
for col in range(30,90):
    for row in range(110,120):
        img.setPixel(col, row, blue_pixel)
for col in range(90,120):
    for row in range(110,120):
        img.setPixel(col, row, skin_pixel)
for col in range(0,20):
    for row in range(120,130):
        img.setPixel(col, row, skin_pixel)  
for col in range(20,100):
    for row in range(120,130):
        img.setPixel(col, row, blue_pixel)
for col in range(100,120):
    for row in range(120,130):
        img.setPixel(col, row, skin_pixel)
for col in range(20,100):
    for row in range(130,140):
        img.setPixel(col, row, blue_pixel)        
for col in range(10,40):
    for row in range(140,150):
        img.setPixel(col, row, brown_pixel)  
for col in range(80,110):
    for row in range(140,150):
        img.setPixel(col, row, brown_pixel)
for col in range(0,40):
    for row in range(150,160):
        img.setPixel(col, row, brown_pixel)
for col in range(80,120):
    for row in range(150,160):
        img.setPixel(col, row, brown_pixel)

#draws image
img.draw(win)
win.exitonclick()
