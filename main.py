
import pyautogui
import random
import time

while True:
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(random.uniform(1, 3))
