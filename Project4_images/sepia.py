
#imports image and opens gif
import image
img = image.Image("cat.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())



for row in range(img.getHeight()):      #for loop for rows
    for col in range(img.getWidth()):   #for loop for columns
        p = img.getPixel(col, row)      #makes p a specific pixel

       # creates new red keeping it below 255
        newred = int((p.getRed() * .393) + (p.getGreen() * .769) + (p.getBlue() * .189))
        if newred > 255:
            newred = 255
       # creates new green keeping it below 255     
        newgreen = int((p.getRed() * .349) + (p.getGreen() * .686) + (p.getBlue() * .168))
        if newgreen > 255:
            newgreen = 255
       # creates new blue keeping it below 255     
        newblue = int((p.getRed() * .272) + (p.getGreen() * .534) + (p.getBlue() * .131))
        if newblue > 255:
            newblue = 255
        

        newpixel = image.Pixel(newred, newgreen, newblue)   #creates new pixel

        img.setPixel(col, row, newpixel)

#draws the new image
img.draw(win)
win.exitonclick()
