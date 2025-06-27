from tkinter import *
import turtle
import keyboard
window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)


# my label
my_label = Label(text="I Am a Label",font=("Arial", 24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")    
# tim = turtle.Turtle()
# tim.write("Some text")
# import turtle
# turtle.Turtle()

# button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())  
    print(input.get())      
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
# print(input.get(Entry))

# my_label.config(text=)    









window.mainloop()