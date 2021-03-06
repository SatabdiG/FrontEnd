#!/usr/bin/env python

import pyautogui
import Tkinter as tk
import sys
import pyscreeze
import pygame
import os
from classes import Node, Graph
import termios
import tty



#Global Variables
childOffsetX = 20
screenWidth, screenHeight = pyautogui.size()
print screenHeight
print screenWidth

graphMaster = Graph()
parentRoot = Node(name = "Root")
graphMaster.addNode(parentRoot)

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

    #Updates values and creates the node tree structure    
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
        parentName = self.varele.get()     
       

        self.filename = self.inputEleName.get()        
        self.labelX.config(text="Values set : "+self.filename) 
        self.height =  self.inputHeight.get()
        self.width =  self.inputWidth.get()

         #create a node object
         #Rootlevel nodes
        if(parentName  == "Root"):
            newNode = Node(name = self.filename, parent = parentName)
            graphMaster.addNode(newNode)
        else:
            #find the node in the graph
            existNode = graphMaster.getNode(self.filename)
            if(existNode != "Not Found"):
                #create a new node append as children to existing Nodes
                newNode = Node(name = self.filename, parent = existNode)
                existNode.addChildren(newNode)
        
             
        #self.master.iconify()
    
    def Reset(self):
        self.inputEleName.delete(0 , 'end')
        self.inputHeight.delete(0 , 'end')
        self.inputWidth.delete(0 , 'end')
    
    def Help(self):
        self.labelX.config(text = "Enter the component name. Then position mouse button on component and press space on keyboard")

    def Detect(self):
        #Check if an image can be detected
        testpos = pyautogui.locateOnScreen("./Elements/Audio.png")
        print testpos
        self.labelX.config(text = testpos)
        #click Test
        posx, posy = pyautogui.center(testpos)
        pyautogui.click(posx, posy)        
        #get screen shot
        im=pyautogui.screenshot(region=(posx, posy+20, 40, 20))
        im.save("file.jpg")
        #View Current graph
        graphele = graphMaster.nodes
        for n1 in graphele:
            print "#name :" + n1.name 
            childNodes = n1.children
            for eachChild in childNodes:
                print "Chidren arw"
                print childNodes.name + " :  Parent : " + childNodes.parent.name

    def addChild(self):
        print "Clicked!!"
        #get Parent
        parentName = self.varele.get()  
        componentName = self.inputEleName.get()   
        print parentName
        ## get value as to the number of child
        childNum = int(self.inputNumChild.get())
        childNum += 1
        print childNum
        ### Locate parent Name in App and Click
        testpos = pyautogui.locateOnScreen("./Elements/"+parentName+".png")
        posx, posy = pyautogui.center(testpos)
        pyautogui.click(posx, posy)
        numOff = childNum*childOffsetX        
        ### Move mouse by childNum times current position
        newPosX = posx + int((childOffsetX)*childNum)
        ### Take Screen Shot With Name ###
        im=pyautogui.screenshot(region=(posx - 15, posy + numOff, 70, 20))
        im.save("./Elements/"+componentName+".png")





    def createWidjet(self):
        self.quitButton=tk.Button(self, text='QUIT', command = self.quitFunc)
        self.quitButton.grid(row = 9, column = 4 )   
        self.quitButton=tk.Button(self, text='RESET', command = self.Reset)
        self.quitButton.grid(row = 9, column =  5 )  
        self.quitButton=tk.Button(self, text='HELP', command = self.Help)
        self.quitButton.grid(row = 9, column =  6 )
        self.detectButton=tk.Button(self, text='DetectTest', command = self.Detect)
        self.detectButton.grid(row = 13, column =  5 ) 
        """ Add child """
        self.addChild=tk.Button(self, text='Add Child', command = self.addChild)
        self.addChild.grid(row = 16, column =  5 )
        """ State which number child """
        self.labelChild=tk.Label(self, text="Enter ChildNumber")
        self.labelChild.grid(row = 14,column = 5  )

        self.inputNumChild = tk.Entry(self , width = 30)
        self.inputNumChild.grid(row = 15, column = 5)

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
        # if(event.keysym == "Return"):
        #     self.master.iconify()              

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


# ######## Main Application Code #########
# while True:
#     os.system("stty raw -echo")
#     c = sys.stdin.read(1)
#     print ord(c)
#     if(ord(c) == 13):
#         ## Call the application Code
#         app.mainloop()
#     elif(ord(c) == 32):
#             ## capture Screen                    
#             #Get mouse position 
#             currentMouseX, currentMouseY = pyautogui.position()
#             print(currentMouseX)
#             print(currentMouseY)
#             print "Done!!"
#             offsetx=6
#             offsety=6          
           
           
#             im=pyautogui.screenshot(region=(currentMouseX-offsetx, currentMouseY-offsety, 20, 40))            
#             im.save(os.path.join("./Elements/test.png"))
#     elif(ord(c) == 113):
#         sys.exit()


#     os.system("stty -raw echo")