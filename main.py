# Patient Management
# Creator : Iranian Programmers YouTube Channel

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from tkinter import Scrollbar
import datetime 

window = Tk()
window.title("Patient Management")
window.geometry("1000x800")
window.configure(bg="dodgerblue")


def Labels():
    big = tk.Label(window, text="Patient Management", fg="black", font=("Arial Bold", 30))
    info = tk.Label(window, text="Patient Information", font=("Arial Bold", 15))
    Name = tk.Label(window, text="Name", font=("Arial Bold", 20))
    FirstName = tk.Label(window ,text="First Name")
    LastName = tk.Label(window, text="LastName")
    Birthday = tk.Label(window, text="Birth", font=("Arial Bold", 20))
    gender = tk.Label(window, text="Gender", font=("Arial Bold", 20))
    desease = tk.Label(window, text="Desease", font=("Arial Bold", 20))
    month_lbl = tk.Label(window, text="Month")
    day_lbl = tk.Label(window, text="Day")
    year_lbl = tk.Label(window, text="Year")
    big.place(x=10, y=10)
    info.place(x=10, y=80)
    Name.place(x=10, y=141)
    Birthday.place(x=10, y=240)
    FirstName.place(x=180, y=175)
    LastName.place(x=480, y=175)
    gender.place(x=10, y=340)
    desease.place(x=10, y=440)
    month_lbl.place(x=160, y=275)
    day_lbl.place(x=420, y=275)
    year_lbl.place(x=670, y=275)

def Entries():
    global Name_entry
    global Last_entry 
    Name_entry = Entry(window, width=30)
    Name_entry.focus()
    Last_entry = Entry(window, width=30)
    Name_entry.place(x=100, y=150)
    Last_entry.place(x=400, y=150)

def Gender():
    global male
    global female
    global selected
    selected = IntVar()
    male = tk.Radiobutton(window, text="Male", value=0, font=("Arial Bold", 15), var=selected)
    female = tk.Radiobutton(window, text="Female", value=1, font=("Arial Bold", 15), var=selected)
    male.place(x=140, y=345)
    female.place(x=240, y=345)


def Comboboxes():
    global months 
    global day 
    global year 
    global desease_box
    global values
    global day_values
    global this_year
    global year_values
    values = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    months = Combobox(window)
    months["values"] = values 
    months.current(0)
    months.place(x=100, y=250)
    day = Combobox(window)
    day_values = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    day["values"] = day_values
    day.current(14)
    day.place(x=350, y=250)
    this_year = datetime.datetime.now()
    year = Combobox(window)
    year_values = (1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)
    year["values"] = year_values 
    year.current(20)
    year.place(x = 600, y=250)
    desease_box = Combobox(window)
    desease_box["values"] = ("Autoimmune Diseases","Allergies & Asthma","Cancer","Celiac Disease","Crohn's & Colitis","Heart Disease","Infectious Diseases","Liver Disease", "Nothing Just for visiting")
    desease_box.current(4)
    desease_box.place(x=150, y=450)

def Clicked():
    if Name_entry.get() == "":
        messagebox.showwarning("WARN", "Enter Your Name")

    elif Last_entry.get() == "":
        messagebox.showwarning("WARN", "Enter Your LastName")

    elif months.get() == "":
        messagebox.showwarning("WARN", "Enter The Month")

    elif day.get() == "":
        messagebox.showwarning("WARN", "Enter The Day")

    elif year.get() == "":
        messagebox.showwarning("WARN", "Enter The Year")

    elif len(Name_entry.get()) <= 2:
        messagebox.showwarning("WARN", "Enter Valid Name (more than two characters)")

    elif len(Name_entry.get()) >= 30:
        messagebox.showwarning("WARN", "Enter Valid Name (less than 30 characters)")

    elif months.get() not in values:
        messagebox.showwarning("WARN", "Enter The Month from the box")

    elif int(day.get()) > 31 or int(day.get()) < 1:
        messagebox.showwarning("WARN", "Enter The Day from the box")

    new_year = 2020
    old_year = 1960

    if int(year.get()) > new_year or int(year.get()) < old_year:
        messagebox.showwarning("WARN", "Enter The Year from the box")

    elif desease_box.get() not in desease_box["values"] or desease_box.get() == "":
        messagebox.showwarning("WARN", "Enter Your Desease from the box")

    else:
        li = ["------------------------------------"]
        with open("DataBase.txt", "a") as f:
            for i in li:
                f.write("{}\n".format(i))
            f.write("First Name : {} | LastName : {} | Birth | Month : {} | Day : {} | Year : {} | Gender : {} | Desease : {}\n".format(Name_entry.get(), Last_entry.get(), months.get(), day.get(), year.get(), selected.get(), desease_box.get()))
            f.close()
            messagebox.showinfo("Successful", "Your Request Completed Successfully")
            sys.exit()
            


btn = Button(window, text="Submit", command=Clicked)
btn.place(x = 10, y=540)

Labels()
Entries()
Comboboxes()
Gender()

window.mainloop()