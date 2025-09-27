from tkinter import *
window = Tk()
window.title("Calculate")

window.minsize(width=400,height=600)
window.resizable(False,False)

chieu_dai_man_hinh = 320
chieu_cao_man_hinh = 532

chieu_dai_nut = 77
chieu_cao_nut = 51

labelcalculate = Label()
labelcalculate.grid(row=0,columnspan=4,column=0,sticky="ew")

buttonphantram = Button(text="%",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonphantram.grid(row=1,column=0,padx=2.5,pady=2.5)

buttonxoatatca = Button(text="C",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoatatca.grid(row=1,column=1,padx=2.5,pady=2.5)

buttonxoa = Button(text="⌫",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxoa.grid(row=1,column=3,columnspan=2,padx=2.5,pady=2.5)

buttonmotphanx = Button(text="¹/x",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonmotphanx.grid(row=2,column=0,padx=2.5,pady=2.5)

buttonxmu2 = Button(text="x²",font=("Arial",35),border=1,width=chieu_cao_nut,height=chieu_dai_nut)
buttonxmu2.grid(row=2,column=1,padx=2.5,pady=2.5)


buttonsodoi = Button(text="⁺/-")
# buttonsodoi.grid(row=, colomn=)

window.mainloop()