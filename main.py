#!/usr/bin/env python

import pyautogui
import Tkinter as tk
import sys
import pyscreeze
import pygame
import os


#Global Variables
screenWidth, screenHeight = pyautogui.size()
print screenHeight
print screenWidth

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self,master=None)
        self.grid()       
        self.master.minsize(width=200,height=100)   
        self.master.bind("<Key>", self.show)
        self.filename = "" 
        self.height = 0
        self.width =  0    
        self.listele = ()
        self.createWidjet()
              

    def quitFunc(self):
        sys.exit()

    def changeText(self):
        #update self.listele
        for files in os.listdir("./Elements"):            
            tempele = files.split(".png")
            filename = tempele[0].strip()            
            templist = list(self.listele)
            if(filename not in templist):
                templist.append(filename)
                self.listele = tuple(templist)
                
        
        # self.parentList.place(self.listele)
        menu = self.parentList["menu"]
        
        menu.delete(0, "end")
        for value  in self.listele:
            menu.add_command(label = value , command=lambda v=value:self.varele.set(v))
        
        ### This gets the currently selected item menu ####
        print self.varele.get()

        self.filename = self.inputEleName.get()        
        self.labelX.config(text="Values set : "+self.filename) 
        self.height =  self.inputHeight.get()
        self.width =  self.inputWidth.get()
             
        #self.master.iconify()
    
    def Reset(self):
        self.inputEleName.delete(0 , 'end')
        self.inputHeight.delete(0 , 'end')
        self.inputWidth.delete(0 , 'end')
    
    def Help(self):
        self.labelX.config(text = "Enter the component name. Then position mouse button on component and press space on keyboard")

    def Detect(self):
        #Check if an image can be detected
        testpos = pyautogui.locateOnScreen("./Elements/Audio.png");
        print testpos
        self.labelX.config(text = testpos)
        #click Test
        posx, posy = pyautogui.center(testpos)
        pyautogui.click(posx, posy)

    def createWidjet(self):
        self.quitButton=tk.Button(self, text='QUIT', command = self.quitFunc)
        self.quitButton.grid(row = 9, column = 4 )   
        self.quitButton=tk.Button(self, text='RESET', command = self.Reset)
        self.quitButton.grid(row = 9, column =  5 )  
        self.quitButton=tk.Button(self, text='HELP', command = self.Help)
        self.quitButton.grid(row = 9, column =  6 )
        self.detectButton=tk.Button(self, text='DetectTest', command = self.Detect)
        self.detectButton.grid(row = 13, column =  5 )                
        self.labelX=tk.Label(self, text="Welcome to input database creator")
        self.labelX.grid(row = 11,column = 5  )
        #The name of the Element
        self.labelName=tk.Label(self, text="Enter Component Name")
        self.labelName.grid(row = 3,column = 5  )
        self.inputEleName = tk.Entry(self, width = 20)
        self.inputEleName.grid(row = 4 , column = 5)

        #Get parent of element       
        print self.listele.__len__()
        if(len(self.listele) == 0 ) :
            self.varele = tk.StringVar(self)
            self.varele.set("Root")
            tempval = list(self.listele)
            tempval.insert(0,"Root")
            self.listele  = tuple(tempval)
        
        self.parentList = tk.OptionMenu(self, self.varele , tuple(self.listele))
        self.parentList.grid(row = 4 , column = 7)

        #The input Width
        self.labelName=tk.Label(self, text="Enter Component Width")
        self.labelName.grid(row = 5,column = 5  )
        self.inputWidth = tk.Entry(self, width = 20 )      
        self.inputWidth.grid(row = 6 , column = 5)
        # The input height
        self.labelHeight=tk.Label(self, text="Enter Component Height")
        self.labelHeight.grid(row = 7,column = 5  )
        self.inputHeight = tk.Entry(self, width = 20)
        self.inputHeight.grid(row = 8 , column = 5)
        self.changeText=tk.Button(self, text='Set Values', command = self.changeText)
        self.changeText.grid(row = 2, column = 5  )
    
    def show(self, event):      
        if(event.keysym == "space"):
            #Get mouse position 
            currentMouseX, currentMouseY = pyautogui.position()
            print(currentMouseX)
            print(currentMouseY)
            print "Done!!"
            offsetx=6
            offsety=6            
            #button Click 
            if(self.height != 0 and self.width != 0 ) :          
                im=pyautogui.screenshot(region=(currentMouseX-offsetx, currentMouseY-offsety, self.height , self.width ))
            else:
                im=pyautogui.screenshot(region=(currentMouseX-offsetx, currentMouseY-offsety, 20, 40))

            print self.filename
            if(self.filename != ""):
                 im.save(os.path.join("./Elements", self.filename+".png"))
            else:
                self.labelX.config(text = "Please enter the component name in the input box" )            
           
            #DONE
            self.labelX.config(text="DONE") 
            #pyautogui.click()

    
       

app =  Application()
app.master.title('Input Database creator')
app.mainloop()


