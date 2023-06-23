import os
from operating import RunWhenSet
from operating import CompileWhenSet

JC = ''
win_title = "POOL"
width = 500
high = 500
Ig = "pool.png"

def jre():
    os.system("sudo apt-get install default-jre >/dev/null 2>&1")
        
def jdk():
    os.system("sudo apt-get install default-jdk >/dev/null 2>&1")
    
def compilej():
    global JC
    os.system("javac "+JC)
        
def runj():
    global JC
    global win_title, w, h, Ig
    os.system("java "+JC+" "+win_title+" "+w+" "+h+" "+Ig)

class window:
    def open():
        global JC
        global win_title
        global w, h, Ig
        global width, high
        
        w = str(width)
        h = str(high)
        
        JC = "java/window.java"
    
        if RunWhenSet:
            runj()
        if CompileWhenSet:
            compilej()
            
    def SetTitle(title):
        global win_title
        win_title = title
        
    def SetSize(width,high):
        global win_title
        win_title = title
        
        w = str(width)
        h = str(high)
        
    def SetImage(img):
        global Ig
        Ig = img
        
    
        