from tkinter import *
from random import randint

tk = Tk()
canvas = Canvas(tk, width=800, height=500, bg='blue')
canvas.pack()

maxB = 10
genT = 1000

class Bub:
    number = 0
    clicked = 0

    def __init__(self):
        self.d = 40
        self.x = randint(2, 755)
        self.y = randint(2, 455)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        Bub.number += 1

        self.id = canvas.create_oval(self.x, self.y, self.x + self.d, self.y + self.d, fill='blue')
        canvas.tag_bind(self.id, '<Button-1>', self.on_click)
        self.move()

    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        pos = canvas.coords(self.id)
        if len(pos) > 0:
            if pos[0] < 2 or pos[2] > 798:
                self.dx = -self.dx
            if pos[1] < 2 or pos[3] > 498:
                self.dy = -self.dy
            tk.after(100, self.move)

    def on_click(self, event):
        canvas.delete(self.id)
        Bub.number -= 1
        Bub.clicked += 1
        tk.title(f'Клацнуто: {Bub.clicked}')

def play():
    if Bub.number < maxB:
        Bub()
        tk.after(genT, play)
    else:
        tk.title('Гру закінчено. Ваш результат: ' + str(Bub.clicked))

play()
tk.mainloop()