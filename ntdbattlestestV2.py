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
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


#red 255,26,26
#blue 0,168,255
#pink 255,120,166
#geen 61, 212, 0
#yellow 255,232,0
#white 255,255,255,255
#black 42,42,42
#lead 148,148,148
#zebra 56,56,56?
#rainbow 255, (240,255)

#This takes a PNG of the money and makes it black and white for reading
def recolor(a):
    money = Image.open("money.png")
    pixels = money.load()
    width, height = money.size
    for a in range(0,width):
        for b in range(0,height):
            if pixels[a,b][0]  not in  range(200,256):
                pixels[a,b] = (0,0,0)
            else:
                pixels[a,b] = (255,255,255)
    money.save("money.png")

#clicks x,y pixels
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def test(x,before = pyautogui.screenshot(region = (0,0,1920,1080)), panic = False, item = '1'):
    side = "Left"
    print(dats.homeside())
    time.sleep(2)
    try:
        if dats.homeside() == "Right":
            side = "Right"
    except:
        pass

    if side == "Left":
        click(400,200)
    else:
        click(1080-400,200)
    
    dist = 60
    #before = pyautogui.screenshot(region = (0,0,1920,1080))
    if dats.homeside() == "Left":
        tried = False
        while x > 0:
            pyautogui.moveTo(1200, 400)
            x = x -1
            width = random.randint(330,907)
            height = random.randint(75, 856)
            if panic == True and tried == False:
                tried == True
                
                try:
                    panicplace = dats.panicplace()
                    width = panicplace[0]
                    height = panicplace[1]
                except:
                    pass
            if width > 500:
                right = width + dist
            else:
                right = width - dist
            clean = before.getpixel((right, height))[0]
            
            pyautogui.press(item)
            pyautogui.moveTo(width, height)
            time.sleep(0.05)
            after = pyautogui.screenshot(region = (0,0,1920,1080))
            new = after.getpixel((right, height))[0]
            predgray = round((67/119)*clean - (81/119))
            print(clean, after, predgray)
            if predgray in range(new -10, new + 10):
                pyautogui.click(width,height)
                pyautogui.click(1200, 400)
                return(["DONE",(width, height)])
            
            else:
                pass
        return(["FAIL",0])
    else:
        tried = False
        print("RIGHT SIDE EXE")
        while x > 0:
            pyautogui.moveTo(120, 400)
            x = x -1
            width = random.randint(1000,1591)
            height = random.randint(75,856)
            if panic == True and tried == False:
                tried == True
                try:
                    panicplace = dats.panicplace()
                    width = panicplace[0]
                    height = panicplace[1]
                except:
                    pass

            if width < 1200:
                right = width + dist
            else:
                right = width - dist
            print(right, height)
            clean = before.getpixel((right, height))[0]
            
            pyautogui.press(item)
            pyautogui.moveTo(width, height)
            time.sleep(0.05)
            after = pyautogui.screenshot(region = (0,0,1920,1080))
            new = after.getpixel((right, height))[0]
            predgray = round((67/119)*clean - (81/119))
            print(clean, after, predgray)
            if predgray in range(new -10, new + 10):
                pyautogui.click(width,height)
                pyautogui.click(120, 400)
                return(["DONE",(width, height)])
            
            else:
                pass
        return(["FAIL",0])



def placetack(x,before):
    while x > 0:
        a = test(30,before)
        if a[0] == "DONE":
            x = x -1
        else:
            x = x -1

def tackpanic(x,before,panic):
    x = 1
    while x > 0:
        a = test(30,before,panic)
        if a[0] == "DONE":
            x = x -1
            try:
                if dats.homeside() == "Left":
                    # clicks building
                    pyautogui.click(a[1][0],a[1][1])

                    #upgrades it
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)

                    pyautogui.click(1300,400)
                    pyautogui.click(447,1001)
                    time.sleep(2)

                    #sells it
                    pyautogui.click(a[1][0],a[1][1])
                    pyautogui.click(695,943)
                else:
                    #clicks building
                    pyautogui.click(a[1][0],a[1][1])

                    #upgrades it 
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)
                    pyautogui.click(1546,956)

                    
                    #clears mouse, uses ability and sleeps
                    pyautogui.click(400,400)
                    pyautogui.click(1130,1011)
                    time.sleep(2)

                    #sells it
                    pyautogui.click(a[1][0],a[1][1])
                    pyautogui.click(756,954)
            except:
                pass
            

