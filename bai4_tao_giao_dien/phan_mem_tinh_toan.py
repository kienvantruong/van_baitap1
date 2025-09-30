from tkinter import *
window = Tk()
window.title("Calculate")

window.minsize(width=400,height=600)
window.resizable(False,False)

chieu_dai_man_hinh = 20
chieu_cao_man_hinh = 532

chieu_dai_nut = 0
chieu_cao_nut = 0

labelcalculate = Label(text="0",font=("Arial",52))
labelcalculate.grid(row=0,columnspan=4,column=0,sticky="e",ipadx=10,ipady=50,)

buttonphantram = Button(text="%",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonphantram.grid(row=1,column=0,padx=2.5,pady=2.5)

buttonxoaso = Button(text="CE",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoaso.grid(row=1,column=1,padx=2.5,pady=2.5)

buttonxoatatca = Button(text="C",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoatatca.grid(row=1,column=2,padx=2.5,pady=2.5)

buttonxoa = Button(text="⌫",font=("Arial",20),border=1,width=chieu_dai_nut,height=chieu_cao_nut)
buttonxoa.grid(row=1,column=3,padx=2.5,pady=2.5)

buttonmotphanx = Button(text="¹/x",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonmotphanx.grid(row=2,column=0,padx=2.5,pady=2.5)

buttonxmu2 = Button(text="x²",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxmu2.grid(row=2,column=1,padx=2.5,pady=2.5)

buttoncanbac2 = Button(text="²√x",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttoncanbac2.grid(row=2,column=2,padx=2.5,pady=2.5)

buttonchia = Button(text="÷",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonchia.grid(row=2,column=3,padx=2.5,pady=2.5)

button7 = Button(text="7",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button7.grid(row=3,column=0,padx=2.5,pady=2.5)

button8 = Button(text="8",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button8.grid(row=3,column=1,padx=2.5,pady=2.5)

button9 = Button(text="9",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button9.grid(row=3,column=2,padx=2.5,pady=2.5)

button4 = Button(text="4",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button4.grid(row=4,column=0,padx=2.5,pady=2.5)

button5 = Button(text="5",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button5.grid(row=4,column=1,padx=2.5,pady=2.5)

button6 = Button(text="6",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button6.grid(row=4,column=2,padx=2.5,pady=2.5)

button1 = Button(text="1",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button1.grid(row=5,column=0,padx=2.5,pady=2.5)

button2 = Button(text="2",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button2.grid(row=5,column=1,padx=2.5,pady=2.5)

button3 = Button(text="3",font=("Arial",20),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
button3.grid(row=5,column=2,padx=2.5,pady=2.5)

buttonnhan = Button(text="×",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonnhan.grid(row=3,column=0,padx=2.5,pady=2.5)



buttonsodoi = Button(text="⁺/-")
# buttonsodoi.grid(row=, colomn=)

window.mainloop()