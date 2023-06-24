import pyautogui
import time


clickButtonX = 850
clickButtonY = 350
downArrowX = 955
downArrowY = 1030

refreshButtonX = 90
refreshButtonY = 57

numStartingDownArrows = 17 #the number of down arrows you need to click to get to the first coupon
numBetweenDownArrows = 20 #the number of down arrows you need to click to get to the next coupon
numClipsMax = 5

rangeMax = 69 #the number of clicks that are in the range
rangeVal = 10 #the distance between each click

for item in range(numStartingDownArrows): #this it down to get to the first coupon
    pyautogui.click(downArrowX, downArrowY)

pyautogui.click(refreshButtonX, refreshButtonY) #refreshes the page
time.sleep(1)
for j in range(rangeMax):
            pyautogui.click(clickButtonX, clickButtonY + rangeVal * j)