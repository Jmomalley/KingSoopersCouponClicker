import pyautogui
import time

#(across, down)
#important locations
#(850, 1010) - clip button
#(955, 1030) - down arrow
# pyautogui.click(850, 980)

clickButtonX = 850
clickButtonY = 950
downArrowX = 955
downArrowY = 1030
numClipsMax = 5

numCouponsGetting = 150

rangeMax = 9 #the number of clicks that are in the range
rangeVal = 10 #the distance between each click

numClips = 0

for item in range(3): #this it down to get to the first coupon
    pyautogui.click(downArrowX, downArrowY)

for i in range(20):

    for j in range(rangeMax):
        pyautogui.click(clickButtonX, clickButtonY + rangeVal * j)

        #time.sleep(0.25)
    for i in range(6):
        pyautogui.click(downArrowX, downArrowY)
    if numClips == numClipsMax:
        pyautogui.click(downArrowX,downArrowY)
        pyautogui.click(downArrowX,downArrowY)
        numClips = 0
    else:
        numClips += 1

# pyautogui.click(clickButtonX, clickButtonY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)

# pyautogui.click(clickButtonX, clickButtonY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)

# pyautogui.click(clickButtonX, clickButtonY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)
# pyautogui.click(downArrowX, downArrowY)

# time.sleep(0.5)
# pyautogui.click(clickButtonX, clickButtonY)