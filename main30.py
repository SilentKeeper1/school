from tkinter import *
from tkinter import messagebox

def b1_click():
    try:
        n = float(entry1.get().replace(',', '.'))
        if n < 0:
            raise ValueError


        trees = int(n // 60)


        area = (n / 60) * 0.0005
    except Exception:
        messagebox.showerror("Помилка", "Введи коректну масу (невід’ємне число).")
        return

    entry2.delete(0, END)
    entry2.insert(0, str(trees))

    entry3.delete(0, END)
    entry3.insert(0, f"{area:.6f}")

root = Tk()
root.title("Збережи дерево")


Label(root, text="Введіть масу, кг:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
entry1 = Entry(root, width=10)
entry1.grid(row=0, column=1, padx=8, pady=8)


b1 = Button(root, text="Обчислити", command=b1_click, width=14)
b1.grid(row=1, column=0, columnspan=2, padx=8, pady=8)


Label(root, text="Збережено дерев:").grid(row=2, column=0, padx=8, pady=8, sticky="w")
entry2 = Entry(root, width=10)
entry2.grid(row=2, column=1, padx=8, pady=8)


Label(root, text="Збережено лісу, га:").grid(row=3, column=0, padx=8, pady=8, sticky="w")
entry3 = Entry(root, width=10)
entry3.grid(row=3, column=1, padx=8, pady=8)

root.mainloop()
