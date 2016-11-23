#input variables
inputFileName = "imageToChange.jpg" #the file to put a filter over (includes the file extension)
color1 = color(255, 0, 0) #the primary color
color2 = color(255, 255, 255) #the secondary color
name = "OutputImage" #the name of the new image (excluding file extension)
ext = "png" #file type that the new image should be
displacement = 250 #displacement of the top half of the image
maxDifference = 10 #maximum difference between pixels

sumCentre = 0
sumUp = 0
sumDown = 0
sumLeft = 0
sumRight = 0


def setup():
    size(1200, 1200)
    LoadImage() #load the image to change (which should be in the /data folder)
    

def LoadImage():
    global img
    img = loadImage(inputFileName)
    Decolor()
    

def Decolor():
    global img, maxDifference, sumCentre, sumUp, sumDown, sumLeft, sumRight
    img.loadPixels()
    image(img, 0, 0)
    edgeImg = createImage(img.width, img.height, RGB)
    loadPixels()
    for i in range(0, width * height):
        #reset the sums
        sumCentre = 0
        sumUp = 0
        sumDown = 0
        sumLeft = 0
        sumRight = 0
        
        #calculate the sums
        sumCentre = (red(pixels[i]) + green(pixels[i]) + blue(pixels[i])) / 3.0
        sumUp = (red(pixels[i - width]) + green(pixels[i - width]) + blue(pixels[i - width])) / 3.0
        sumLeft = (red(pixels[i - 1]) + green(pixels[i - 1]) + blue(pixels[i - 1])) / 3.0
        if(i + 1 < width * height):
            sumRight = (red(pixels[i + 1]) + green(pixels[i + 1]) + blue(pixels[i + 1])) / 3.0
        if(i + width < width * height):
            sumDown = (red(pixels[i + width]) + green(pixels[i + width]) + blue(pixels[i + width])) / 3.0
            
        
        #change color to red if the colors next to the pixel i are too different
        if(sumCentre - sumLeft < maxDifference):
            pixels[i - 1] = color(255, 0, 0)
        if(sumCentre - sumRight < maxDifference and i + 1 < width * height):
            pixels[i + 1] = color(255, 0, 0)
        if(sumCentre - sumUp < maxDifference): 
            pixels[i - width] = color(255, 0, 0)
        if(sumCentre - sumDown < maxDifference and i + width < width * height):
            pixels[i + width] = color(255, 0, 0)
        
            
        
        
    updatePixels()
    Recolour() #change the red pixels to another color (color1) and the other pixels to another color (color2)

def Recolour():
    global color1, color2, name, ext
    
    loadPixels()
    for i in range(0, width * height):
        if(pixels[i] != color(255, 0, 0)):
            pixels[i] = color1
        else:
            pixels[i] = color2 
        
    updatePixels()
    
    Displacement() #displaces the top half of the image by displacement amount of pixels
    

def Displacement():
    global name, ext
    tempInt = 0
    loadPixels()
    while tempInt < (width * height) / 2:
        tempInt += 1
        pixels[tempInt] = pixels[tempInt + displacement]
    updatePixels()
    
    SaveImage(name, ext) #saves the image to the folder
    
def SaveImage(fileName, extension):
    save(fileName + "." + extension)