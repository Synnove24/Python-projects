#imports image and opens gif
import image
img = image.Image("cat.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())



for row in range(img.getHeight()):      #for loop for rows
    for col in range(img.getWidth()):   #for loop for columns
        p = img.getPixel(col, row)      #sets p to be a specific pixel

        newred = p.getRed()             #keeps red at a certain intensity and
        newgreen = 0                    #sets green and blue to 0
        newblue = 0

        newpixel = image.Pixel(newred, newgreen, newblue)   #creates new pixel

        img.setPixel(col, row, newpixel)

#draws the new image
img.draw(win)
win.exitonclick()
