#!/usr/bin/env python
# import os , sys
# import cv2
# import pyautogui

# while True:
#     os.system("stty raw -echo")
#     c = sys.stdin.read(1)
#     print ord(c)
#     if(ord(c) == 32):
#         break
#     elif (ord(c) == 13):
#         currentMouseX, currentMouseY = pyautogui.position()
#         print(currentMouseX)
#         print(currentMouseY)
        
#     os.system("stty -raw echo")

import Xlib
import Xlib.display

def main():
    display = Xlib.display.Display(':0')
    root = display.screen().root
    root.change_attributes(event_mask=
        Xlib.X.ButtonPressMask | Xlib.X.ButtonReleaseMask)

    while True:
        event = root.display.next_event()
        print event

if __name__ == "__main__":
    main()
