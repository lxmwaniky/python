from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)

window = Tk()

window.title("Lxmwaniky")
window.geometry("600x600")
window.config(background="skyblue")


        #LABELS
label = Label(window,text="Hello World", font=("Arial",40,"bold"), fg=("green"), bg="skyblue")
label.pack()


        #BUTTONS
button = Button(window, text="Click me", command=click, font=("Comic Sans",30))
button.pack()







window.mainloop()