def pngtoint():
    hjhj = "money.png"
    try:
        zero = list(pyautogui.locateAll("zero.png", hjhj, confidence = 0.86))
        one = list(pyautogui.locateAll("one.png", "money.png", confidence = 0.85))
        two = list(pyautogui.locateAll("two.png", "money.png", confidence = 0.9))
        three = list(pyautogui.locateAll("three.png", "money.png", confidence = 0.82))
        four = list(pyautogui.locateAll("four.png", "money.png", confidence = 0.86))
        five = list(pyautogui.locateAll("five.png", "money.png", confidence = 0.88))
        six = list(pyautogui.locateAll("six.png", "money.png", confidence = 0.9))
        seven = list(pyautogui.locateAll("seven.png", "money.png", confidence = 0.86))
        eight = list(pyautogui.locateAll("eight.png", "money.png", confidence = 0.85))
        nine = list(pyautogui.locateAll("nine.png", "money.png", confidence = 0.88))


        number= []
        for x in zero:
            number.append((x[0],"0"))
        for x in one:
            number.append((x[0],"1"))
        for x in two:
            number.append((x[0],"2"))
        for x in three:
            number.append((x[0],"3"))
        for x in four:
            number.append((x[0],"4"))
        for x in five:
            number.append((x[0],"5"))
        for x in six:
            number.append((x[0],"6"))
        for x in seven:
            number.append((x[0],"7"))
        for x in eight:
            number.append((x[0],"8"))
        for x in nine:
            number.append((x[0],"9"))

        number.sort()
        final = []
        for x in number:
            final.append(x[1])

        final = "".join(final)
        final = int(final)
        return(final)
    except:
        return(-1)

