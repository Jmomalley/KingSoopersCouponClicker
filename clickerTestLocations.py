import pyautogui
import time


clickButtonX = 850
clickButtonY = 1000
downArrowX = 955
downArrowY = 1030


for item in range(3):
    pyautogui.click(downArrowX, downArrowY)


pyautogui.click(clickButtonX, clickButtonY)
time.sleep(0.25)