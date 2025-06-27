from tkinter import *

windows = Tk()
windows.title("Miles to Km Coverter")
windows.minsize(width=335,height=175)
# Label
my_label = Label(text="Miles", font=("Arial", 15))
my_label.grid(column=2,row=0)

my_label2 = Label(text="                                     ")
my_label2.grid(column=0,row=0)

my_label3 = Label(text="is equal to",font=("Arial",15))
my_label3.grid(column=0, row=1)

my_label4 = Label(text="0",font=("Arial", 14))
my_label4.grid(column=1, row=1)

my_label5 = Label(text="Km",font=("Arial", 15))
my_label5.grid(column=2, row=1)

my_label6 = Label(text="                                     ")
my_label6.grid(column=0, row=2)
# Entry
input = Entry(width=25)
input.grid(column=1, row=0)

# Button
def button_clicked():
    abc = calculate(input.get())
    my_label4.config(text=abc)
button = Button(text="Calculate", command=button_clicked, width=20, font=("Arial", 13))
button.grid(column=1, row=2)
# Calculate
def calculate(x):
    
    return 1.609344*int(x)
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
windows.mainloop()