class boarddata():
    def __init__(self):
        self.__board ="IDK"
        self.__wiz2 = ([0,0])
        try:
            a = (pyautogui.locateOnScreen("locked2.png",confidence = 0.4))[0]
            if a > 1000:
                self.__homeside = "Left"
            else:
                self.__homeside = "Right"
        except:
            try:
                a = (pyautogui.locateOnScreen("zach.png",confidence = 0.8))[0]
                if a < 1000:
                    self.__homeside = "Left"
                else:
                    self.__homeside = "Right"
            except:  
                self.__homeside = "Fail"
        if self.__homeside == "Left" or self.__homeside == "Right":
            if (type( (pyautogui.locateOnScreen("waterworks.png",confidence = 0.6)))) != type(None):
                self.__board = "waterworks"
                self.__panicplace = [1121,183]
                self.__panic = [1086,574]
                self.__panic2 = [0,0]
                self.__goodplacement = [1256,511]
                self.__enemy_Bloons = [1575,579]
                self.__default_Bloons = [1583, 383]
                self.__upgrade1 = [1201,591]
                self.__upgrade2 = [1077,461]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
                    
            elif (type( (pyautogui.locateOnScreen("islands.png",confidence = 0.8)))) != type(None) or (type( (pyautogui.locateOnScreen("islands2.png",confidence = 0.8)))) != type(None):
                self.__board = "islands"
                self.__panicplace = [1539,831]
                self.__panic = [1280,648]
                self.__panic2 = [0,0]
                self.__goodplacement = [1362,260]
                self.__enemy_Bloons = [1283,103]
                self.__default_Bloons = [1570,706]
                self.__upgrade1 = [1276,168]
                self.__upgrade2 = [1100,718]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
            elif (type( (pyautogui.locateOnScreen("yingyang.png",confidence = 0.8)))) != type(None):
                self.__board = "yingyang"
                self.__panicplace = [1301,362]
                self.__panic = [1143,99]
                self.__panic2 = [0,0]
                self.__goodplacement = [1271,713]
                self.__enemy_Bloons = [1410,726]
                self.__default_Bloons = [1325,691]
                self.__upgrade1 = [1010,240]
                self.__upgrade2 = [1338,122]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
            elif (type( (pyautogui.locateOnScreen("swamp.png",confidence = 0.8)))) != type(None):
                self.__board = "swamp"
                self.__panicplace = [1400,776]
                self.__panic = [1257,719]
                self.__panic2 = [0,0]
                self.__goodplacement = [1242,424]
                self.__enemy_Bloons = [1289,395]
                self.__default_Bloons = [1289,395]
                self.__upgrade1 = [1225,235]
                self.__upgrade2 = [1225,235]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
            elif (type( (pyautogui.locateOnScreen("yellowbrick.png",confidence = 0.8)))) != type(None):
                self.__board = "yellowbrick"
                self.__panicplace = [1150,178]
                self.__panic = [1457,521]
                self.__panic2 = [0,0]
                self.__goodplacement = [1311,403]
                self.__enemy_Bloons = [1555,305]
                self.__default_Bloons = [1555,305]
                self.__upgrade1 = [1176,496]
                self.__upgrade2 = [1176,496]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
            elif (type( (pyautogui.locateOnScreen("ally.png",confidence = 0.8)))) != type(None):
                self.__board = "ally"
                #NEEDS TO ADD PANICPLACE2
                self.__panic = [1318,470]
                self.__panic2 = [0,0]
                self.__goodplacement = [1400,430]
                self.__enemy_Bloons = [1040,709]
                self.__default_Bloons = [1486,148]
                self.__upgrade1 = [1116,438]
                self.__upgrade2 = [1306,582]
                if self.__homeside == "Left":
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
                
            elif (type( (pyautogui.locateOnScreen("cards.png",confidence = 0.8)))) != type(None):
                if self.__homeside == "Right":
                    self.__panicplace = [1053,136]
                    self.__board = "cards"
                    self.__panic = [1162,454]
                    self.__panic2 = [0,0]
                    self.__goodplacement = [1253,511]
                    self.__enemy_Bloons = [1465,267]
                    self.__default_Bloons = [1300,117]
                    self.__upgrade1 = [1140,684]
                    self.__upgrade2 = [1140,684]
                    
                else:
                    self.__board = "cards"
                    self.__panicplace = [868,157]
                    self.__panic = [775,459]
                    self.__panic2 = [0,0]
                    self.__goodplacement = [650,440]
                    self.__enemy_Bloons = [434,700]
                    self.__default_Bloons = [620,800]
                    self.__upgrade1 = [730,220]
                    self.__upgrade2 = [730,220]
                    
            elif (type( (pyautogui.locateOnScreen("longroundwater.png",confidence = 0.8)))) != type(None):
                self.__board = "longroundwater"
                
                self.__panicplace = [1530,817]
                self.__panic = [1444,568]
                self.__panic2 = [0,0]
                self.__goodplacement = [1132,248]
                self.__enemy_Bloons = [1056,200]
                self.__default_Bloons = [1056,200]
                self.__upgrade1 = [1338,350]
                self.__upgrade2 = [1338,350]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
                
            elif (type( (pyautogui.locateOnScreen("mine.png",confidence = 0.8)))) != type(None):
                self.__board = "mine"
                #NEED TO FIX NOT MIRRORED
                self.__panicplace = [1134,285]
                self.__panic = [1227,611]
                self.__panic2 = [0,0]
                self.__goodplacement = [1330,530]
                self.__enemy_Bloons = [1402,380]
                self.__default_Bloons = [1402,380]
                self.__upgrade1 = [1546,250]
                self.__upgrade2 = [1546,250]
                if self.__homeside == "Left":
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]

            elif (type( (pyautogui.locateOnScreen("mond.png",confidence = 0.8)))) != type(None):
                self.__board = "mond"
                self.__panicplace = [1523,810]
                self.__panic = [1429,668]
                self.__panic2 = [1155,228]
                self.__goodplacement = [1300,450]
                self.__enemy_Bloons = [1270,815]
                self.__default_Bloons = [1423,118]
                self.__upgrade1 = [1155,600]
                self.__upgrade2 = [1430,317]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
                
            elif (type( (pyautogui.locateOnScreen("pinball.png",confidence = 0.8)))) != type(None):
                self.__board = "pinball"
                self.__panicplace = [1542,823]
                self.__panic = [1197,521]
                self.__panic2 = [1444,521]
                self.__goodplacement = [1316,328]
                self.__enemy_Bloons = [1080,777]
                self.__default_Bloons = [1080,777]
                self.__upgrade1 = [1206,360]
                self.__upgrade2 = [1455,395]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__enemy_Bloons = [1920 -self.__enemy_Bloons[0],self.__enemy_Bloons[1]]
                    self.__default_Bloons = [1920 - self.__default_Bloons[0],self.__default_Bloons[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]

            elif (type( (pyautogui.locateOnScreen("river.png",confidence = 0.8)))) != type(None):
                self.__board = "river"
                self.__panicplace = [1544,819]
                self.__panic = [1090,464]
                self.__panic2 = [0,0]
                self.__goodplacement = [1252,250]
                self.__upgrade1 = [1090,344]
                self.__upgrade2 = [1100,537]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]

            elif (type( (pyautogui.locateOnScreen("treasure.png",confidence = 0.8)))) != type(None):
                self.__board = "treasure"
                self.__panicplace = [1257,233]
                self.__panic = [1125,368]
                self.__panic2 = [0,0]
                self.__goodplacement = [1172,436]
                self.__upgrade1 = [1232,368]
                self.__upgrade2 = [1044,462]
                if self.__homeside == "Left":
                    self.__panicplace = [683,266]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]

            elif (type( (pyautogui.locateOnScreen("wattle.png",confidence = 0.8)))) != type(None):
                self.__board = "wattle"
                self.__panicplace = [1545,823]
                self.__panic = [1168,636]
                self.__panic2 = [0,0]
                self.__goodplacement = [1255,629]
                self.__upgrade1 = [1265,363]
                self.__upgrade2 = [1265,363]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
                
            elif (type( (pyautogui.locateOnScreen("moon.png",confidence = 0.8)))) != type(None):
                self.__board = "moon"
                self.__panicplace = [832,809]
                self.__panic = [1187,441]
                self.__panic2 = [0,0]
                self.__goodplacement = [1413,587]
                self.__upgrade1 = [1123,449]
                self.__upgrade2 = [1318,520]
                if self.__homeside == "Left":
                    self.__panicplace = [1920-self.__panicplace[0],self.__panicplace[1]]
                    self.__panic = [1920-self.__panic[0], self.__panic[1]]
                    self.__panic2 = [1920-self.__panic2[0],self.__panic2[1]]
                    self.__goodplacement = [1920 -self.__goodplacement[0],self.__goodplacement[1]]
                    self.__upgrade1 = [1920 -self.__upgrade1[0],self.__upgrade1[1]]
                    self.__upgrade2 = [1920 - self.__upgrade2[0],self.__upgrade2[1]]
        else:
            self.__board = "IDK"
            self.__panic = [0,0]
            self.__panic2 = [0,0]
            self.__goodplacement = [0,0]
            self.__enemy_Bloons = [0,0]
            self.__default_Bloons = [0,0]
            self.__upgrade1 = [0,0]
            self.__upgrade2 = [0,0]
    def __str__(self):
        return (str([self.__board,self.__homeside]) )
    def homeside(self):
        return(self.__homeside)
    def boardmap(self):
        return(self.__board)
    def panicpos(self):
        return(self.__panicplace)
    def goodplacements(self):
        return self.__goodplacement
    def wiz2(self, x,y):
        self.__wiz2 = ([x,y])
        print(self.__wiz2, "SELF.__wiz2")
    def retwiz2(self):
        return self.__wiz2


