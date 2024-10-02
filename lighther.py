
import time
import keyboard
press_button=False

def press(e):
        
        global press_button
        press_button = True

while True:
        if press_button == False:
                print("red")
                time.sleep(3)

        else:
                print('green')
                time.sleep(3)
                press_button = False
        keyboard.hook(press)