import tkinter as tk
from random import randint

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack()

class Ball:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+50, y+50, fill=color)
        self.dy = 2

    def ruh(self):
        pos = self.canvas.coords(self.id)
        if pos[1] > 348 or pos[1] < 2:
            self.dy = -self.dy
        self.canvas.move(self.id, 0, self.dy)

list_ball = []
colors = ['red', 'orange', 'yellow', 'green', 'blue']

for i in range(10):
    x = randint(10, 400)
    y = randint(10, 350)
    list_ball.append(Ball(canvas, x, y, colors[i % 5]))

def play():
    for ball in list_ball:
        ball.ruh()
    root.after(10, play)

play()
root.mainloop()