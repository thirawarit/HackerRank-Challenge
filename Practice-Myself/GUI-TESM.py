from tkinter import *
def namefunc(var1, var2):
    pass
mainwindow = Tk()
mainwindow.geometry("720x480")
transparent = "white"
mainwindow.configure(bg=transparent)
label_1 = Label(mainwindow, text="Lot Management", font=("",24) ,bg=transparent, fg='black')
label_1.grid(row=10,column=10)
label_2 = Label(mainwindow, text="Lot Management", font=("",24) ,bg=transparent, fg='black')
label_2.grid(row=200,column=200)
mainwindow.mainloop()