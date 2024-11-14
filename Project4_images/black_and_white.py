#imports image and brings in the gif
import image
img = image.Image("cat.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())


#changes pixels to black and white
for row in range(img.getHeight()):      #for loop for rows
    for col in range(img.getWidth()):   #for loop for columms
        p = img.getPixel(col, row)      #sets p to be a specific pixel

        a = int((p[0]+p[1]+p[2])/3)     #makes each color the same without changing intensity

        newpixel = image.Pixel(a, a, a) #makes new gray pixel

        img.setPixel(col, row, newpixel) #sets the pixel to the correct spot

#creates image
img.draw(win)
win.exitonclick()
