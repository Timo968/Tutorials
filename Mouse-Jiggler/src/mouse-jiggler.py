import pyautogui
import time

while True:
    pyautogui.moveRel(50, 50, duration=1)
    pyautogui.moveRel(-50, -50, duration=1)
    time.sleep(1)