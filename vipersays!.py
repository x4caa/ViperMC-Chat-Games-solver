from PIL import Image, ImageFilter
from numpy.core.fromnumeric import reshape
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import pytesseract
import cv2
from pytesseract import image_to_string
import numpy as np
import random
import pynput
from pynput.keyboard import Key, Controller
from dhooks.client import Webhook
from dhooks.file import File

#sleep so i can tab in
time.sleep(5)
print("now running")

#press esc to stop script
while not keyboard.is_pressed('esc'):
    start = pyautogui.locateOnScreen('vipersays.png', region=(8, 452, 947, 479), grayscale=True, confidence=0.90)
    if start is not None:
            timer1 = time.time()
            pyautogui.moveTo(start)
            time.sleep(0.1)
            #screenshot the chat when img is there
            iml = pyautogui.screenshot(region=(318, 452, 630, 479))
            iml.save('savedimage.png')
            #get only the tooltip
# Open image and make into Numpy array
            im = Image.open('savedimage.png').convert('RGB')
            na = np.array(im)
            orig = na.copy()   
            im = im.filter(ImageFilter.MedianFilter(3))
            pinkY, pinkX = np.where(np.all(na==[20,5,20],axis=2))
            top, bottom = pinkY[0], pinkY[-1]
            left, right = pinkX[0], pinkX[-1]


            ROI = orig[top:bottom, left:right]
            Image.fromarray(ROI).save('result.png')
            #img to text
            pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
            img = cv2.imread('result.png')
            img  = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            timer2 = time.time()
            print("timer started")
            sleep(random.uniform(1.3, 1.8))
            keyboard.write(pytesseract.image_to_string(img))
            print(f'Time for message to be sent: {time.time() - timer2} seconds')
            print(pytesseract.image_to_string(img))
            #webhook
            hook = Webhook("YOUR DISCORD WEBHOOK")
            success = pyautogui.locateOnScreen('success.png', region=(8, 452, 947, 479), grayscale=True, confidence=0.90)
            if success is not None:
                hook.send(f'```success, done in {time.time() - timer1} seconds```')
            else:
                hook.send("```unsuccessful```")
            #discord message with the string
            ##grab results file
            file = File('result.png', name='result.png')
            #send img to text and file
            hook.send(f'<@437049197905182730> {pytesseract.image_to_string(img)}', file=file)

            time.sleep(5)
            keyboard.press_and_release('enter')
            time.sleep(865)