#Вправа 1
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

# Вправа 2

# from tkinter import *


# root = Tk()
# root.title("Планування родини")
# root.geometry("480x220")
# root.config(bg="#FFD580") 


# label1 = Label(root,
#                text="Канікули завершуються 14 січня!",
#                font=("Arial Rounded MT Bold", 22),
#                bg="#FFD580",
#                fg="#B22222",
#                pady=20)
# label1.pack()

# label2 = Label(root,
#                text="Пора готуватись до навчання",
#                font=("Segoe UI", 14),
#                bg="#FFD580",
#                fg="#333333")
# label2.pack()

# button = Button(root,
#                 text="Окей, зрозумів",
#                 font=("Calibri", 14, "bold"),
#                 bg="#FF8C00",
#                 fg="white",
#                 width=20,
#                 height=2,
#                 command=root.destroy)
# button.pack(pady=20)

# root.mainloop()

# Вправа 3

# from tkinter import *
# import calendar
# from datetime import datetime


# root = Tk()
# root.title("Календар")
# root.geometry("400x350")
# root.config(bg="#F0F8FF") 


# now = datetime.now()
# year = now.year
# month = now.month


# cal_text = calendar.month(year, month)


# label_title = Label(root,
#                     text=f"Календар на {calendar.month_name[month]} {year}",
#                     font=("Arial Rounded MT Bold", 16),
#                     bg="#F0F8FF",
#                     fg="#00008B")
# label_title.pack(pady=10)


# label_calendar = Label(root,
#                        text=cal_text,
#                        font=("Consolas", 12),
#                        bg="#F0F8FF",
#                        fg="#333333",
#                        justify=LEFT)
# label_calendar.pack(padx=20)


# button_exit = Button(root,
#                      text="Закрити календар",
#                      font=("Calibri", 12, "bold"),
#                      bg="#6495ED",
#                      fg="white",
#                      command=root.destroy)
# button_exit.pack(pady=15)

# root.mainloop()

