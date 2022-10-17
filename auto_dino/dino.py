import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def takeScreenshot():
    image = ImageGrab.grab().convert('L') # capturing image and converting image to black and white
    return image

def hit(key):
    pyautogui.keyDown(key)

def isCollideCactus(data): # checks for cactus
    for i in range(300,700): # x direction of black box created
        for j in range(600, 705): # y direction of black box created
            if data[i, j] > 150: #150 becaause it denotes white colour because of dark theme, choose < 100 for black colour in light theme
                return True
    return False

if __name__ == "__main__":
    print("Hey Dino Game starts in 3 sseconds")
    time.sleep(3)
    hit("up")
    while True:
        image = takeScreenshot()
        data = image.load()
        if isCollideCactus(data): #checks if cactus is in place for jump or not
            hit('up')
        #print (asarray(image))
        #for i in range(300,415):
         #   for j in range(600, 650):
          #      data[i,j]=0
        #image.show()
