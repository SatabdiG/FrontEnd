#!/usr/bin/env python
import os , sys
import cv2


while True:
    os.system("stty raw -echo")
    c = sys.stdin.read(1)
    print ord(c)
    if(ord(c) == 32):
        break
    os.system("stty -raw echo")