import sqlite3

from tkinter import *

conn = sqlite3.connect('cars.db')
c = conn.cursor()

MakeOptions=["Skoda","Suzuki","Hundai","Jeep"]
SkodaModel=["Rapid","Octavia","Superb"]
SuzukiModel=["Ciaz","Baleno","Ertiga"]
HundaiModel=["i10","i20","Creta"]
JeepModel=["Compass","Cherokee"]

root = Tk()

root.geometry("500x500")


def search():
    CModel(CMake)
    print(Car_Model,Car_Make)
    Search_car()

def CModel(CMake):

    global Car_Model
    Car_Model=CarModel.get()
    print(Car_Model)



def CMake():
    global Car_Make,Car_Model,CarModel
    Car_Make=CarMake.get()
    if Car_Make=="Skoda":
        CarModel = StringVar()
        CarModel.set("Select car")
        Cmodel=OptionMenu(root, CarModel , *SkodaModel)
        Cmodel.grid(row=3, column=3)
    elif Car_Make=="Suzuki":
            CarModel = StringVar()
            CarModel.set("Select car")
            Cmodel=OptionMenu(root, CarModel , *SuzukiModel)
            Cmodel.grid(row=3, column=3)
    elif Car_Make=="Hundai":
            CarModel = StringVar()
            CarModel.set("Select car")
            Cmodel=OptionMenu(root, CarModel , *HundaiModel)
            Cmodel.grid(row=3, column=3)
    elif Car_Make=="Jeep":
            CarModel = StringVar()
            CarModel.set("Select car")
            Cmodel=OptionMenu(root, CarModel , *JeepModel)
            Cmodel.grid(row=3, column=3)
    next_button.destroy()
    global Search_button
    Search_button=Button(root, text="Next", command=search)
    Search_button.grid(row=4,column=5
    )


def Search_car():
    Search_button.destroy()
    global Display_cost,Display_Part
    c.execute("SELECT totalCost FROM car_details WHERE car_model=Car_Model")

    cost=c.fetchall()
    Display_cost = (max(cost))
    print(Display_cost[0])
    e1=Label(root,text="")
    e1.grid(row=6,column=0)
    e2=Label(root,text="")
    e2.grid(row=7,column=0)
    e3=Label(root,text="")
    e3.grid(row=8,column=0)
    e4=Label(root,text="")
    e4.grid(row=9,column=0)

    l1=Label(root,text="The maintanance cost is")
    l1.grid(row=10,column=0)
    l2=Label(root,text=Display_cost[0])
    l2.grid(row=10,column=1)

CarMake = StringVar()
CarMake.set("Select car Company")
Cmake=OptionMenu(root, CarMake , *MakeOptions)
Cmake.grid(row=3, column=0)
next_button=Button(root, text="Next", command=CMake)
next_button.grid(row=4,column=3)

root.mainloop()
