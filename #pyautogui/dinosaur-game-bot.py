from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    dinoLimity = (250,432)#Coordenada Limite do Dino 192,421
    #x= 100 y=415


def restartGame():
    pyautogui.click(479, 410)
    pyautogui.keyDown('down')
    time.sleep(0.05)

    
def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.13)
    pyautogui.keyUp('space')
    #time.sleep(0.08)
    pyautogui.keyDown('down')

def imageGrab():
    box = (Cordinates.dinoLimity[0]+60,Cordinates.dinoLimity[1], Cordinates.dinoLimity[0]+100,Cordinates.dinoLimity[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():

    restartGame()
    while True:
     if(imageGrab()!= 447):
        pressSpace()
        #time.sleep(0.1)
main()
