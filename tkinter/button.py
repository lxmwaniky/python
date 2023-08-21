from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)

window = Tk()
window.title("Button")
button = Button(window, text="Click me", command=click, font=("Comic Sans",30))
button.pack()

window.mainloop()