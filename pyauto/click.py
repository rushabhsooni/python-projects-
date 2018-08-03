import pyautogui as ptg
import time
print(ptg.position())
'''ptg.moveTo(900,265)

ptg.press('down')'''
print(ptg.size())
ptg.click(901,294)
try:
    while True :
        #ptg.moveTo(901,320)
        #ptg.moveTo(905,265)

        pixeltrue = ptg.pixelMatchesColor(1237,344, (56,151,240))
        print(pixeltrue)
        if pixeltrue == True:

                ptg.moveTo(1237,344)
                ptg.click(1237,344)
                ptg.press('down')


        else:
            ptg.press('down')
            print("pixel not found")




        '''
        x, y = ptg.position()
        pixelColour = ptg.screenshot().getpixel((x,y))
        ss = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        ss += ' RGB: (' + str(pixelColour[0]).rjust(3)
        ss += ', ' + str(pixelColour[1]).rjust(3)
        ss += ', ' + str(pixelColour[2]).rjust(3) + ')'
        print(ss)
        '''


        #ptg.click(901,320)
        #ptg.press('down')
        time.sleep(1.0)
except KeyboardInterrupt:
    print("Done")
    


'''
try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        ss = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        ss += ' RGB: (' + str(pixelColor[0]).rjust(3)
        ss += ', ' + str(pixelColor[1]).rjust(3)
        ss += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print_no_newline(ss)
        time.sleep(1.0)
except KeyboardInterrupt:
    print("\nDone...")
'''