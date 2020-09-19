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

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def test(x,before = pyautogui.screenshot(region = (0,0,1920,1080))):
    click(400,200)
    dist = 60
    #before = pyautogui.screenshot(region = (0,0,1920,1080))
    while x > 0:
        pyautogui.moveTo(1200, 400)
        x = x -1
        width = random.randint(350,875)
        height = random.randint(100, 770)
        right = width + dist
        clean = before.getpixel((right, height))[0]
        
        pyautogui.press('1')
        pyautogui.moveTo(width, height)
        time.sleep(0.005)
        after = pyautogui.screenshot(region = (0,0,1920,1080))
        new = after.getpixel((right, height))[0]
        predgray = round((67/119)*clean - (81/119))
        
        if predgray in range(new -10, new + 10):
            pyautogui.click(width,height)
            pyautogui.click(1200, 400)
            return("DONE")
        
        else:
            pass
    return("FAIL")

def tackpanic(x):
    while x > 0:
        if test(30) == "DONE":
            x = x -1


go(10)
