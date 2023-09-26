from tkinter import *


def button_callback(value):
    print(value)


window = Tk()

b1 = Button(window, text="BTN 1", command=lambda: button_callback(1))
b1.grid(row=0, column=0)
b2 = Button(window, text="BTN 2", command=lambda: button_callback(2))
b2.grid(row=0, column=1)
b3 = Button(window, text="BTN 3", command=lambda: button_callback(3))
b3.grid(row=0, column=3)

window.mainloop()