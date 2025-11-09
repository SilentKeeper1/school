from tkinter import *

root = Tk()
root.title("Увага!")

label1 = Label(root, text="Дотримуйся часу роботи за комп'ютером!",
                height=3, bg='orange', fg='black', font='windows 24')
label1.pack()


label2 = Label(root, text='З турботою, твій брат :)',
                height=1, font='windows 16')
label2.pack()

root.mainloop()