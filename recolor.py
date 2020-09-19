import time
from pyautogui import *
import pyautogui
import keyboard
import random
import win32api, win32con
import copy
import math
import pytesseract
import os.path

from PIL import Image

money = Image.open("money.png")
pixels = money.load()

width, height = money.size

print(width)
for a in range(0,width):
    for b in range(0,height):
        if pixels[a,b][0]  not in  range(200,256):
            pixels[a,b] = (0,0,0)
        else:
            pixels[a,b] = (255,255,255)
            

money.save("money.png")
