#author: Vijesh.V @FreakoutGames
#testing Tkinter package

#Tkinter work in two step way - initializing the widget and second placing the widget
#Alway Tkinter has Tk() and mainloop()

from tkinter import *

root = Tk()

def displayLabel():
    myLabel = Label(root, text = enter.get())
    myLabel.pack()
#creating label
#myLabel = Label(root, text="Hello World")
#myLabel1 = Label(root, text="Hello Vijesh")

enter = Entry(root)
enter.pack()
enter.insert(0, "Enter Text")


myButton = Button(root, text="Click Me!", command=displayLabel, fg="red")
myButton.pack()

root.mainloop()