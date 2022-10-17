import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time

def takeScreenshot():
    image = ImageGrab.grab().convert('L') #converting immage to black and white
    return image


if __name__ == "__main__":
    time.sleep(1)
    image = takeScreenshot()
    data = image.load()
    for i in range(300,615):
        for j in range(600, 705):
            data[i,j]=255
    for i in range(300,615):
        for j in range(300, 555):
            data[i,j]=0
    image.show()
