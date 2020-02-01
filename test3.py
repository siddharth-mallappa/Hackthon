from tkinter import *
import sqlite3

conn= sqlite3.connect('cars.db')
c=conn.cursor()

c.execute(""" Create table cars_details(
car_make text,car_model text,
carPart text,partQuantity integer,partTotal integer,
carPart1 text,partQuantity1 integer,partTotal1 integer,
carPart2 text,partQuantity2 integer,partTotal2 integer,
carPart3 text,partQuantity3 integer,partTotal3 integer,
totalCost integer
)
""")


root = Tk()

root.geometry("900x900")



First=Label(root, text="Customer Details")
First.grid(row=0,sticky=W)

empty1=Label(root, text="")
empty1.grid(row=1,sticky=W)

name=Label(root, text="Name")
name.grid(row=2,sticky=W)

EntryName=StringVar()
Ename= Entry(root,textvariable=EntryName,bg="#dcdcdc")
Ename.grid(row=2,column=1)

labl2=Label(root, text="Phone No")
labl2.grid(row=3,sticky=W)

EntryPhoneNumber=StringVar()
textbox2= Entry(root,textvariable=EntryPhoneNumber,bg="#dcdcdc")
textbox2.grid(row=3,column=1)

labl3=Label(root, text="Registration No")
labl3.grid(row=4,sticky=W)

Entry_Registration=StringVar()
textbox3= Entry(root,textvariable=Entry_Registration,bg="#dcdcdc")
textbox3.grid(row=4,column=1)

empty2=Label(root, text="")
empty2.grid(row=5,sticky=W)

labl2=Label(root, text="CAR DETAILS")
labl2.grid(row=6,sticky=W)

empty3=Label(root, text="")
empty3.grid(row=7,sticky=W)

abl2=Label(root, text="Car Type")
abl2.grid(row=8,sticky=W)

var4=IntVar()
cb3=Radiobutton(root, text="Petrol",value=1,variable=var4)
cb3.grid(row=8, column=1)

cb3=Radiobutton(root, text="Diesel",value=2,variable=var4)
cb3.grid(row=8, column=2)

Lmake=Label(root, text="Car Make")
Lmake.grid(row=9,sticky=W)

Entry_CarMake=StringVar()
textboxmake= Entry(root,textvariable=Entry_CarMake,bg="#dcdcdc")
textboxmake.grid(row=9,column=1)

Lmodel=Label(root, text="Car Model")
Lmodel.grid(row=10,sticky=W)

Entry_CarModel=StringVar()
textboxmodel= Entry(root,textvariable=Entry_CarModel,bg="#dcdcdc")
textboxmodel.grid(row=10,column=1)

LYear=Label(root, text="Car Year")
LYear.grid(row=11,sticky=W)

Entry_CarYear=StringVar()
textboxyear= Entry(root,textvariable=Entry_CarYear,bg="#dcdcdc")
textboxyear.grid(row=11,column=1)

LMilage=Label(root, text="Car Milage")
LYear.grid(row=11,sticky=W)



Empty4=Label(root, text="")
Empty4.grid(row=12,sticky=W)

Maintanance=Label(root, text="Maintenance Details")
Maintanance.grid(row=13,sticky=W)

Empty5=Label(root, text="")
Empty5.grid(row=14,sticky=W)

Details=Label(root, text="Part(s) Details")
Details.grid(row=15,column=0,sticky=W)

Q=Label(root, text="Quantity")
Q.grid(row=15,column=1,sticky=W)

up=Label(root, text="Unit Price")
up.grid(row=15,column=2,sticky=W)

up=Label(root, text="Amount in Rs")
up.grid(row=15,column=3,sticky=W)

Entry_Part=StringVar()
Part= Entry(root,textvariable=Entry_Part)
Part.grid(row=16,column=0)

Entry_Quantity=StringVar()
Quantity= Entry(root,textvariable=Entry_Quantity)
Quantity.grid(row=16,column=1)

Entry_UnitPrice=StringVar()
UnitPrice= Entry(root,textvariable=Entry_UnitPrice)
UnitPrice.grid(row=16,column=2)

Entry_Part1=StringVar()
Part1= Entry(root,textvariable=Entry_Part1)
Part1.grid(row=17,column=0)

Entry_Quantity1=StringVar()
Quantity1= Entry(root,textvariable=Entry_Quantity1)
Quantity1.grid(row=17,column=1)

Entry_UnitPrice1=StringVar()
UnitPrice1= Entry(root,textvariable=Entry_UnitPrice1)
UnitPrice1.grid(row=17,column=2)

Entry_Part2=StringVar()
Part2= Entry(root,textvariable=Entry_Part2)
Part2.grid(row=18,column=0)

Entry_Quantity2=StringVar()
Quantity2= Entry(root,textvariable=Entry_Quantity2)
Quantity2.grid(row=18,column=1)

Entry_UnitPrice2=StringVar()
UnitPrice2= Entry(root,textvariable=Entry_UnitPrice2)
UnitPrice2.grid(row=18,column=2)

