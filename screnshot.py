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


time.sleep(5)
fullscreen = (pyautogui.screenshot(region = (0,0,1920,1080)))
a = random.randint(0,1000000)


fullscreen.save(r"C:\Users\zacha\Desktop\fullscreenbtd\super.png")

