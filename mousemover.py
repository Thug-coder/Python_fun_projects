import pyautogui as pag
import random
import time


while True:
    x = random.randint(800, -1000)
    y = random.randint(400, -800)
    pag.move(x, y, 0.2)
    time.sleep(1)