def getpotpos(x):
    a = x %30
    b = x // 30
    return ( a,b)

def whatdef(x, before = pyautogui.screenshot(region = (0,0,1920,1080))):
    try:
        if x == 1:
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
            pyautogui.click(1278,956)
        elif x == 2:
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
            pyautogui.click(1278,956)
        elif x == 3:
            #place WIZ2
            abss = test(30, before, False, '2')
            print(abss[1])
            dats.wiz2(abss[1][0],abss[1][1])
            print("")
            print("")
            print(dats.retwiz2())
        elif x == 4:
            #Up wizz2 1,0
            print(dats.retwiz2())
            abss = dats.retwiz2()
            print(abss, "ABSS")
            pyautogui.click(abss[0],abss[1])
            pyautogui.click(1278,956)
        elif x == 5:
            #up wizz2 2,0
            abss = dats.retwiz2()
            pyautogui.click(abss[0],abss[1])
            pyautogui.click(1278,956)
        elif x == 6:
            #camo 4 both wiz
            abss = dats.retwiz2()
            pyautogui.click(abss[0],abss[1])
            pyautogui.click(1546,956)
            pyautogui.click(1546,956)
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
            pyautogui.click(1546,956)
            pyautogui.click(1546,956)
        elif x == 7:
            # fire wiz
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
            pyautogui.click(1546,956)
        else:
            pass
    except:
        pass
    
