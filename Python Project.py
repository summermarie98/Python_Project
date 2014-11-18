# Hello world

from Tkinter import *
root =Tk()
    
drawpad = Canvas(root, width=800,height=600, background = 'white')
player = drawpad.create_rectangle(390,580,410,600, fill="pink")
player2 = drawpad.create_rectangle(390,10,410,30, fill="orange")

class myApp(object):
    def __init__(self,parent):
        
        global drawpad
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
         
        drawpad.pack()
        root.bind_all("<Key>", self.key)
        
        
    def key(self,event):
        global player
        global rocket1Fired
        global drawpad
        #rocketHit = self.collisionDetect()
        px1,py1,px2,py2 = drawpad.coords(player)
        if event.char == "w" and py1>0: #and rocketHit==False:
            drawpad.move(player,0,-4)
            if rocket1Fired== False:
                drawpad.move(rocket1,0,-4)
        elif event.char == "a" and px1>=0: #and rocketHit==False:
            drawpad.move(player,-4,0)
            if rocket1Fired== False:
                drawpad.move(rocket1,-4,0)
        elif event.char == "d" and px2<=800: #and rocketHit==False:
            drawpad.move(player,4,0)
            if rocket1Fired== False:
                drawpad.move(rocket1,4,0)
        elif event.char == "s" and py2<600: #and rocketHit==False:
            drawpad.move(player,0,4)
            if rocket1Fired== False:
                drawpad.move(rocket1,0,4)
        if event.char == " ":
            rocket1Fired = True
            self.rockets= (self.rockets-1)
            self.rocketsTxt.configure(text=self.rockets)
            
        
        
        
        
        
        
        
        
app = myApp(root)
root.mainloop()