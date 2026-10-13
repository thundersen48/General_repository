from tkinter import*
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("960x720")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()