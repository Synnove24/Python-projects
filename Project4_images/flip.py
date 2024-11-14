#imports image and opens gif
import image
img = image.Image("cat.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())

#defines heigth and width
height = img.getHeight()
width = img.getWidth()

new = image.EmptyImage(width,height)    #creates empty image

for row in range(img.getHeight()):      #for loop for rows
    for col in range(img.getWidth()):   #for loop for columns
        p = img.getPixel(col, row)      #makes p a specific pixel
        

        new.setPixel(col, height - row - 1, p) #changes pixels to be in opposite locations

#draws the new image
new.draw(win)
win.exitonclick()
