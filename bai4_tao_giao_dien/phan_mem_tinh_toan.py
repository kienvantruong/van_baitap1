from tkinter import *
window = Tk()
window.title("Calculate")
chieu_dai_man_hinh = 260
chieu_cao_man_hinh = 532

window.minsize(width=chieu_dai_man_hinh,height=chieu_cao_man_hinh)
window.resizable(False,False)

padynut=1
padxnut=0.1
bordernut = 1
chieu_dai_nut = 0
chieu_cao_nut = 0

labelcalculate = Label(text="0",font=("Arial",52))
labelcalculate.grid(row=0,columnspan=4,column=0,sticky="e",ipadx=10,ipady=50,)

buttonphantram = Button(text=" % ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonphantram.grid(row=1,column=0,padx=padxnut,pady=padynut)

buttonxoaso = Button(text=" CE ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoaso.grid(row=1,column=1,padx=padxnut,pady=padynut)

buttonxoatatca = Button(text="  C  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoatatca.grid(row=1,column=2,padx=padxnut,pady=padynut)

buttonxoa = Button(text=" ⌫ ",font=("Arial",20),border=bordernut,width=chieu_dai_nut,height=chieu_cao_nut)
buttonxoa.grid(row=1,column=3,padx=padxnut,pady=padynut)

buttonmotphanx = Button(text=" ¹/x ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonmotphanx.grid(row=2,column=0,padx=padxnut,pady=padynut)

buttonxmu2 = Button(text="  x² ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxmu2.grid(row=2,column=1,padx=padxnut,pady=padynut)

buttoncanbac2 = Button(text=" ²√x ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttoncanbac2.grid(row=2,column=2,padx=padxnut,pady=padynut)

buttonchia = Button(text=" ÷ ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonchia.grid(row=2,column=3,padx=padxnut,pady=padynut)

button7 = Button(text="  7  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button7.grid(row=3,column=0,padx=padxnut,pady=padynut)

button8 = Button(text="  8  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button8.grid(row=3,column=1,padx=padxnut,pady=padynut)

button9 = Button(text="  9  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button9.grid(row=3,column=2,padx=padxnut,pady=padynut)

button4 = Button(text="  4  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button4.grid(row=4,column=0,padx=padxnut,pady=padynut)

button5 = Button(text="  5  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button5.grid(row=4,column=1,padx=padxnut,pady=padynut)

button6 = Button(text="  6  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button6.grid(row=4,column=2,padx=padxnut,pady=padynut)

button1 = Button(text="  1  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button1.grid(row=5,column=0,padx=padxnut,pady=padynut)

button2 = Button(text="  2  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button2.grid(row=5,column=1,padx=padxnut,pady=padynut)

button3 = Button(text="  3  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
button3.grid(row=5,column=2,padx=padxnut,pady=padynut)

buttonnhan = Button(text="  ×  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttonnhan.grid(row=3,column=3,padx=padxnut,pady=padynut)

buttontru = Button(text="  ⁻  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttontru.grid(row=4,column=3,padx=padxnut,pady=padynut)

buttoncong = Button(text="  ⁺  ",font=("Arial",20),border=bordernut,width=chieu_cao_nut,height=chieu_dai_nut)
buttoncong.grid(row=4,column=3,padx=padxnut,pady=padynut)


buttonsodoi = Button(text="⁺/-")
# buttonsodoi.grid(row=, colomn=)

window.mainloop()