#tack, wiz, cobra

start = True
ab = True
timestart = time.time()
one = False
two = False
three = False
four = False
five = False
six = False
seven = False
while ab:
    timepassed = round(time.time()-timestart)
    shoulhavespent = timepassed* 26 + 1000
    
    if start == True:
        dats = boarddata()
        before = pyautogui.screenshot(region = (0,0,1920,1080))
        start = False
        timestart = time.time()

        print("failed to capture")
        
        
        if dats.homeside() == "Fail" or dats.boardmap() == "IDK":
            start = True
        else:
            print("TRIED TO PLACE WIZ")
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
            pyautogui.press('2')
            pyautogui.click(dats.goodplacements()[0],dats.goodplacements()[1])
    else:
        #dats = boarddata()
    
        

            
        #Gets the amount of money in integers
        try:
            iml1 = pyautogui.screenshot(region = (950,879,120,40))
            iml1.save(r"C:\Users\zacha\Desktop\btdbattles\money.png")
            recolor("money.png")
            money = pngtoint()
        except:
            money = -1
        
        print(money, dats.homeside(), dats.boardmap(),timepassed)
        if timepassed > 20 and one == False and money > 200:
            print("UP ONE")
            whatdef(1, before)
            one = True
        elif timepassed > 40 and two == False and money  > 1200:
            print("TWO UP")
            whatdef(2,before)
            two = True
        elif timepassed > 60 and three == False and money > 550:
            print("three UP")
            whatdef(3,before)
            three = True
        elif timepassed > 80 and four == False and money > 200:
            print("four UP1")
            whatdef(4,before)
            four = True
        elif timepassed > 100 and five == False and money > 1200:
            print("five UP")
            whatdef(5,before)
            five = True
        elif timepassed > 120 and six == False and money > 900:
            print("6 UP")
            whatdef(6,before)
            six = True
        elif timepassed > 300 and seven == False and money > 3000:
            whatdef(7,before)
            seven = True
        else:
            pass

        #blooneco
        if timepassed > 100 and money > 1500 and timepassed < 140:
            if dats.homeside() == "Left":
                click(1300,400)
                click(1360,920)
            else:
                click(400,400)
                click(566,920)

        #murder
        if timepassed > 220:
            if dats.homeside() == "Left":
                pyautogui.click(1500,400)
                pyautogui.click(1500,958)

                
                pyautogui.click(1573,1000)
                
                pyautogui.click(1371,986)
                pyautogui.click(1371,986)
                pyautogui.click(1371,986)
                pyautogui.click(1371,986)
                pyautogui.click(1371,986)
            else:
                pyautogui.click(400,400)
                #pyautogui.click(716,955)
                pyautogui.click(716,955)
                pyautogui.click(800,1000)
                pyautogui.click(660,993)
                pyautogui.click(660,993)
                pyautogui.click(660,993)
                pyautogui.click(660,993)
                pyautogui.click(660,993)
            time.sleep(5)
                
            
        #Panic system
        if keyboard.is_pressed('q') == True:
            #damage boost
            #pyautogui.click(883,100)

            #tackshooter ult
            tackpanic(2,before,True)
        if keyboard.is_pressed('t') == True:
            placetack(5,before)
                                          
            

