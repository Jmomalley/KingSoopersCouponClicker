import pyautogui
import time

#(across, down)
#important locations
#(850, 1010) - clip button
#(955, 1030) - down arrow
# pyautogui.click(850, 980)

clickButtonX = 850
clickButtonY = 350
downArrowX = 955
downArrowY = 1030
refreshButtonX = 90
refreshButtonY = 57

numStartingDownArrows = 20 #the number of down arrows you need to click to get to the first coupon
numBetweenDownArrows = 20 #the number of down arrows you need to click to get to the next coupon
numClipsMax = 5

numCouponsGetting = 1 #the number of coupons you want to get in a single run
#numRuns = 5 #the number of times you want to run the program
numRuns = 1 #the number of times you want to run the program

rangeMax = 69 #the number of clicks that are in the range
rangeVal = 10 #the distance between each click

numClips = 0

for item in range(numStartingDownArrows): #this it down to get to the first coupon
    pyautogui.click(downArrowX, downArrowY)

for k in range(numRuns): #this is the number of times you want to run the program
    pyautogui.click(refreshButtonX, refreshButtonY) #refreshes the page



    for j in range(rangeMax):
            pyautogui.click(clickButtonX, clickButtonY + rangeVal * j)

    for i in range(numBetweenDownArrows): #clicks the down arrow 6 times to get to the next coupon
            pyautogui.click(downArrowX, downArrowY)

        # if numClips == numClipsMax: #helps to stop the precession of the coupons up the page
        #     pyautogui.click(downArrowX,downArrowY)
        #     pyautogui.click(downArrowX,downArrowY)
        #     numClips = 0
        # else:
        #     numClips += 1
    
