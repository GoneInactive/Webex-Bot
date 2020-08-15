## Webex Bot

## Imports

import pyautogui as cb
import json

## END Imports


## NOTE: CTRL+ALT+DEL <-- SHUTDOWN PROGRAM
## NOTE: cb.PAUSE() to pause program


def main():
    ##
    ##  Main Method
    ##
    print("Starting Program")

    value = input("What Day Is It TMR? ")
    print(pick_class(value))

    # Assign Fail Safe & Pause
    cb.PAUSE = 1
    cb.FAILSAFE = True
    # END

    # Size the Screen
    width, height = cb.size()
    # END

    open_webex()


#########################################
##
##  Operation Functions
##
#########################################

def open_webex(url):
    ##
    ##  Open_Webex Method
    ##
    cb.moveTo(57, 1055)  # <-- Move's mouse to Search Bar
    cb.click()

    cb.countdown(2)

    cb.moveTo(108, 1008)
    cb.click()

    cb.countdown(2)

    cb.typewrite('webex')

    cb.countdown(1)

    cb.typewrite(['enter'])

    cb.countdown(2)

    cb.moveTo(1294, 338)
    cb.click()
    cb.countdown(2)

    cb.typewrite(url)
    print("TYPED")
    cb.countdown(5)

    cb.moveTo(1370, 334)
    cb.click()
    cb.countdown(5)

    cb.moveTo(1007, 700)
    cb.click()
    cb.countdown(15)

    cb.moveTo(700, 569)
    cb.click()
    cb.countdown(5)

    cb.moveTo(780, 994) # chat button
    cb.click()
    cb.countdown(5)

    cb.moveTo(1560, 963)
    cb.click()
    cb.countdown(5)

    cb.moveTo(1527, 989)
    cb.click()
    cb.countdown(5)

    cb.moveTo(1527, 989)
    cb.click()
    cb.countdown(5)

    for i in range(100):
        cb.typewrite("Hello Mr. Rice, How Are YOU?")
        cb.typewrite(['enter'])



    print("-------------------------------------------------------------")
    print("Done")


def pick_class(val):
    ##
    ##  pick school class method
    ##
    print("Finding Class")

    contents = open('class_pick.json').read()
    load_classes = json.loads(contents)


    if val == 'A':
        classes = load_classes['Block 1'], load_classes['Block 2'], load_classes['Block 3'], load_classes['Block 4']
        return classes
    elif val == 'B':
        classes = load_classes['Block 5'], load_classes['Block 6'], load_classes['Block 7'], load_classes['Block 8']
        return classes
    else:
        return 'Error'


def start_class():
    open_webex('https://meetingsamer30.webex.com/meet/pr1266298228')


# No EDIT __NAME__

if __name__ == '__main__':
    main()

# NO CODE PAST THIS POINT <-- -->