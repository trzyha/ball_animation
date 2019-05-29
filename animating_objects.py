import tkinter
import random
import time

WIDTH = 800
HEIGHT = 600


tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Animating circles")
canvas.pack()

class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(1, 1, 60, 60, fill = "orange")
        self.xspeed = 4
        self.yspeed = 5
    
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos [3] >= HEIGHT or pos [1] <=0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos [0] <= 0:
            self.xspeed = -self.xspeed

newball = Ball()
#newball2 = Ball()

while 1:
    newball.move()
    #newball2.move()
    tk.update()
    time.sleep(0.01)

    tk.mainloop()