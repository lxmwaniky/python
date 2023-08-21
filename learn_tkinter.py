from tkinter import *

window = Tk()
window.title("Lxmwaniky")
window.geometry("600x600")
window.config(background="skyblue")

label = Label(window,text="Hello World", 
              font=("Arial",40,"bold"), 
              fg=("green"), 
              bg="skyblue")
label.pack()







window.mainloop()