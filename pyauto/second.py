import pyautogui as ptg
'''
import PIL as pl
import playsound as play
#setting fail safes
ptg.FAIL_SAFE=True
ptg.PAUSE=1
#moving the pointer to screen center
screenWidth, screenHeight = ptg.size()
ptg.moveTo(screenWidth / 2, screenHeight / 2)
ptg.click() #click!!
ptg.PAUSE = 10
#moving mouse like in staircase pattern
distance=20
for i in range(0,20):
 if i%2==0:
  ptg.moveRel(0,-distance,0.5)
 else :
  ptg.moveRel(distance,0,0.5)

#ptg.screenshot('foo.png')
#locaaion= ptg.locateOnScreen('start.png')

#locaaion=ptg.locateCenterOnScreen('click button.png')
#print(locaaion)
#print(locaaion.x)

#ptg.moveTo(locaaion)
#ptg.PAUSE = 5
#ptg.click(locaaion)

'''
for n in range(1,2):
    locaaion2 = ptg.locateCenterOnScreen('click button.png')
    print(locaaion2)
    ptg.moveTo(locaaion2)
    #ptg.click(locaaion2)
    #play.playsound('C:/Users/DAM/PycharmProjects/pyauto/1.mp3')
    #locaaion2 = ptg.locateCenterOnScreen('click button.png')
    #ptg.moveTo(locaaion2)
    #ptg.click(locaaion2)
    print(locaaion2)

    print(n)
    n=n+1
'''

#loccation3 = ptg.locateCentreOnScreen('click button.png', grayscale=True)
#loccation4 = ptg.locateCenterOnScreen('c1.png', grayscale=True)
#loccation5 = ptg.locateCenterOnScreen('c2.png', grayscale=True)
#loccation6 = ptg.locateCenterOnScreen('c3.png', grayscale=True)
#print(loccation4)
#ptg.moveTo(loccation4)
#ptg.click(loccation4)
#print(loccation5)
#ptg.moveTo(loccation5)
#ptg.click(loccation5)
#print(loccation6)
#ptg.moveTo(loccation6)
#ptg.click(loccation6)
#loccation7 = ptg.locateAllOnScreen('c1.png')

#ptg.screenshot('screen.png')
#print(loccation7)
#loccation8= ptg.locateOnScreen('c1.png')
#loccation9 = ptg.locateOnScreen('c2.png')
#print(loccation8)
#ptg.moveTo(544,459)
#ptg.moveTo(550,459)
#ptg.moveTo(600,700)
'''
ptg.moveRel(544,459,0.5)
ptg.moveTo(544,220)
ptg.moveTo(544,340)
ptg.moveTo(544,460)
ptg.moveTo(720,460)
ptg.moveTo(900,460)
'''
'''
loccation10 = ptg.locateCenterOnScreen('c4.png')
print(loccation10)
ptg.moveTo(loccation10)
ptg.click()
ptg.scroll(-50)
ptg.click()
ptg.scroll(-50)
ptg.click()
ptg.scroll(-50)
ptg.click()
ptg.scroll(-50)
ptg.click()
ptg.scroll(-50)
ptg.click()
ptg.scroll(-50)
'''
ptg.screenshot('screen2.png')
for n in range(1,10):
    #locaaion2 = ptg.locateCenterOnScreen('c5.png')
    #locaaion2 = ptg.locateCenterOnScreen('c4.png')
    #print(locaaion2)
    #ptg.moveTo(locaaion2)
    #ptg.click()
    ptg.scroll(-50)
    #load= ptg.locateCenterOnScreen('load.png',grayscale=True)
    #ptg.click(load)
    print(n)
    n=n+1
ptg.screenshot('screen2.png')
print(ptg.locateOnScreen('c5.png'))
print(ptg.locateAllOnScreen('c5.png'))
print(list(ptg.locateAllOnScreen('c5.png')))


#https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-scrolling


'''