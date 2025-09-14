from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from PIL import Image,ImageTk
class POS:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='cadetblue')
        
        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        choice = StringVar()
        print(__file__)
        in_path = "C:/Users/Carini/Documents/GitHub/van_baitap1/bai4_tao_giao_dien/image/"
        
        self.Coffee10 = Image.open(in_path +"coffee1.jpg")
        self.Coffee20 = Image.open(in_path +"coffee2.jpg")
        self.Coffee30 = Image.open(in_path +"coffee3.jpg") 
        self.Coffee40 = Image.open(in_path +"coffee4.jpg")
        self.Coffee50 = Image.open(in_path +"RawCoffee.jpg")
        self.Coffee60 = Image.open(in_path +"CrazyCoffee.jpg")
        
        self.Drink10 = Image.open(in_path +"SummerSoftDrins.jpg")
        self.Drink20 = Image.open(in_path +"cokeA.jpg")
        self.Drink30 = Image.open(in_path +"coke.jpg")
        self.Drink40 = Image.open(in_path +"Non_Alcoholic.jpg")
        self.Drink50 = Image.open(in_path +"Cocktails.jpg")
        self.Drink60 = Image.open(in_path +"Just Drinks.jpg")
        
        self.Cake10 = Image.open(in_path +"AngleCake.jpg")
        self.Cake20 = Image.open(in_path +"Easy Cake.jpg")
        self.Cake30 = Image.open(in_path +"HomemadeCake.jpg")
        self.Cake40 = Image.open(in_path +"cake1.jpg")
        self.Cake50 = Image.open(in_path +"Black Forest Cake.jpg")
        self.Cake60= Image.open(in_path +"cake2.jpg")
        
        self.IceCake10 = Image.open(in_path +"Vanilla Cake.jpg")
        self.IceCake20 = Image.open(in_path +"cake3.jpg")
        self.IceCake30 = Image.open(in_path +"IceCreamCake.jpg")
        self.IceCake40 = Image.open(in_path +"UltimateCake.jpg")
        self.IceCake50 = Image.open(in_path +"RainCake.jpg")
        self.IceCake60 = Image.open(in_path +"PinkCake.jpg")
        
        self.FedBurger1 = Image.open(in_path +"FedBurger.jpg")
        self.Fries0 = Image.open(in_path +"Fries.jpg")
        self.FishBurger0 = Image.open(in_path +"FishBurger.jpg")
        self.BreadRoll0 = Image.open(in_path +"BreadRoll.jpg")
        self.ChickenNuggets0 = Image.open(in_path +"ChickenNuggets.jpg")
        self.MeatPie0 = Image.open(in_path +"NigerianMeatPie.jpg")
        self.Hotdog0 = Image.open(in_path +"Hotdog.jpg")
        self.Meatballs0 = Image.open(in_path +"Meatballs.jpg")

        
        # self.FedBurger1 = Image.open(in_path +"FedBurger.jpg")
        # self.FedBurger = ImageTk.PhotoImage(self.FedBurger1)
        # ===================================================================================================================== #
        
        self.Coffee1 = PhotoImage(self.Coffee10)
        self.Coffee2 = PhotoImage(self.Coffee20)
        self.Coffee3 = PhotoImage(self.Coffee30) 
        self.Coffee4 = PhotoImage(self.Coffee40)
        self.Coffee5 = PhotoImage(self.Coffee5)
        self.Coffee6 = PhotoImage(self.Coffee60)
        
        self.Drink1 = PhotoImage(self.Drink10)
        self.Drink2 = PhotoImage(self.Drink20)
        self.Drink3 = PhotoImage(in_path +"coke.jpg")
        self.Drink4 = PhotoImage(in_path +"Non_Alcoholic.jpg")
        self.Drink5 = PhotoImage(in_path +"Cocktails.jpg")
        self.Drink6 = PhotoImage(in_path +"Just Drinks.jpg")
        
        self.Cake1 = PhotoImage(in_path +"AngleCake.jpg")
        self.Cake2 = PhotoImage(in_path +"Easy Cake.jpg")
        self.Cake3 = PhotoImage(in_path +"HomemadeCake.jpg")
        self.Cake4 = PhotoImage(in_path +"cake1.jpg")
        self.Cake5 = PhotoImage(in_path +"Black Forest Cake.jpg")
        self.Cake6 = PhotoImage(in_path +"cake2.jpg")
        
        self.IceCake1 = PhotoImage(in_path +"Vanilla Cake.jpg")
        self.IceCake2 = PhotoImage(in_path +"cake3.jpg")
        self.IceCake3 = PhotoImage(in_path +"IceCreamCake.jpg")
        self.IceCake4 = PhotoImage(in_path +"UltimateCake.jpg")
        self.IceCake5 = PhotoImage(in_path +"RainCake.jpg")
        self.IceCake6 = PhotoImage(in_path +"PinkCake.jpg")
        
        self.FedBurger = ImageTk.PhotoImage(self.FedBurger1)
        self.Fries = PhotoImage(in_path +"Fries.jpg")
        self.FishBurger = PhotoImage(in_path +"FishBurger.jpg")
        self.BreadRoll = PhotoImage(in_path +"BreadRoll.jpg")
        self.ChickenNuggets = PhotoImage(in_path +"ChickenNuggets.jpg")
        self.MeatPie = PhotoImage(in_path +"NigerianMeatPie.jpg")
        self.Hotdog = PhotoImage(in_path +"Hotdog.jpg")
        self.Meatballs = PhotoImage(in_path +"Meatballs.jpg")
        
        MainFrame = Frame(self.root,bg='cadetblue')
        MainFrame.grid(padx=8,pady=5)
        
        ButtonFrame = Frame(MainFrame,bg='cadetblue', bd=5, width=1348,height=160,padx=4,pady=4,relief=RIDGE )
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame,bg='cadetblue', bd=5, width=800,height=300,padx=4,pady=4,relief=RIDGE )
        DataFrame.pack(side=LEFT)
        
        DataFrameLEFTCOVER = LabelFrame(DataFrame,bg='cadetblue', bd=5, width=800,height=300,padx=4,pady=4,
                                   font=('Arial',12,'bold'),text='Point of Sale',relief=RIDGE )
        DataFrameLEFTCOVER.pack(side=LEFT)
        
        ChangeButtonFrame = Frame(DataFrameLEFTCOVER, bd=5, width=300,height=460,pady=4,relief=RIDGE )
        ChangeButtonFrame.pack(side=LEFT,padx=4)
        
        ReceiptFrame = Frame(DataFrameLEFTCOVER,bd=5,width=200,height=400,pady=5,padx=1,relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT,padx=4)
        
        FoodItemFrame = LabelFrame(DataFrame,bd=5,width=450,height=300,padx=5,pady=2,relief=RIDGE,bg='cadetblue',font=('Arial',12,'bold'),text='Item')
        FoodItemFrame.pack(side=RIGHT)
        
        CalFrame = Frame(ButtonFrame, bd=5 ,width=432, height=140, relief=RIDGE)
        CalFrame.grid(row=0, column=0 ,padx=5)
        
        ChangeFrame = Frame(ButtonFrame, bd=5, width=500 ,height=140,pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0, column= 1, padx=5)
        
        RemoveFrame = Frame(ButtonFrame,bd=5,width=400,height=140,pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0,column=2,padx=5)
        # Entry & Label Widget
        self.lblSubTotal = Label(CalFrame,font=('Arial',14,'bold'),text='Sub Total', bd=5)
        self.lblSubTotal.grid(row=0, column=0 , sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame,font=('Arial',14,'bold'),textvariable=SubTotal_Input, bd=2, width=24)
        self.txtSubTotal.grid(row=0, column=1 , sticky=W, padx=5)
        
        self.lblTax = Label(CalFrame,font=('Arial',14,'bold'),text='Tax', bd=5)
        self.lblTax.grid(row=1, column=0 , sticky=W, padx=5)
        self.txtTax = Entry(CalFrame,font=('Arial',14,'bold'),textvariable=Tax_Input, bd=2, width=24)
        self.txtTax.grid(row=1, column=1 , sticky=W, padx=5)
        
        self.lblTotal = Label(CalFrame,font=('Arial',14,'bold'),text='Total', bd=5)
        self.lblTotal.grid(row=2, column=0 , sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame,font=('Arial',14,'bold'),textvariable=Total_Input, bd=2, width=24)
        self.txtTotal.grid(row=2, column=1 , sticky=W, padx=5)
    # 
        self.lblMOP = Label(ChangeFrame,font=('Arial',14,'bold'),text='Menthod of Payment', bd=5)
        self.lblMOP.grid(row=0, column=0 , sticky=W, padx=5)
        self.cboMOP = ttk.Combobox(ChangeFrame,font=('Arial',14,'bold'),  width=36, state='readonly',textvariable=choice,justify=RIGHT)
        self.cboMOP['values'] = ('','Cash','Visa Card','Master Card')
        self.cboMOP.current(0)
        self.cboMOP.grid(row=0, column=1)
        
        self.lblCost = Label(ChangeFrame,font=('Arial',14,'bold'),text='Cash', bd=5)
        self.lblCost.grid(row=1, column=0 , sticky=W, padx=5)
        self.txtCost = Entry(ChangeFrame,font=('Arial',14,'bold'),textvariable=Tax_Input, bd=2, width=38)
        self.txtCost.grid(row=1, column=1 , sticky=W, padx=5)
        
        self.lblChange = Label(ChangeFrame,font=('Arial',14,'bold'),text='Change', bd=5)
        self.lblChange.grid(row=2, column=0 , sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame,font=('Arial',14,'bold'),textvariable=Total_Input, bd=2, width=38)
        self.txtChange.grid(row=2, column=1 , sticky=W, padx=5)
        # Button
        
        self.btnPay = Button(RemoveFrame,padx=2,font=('Arial',15,'bold'),text='Pay',width=10,height=1, bd=2)
        self.btnPay.grid(row=0, column=0 , pady=2, padx=4)
        
        self.btnExit = Button(RemoveFrame,padx=2,font=('Arial',15,'bold'),text='Exit',width=10,height=1, bd=2)
        self.btnExit.grid(row=0, column=1 , pady=2, padx=4)
        
        self.btnReset = Button(RemoveFrame,padx=2,font=('Arial',15,'bold'),text='Reset',width=10,height=1, bd=2)
        self.btnReset.grid(row=1, column=0 , pady=2, padx=4)
       
        self.btnRemoveItem = Button(RemoveFrame,padx=2,font=('Arial',15,'bold'),text='Remove Item',width=10,height=1, bd=2)
        self.btnRemoveItem.grid(row=1, column=1 , pady=2, padx=4)
        
        # Button Frame
        
        # self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger = Button(ChangeButtonFrame,image=self.FedBurger,padx=2,width=104,height=104, bd=2)        
        self.btnFedBurger.grid(row=0, column=0 , pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=0, column=1 , pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=1, column=0 , pady=2, padx=4)
               
        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=1, column=1 , pady=2, padx=4)
        
        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=2, column=0 , pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=2, column=1 , pady=2, padx=4)
        
        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=3, column=0 , pady=2, padx=4)
        
        self.btnFedBurger = Button(ChangeButtonFrame,padx=2,image=self.FedBurger,width=104,height=104, bd=2)
        self.btnFedBurger.grid(row=3, column=1 , pady=2, padx=4)
        
        #41:17
        
        
        
        
if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()