Entry_Part3=StringVar()
Part3= Entry(root,textvariable=Entry_Part3)
Part3.grid(row=19,column=0)

Entry_Quantity3=StringVar()
Quantity3= Entry(root,textvariable=Entry_Quantity3)
Quantity3.grid(row=19,column=1)

Entry_UnitPrice3=StringVar()
UnitPrice3= Entry(root,textvariable=Entry_UnitPrice3)
UnitPrice3.grid(row=19,column=2)



ServiceC=Label(root, text="Service Cost")
ServiceC.grid(row=20,column=1,sticky=W)

Entry_ServiceCost=StringVar()
Entry_ServiceCost= Entry(root,textvariable=Entry_ServiceCost)
Entry_ServiceCost.grid(row=20,column=3)

def calculate():
    global amt,amt1,amt2,amt3

    Car_part=Entry_Part.get()
    Part_quantity=int(Entry_Quantity.get())
    Unit_Price=int(Entry_UnitPrice.get())
    amt=Part_quantity*Unit_Price
    Entry_Amount=Label(root, text=amt,bg="grey")
    Entry_Amount.grid(row=16,column=3,sticky=W)

    Car_part1=Entry_Part1.get()
    Part_quantity1=int(Entry_Quantity1.get())
    Unit_Price1=int(Entry_UnitPrice1.get())
    amt1=Part_quantity1*Unit_Price1
    Entry_Amount1=Label(root, text=amt1,bg="grey")
    Entry_Amount1.grid(row=17,column=3,sticky=W)

    Car_part2=Entry_Part2.get()
    Part_quantity2=int(Entry_Quantity2.get())
    Unit_Price2=int(Entry_UnitPrice2.get())
    amt2=Part_quantity2*Unit_Price2
    Entry_Amount2=Label(root, text=amt2,bg="grey")
    Entry_Amount2.grid(row=18,column=3,sticky=W)

    Car_part3=Entry_Part3.get()
    Part_quantity3=int(Entry_Quantity3.get())
    Unit_Price3=int(Entry_UnitPrice3.get())
    amt3=Part_quantity3*Unit_Price3
    Entry_Amount3=Label(root, text=amt3,bg="grey")
    Entry_Amount3.grid(row=19,column=3,sticky=W)
    global TotalCost
    ServiceCost=int(Entry_ServiceCost.get())
    TotalCost=ServiceCost+amt+amt1+amt2+amt3

    ShowTotal = Label(root, text=TotalCost,bg="grey")
    ShowTotal.grid(row=21,column=3)

    getinfo()
    #print(CMake,CModel,Car_part,CType,Car_part,Part_quantity,amt)
def clear_form():

      root.reset()

def getinfo():
    global Car_Make,Car_Model,CarPart,PartQuantity,UnitPrice,PartToal
    global CarPart1,PartQuantity1,UnitPrice1,PartToal1
    global CarPart2,PartQuantity2,UnitPrice2,PartToal2
    global CarPart3,PartQuantity3,UnitPrice3,PartToal3

    Total_Cost=TotalCost

    Car_Make=Entry_CarMake.get()
    Car_Model=Entry_CarModel.get()
    if var4.get() == 1:

        Car_Type="Petrol"
    elif var4.get()==2:
        Car_Type="Diesel"

    CarPart=Entry_Part.get()
    PartQuantity=int(Entry_Quantity.get())
    UnitPrice=int(Entry_UnitPrice.get())
    PartToal=amt

    CarPart1=Entry_Part1.get()
    PartQuantity1=int(Entry_Quantity1.get())
    UnitPrice1=int(Entry_UnitPrice1.get())
    PartToal1=amt1

    CarPart2=Entry_Part2.get()
    PartQuantity2=int(Entry_Quantity2.get())
    UnitPrice2=int(Entry_UnitPrice2.get())
    PartToal2=amt2

    CarPart3=Entry_Part3.get()
    PartQuantity3=int(Entry_Quantity3.get())
    UnitPrice3=int(Entry_UnitPrice3.get())
    PartToal3=amt3

def  db():
    print(Car_Make,Car_Model)
    print(CarPart,PartQuantity,PartToal)
    print(CarPart1,PartQuantity1,PartToal1)
    print(CarPart2,PartQuantity2,PartToal2)
    print(CarPart3,PartQuantity3,PartToal3)
    print(TotalCost)
    values=(Car_Make,Car_Model,CarPart,PartQuantity,PartToal,CarPart1,PartQuantity1,PartToal1,CarPart2,PartQuantity2,PartToal2,CarPart3,PartQuantity3,PartToal3,TotalCost)
    with conn:
        s="insert into cars_details values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        c.execute(s,values)
        

total= Button(root, text="TOTAL",command=calculate)
total.grid(row=21,column=2, sticky=W)

Clear_bt= Button(root, text="Clear",command=clear_form)
Clear_bt.grid(row=22,column=0, sticky=W)

Submit_button= Button(root, text="SUBMIT",command=db)
Submit_button.grid(row=22,column=2, sticky=W)
root.mainloop()
