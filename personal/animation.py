import time
import random
from tkinter import *

WIDTH = 800
HEIGHT = 600

animation = Tk()
canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
animation.title('DVD')
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill = color)
        self.xSpeed = random.randrange(-10,20)
        self.ySpeed = random.randrange(-10,20)
    def move(self):
        canvas.move(self.shape, self.xSpeed, self.ySpeed)
        pos = canvas.coords(self.shape)
        if pos[3] >=600 or pos[1]<=0:
            self.ySpeed = -self.ySpeed
        if pos[2] >=800 or pos[0]<=0:
            self.xSpeed = -self.xSpeed

balls  = []
colours = ['red','green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
            'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

for x in range(100):
    balls.append(Ball(colours[random.randrange(0,11)],random.randrange(20,50)))

i = 1

while i > 0:
    for ball in balls:
        ball.move()
    animation.update()
    time.sleep(0.01)

animation.mainloop()