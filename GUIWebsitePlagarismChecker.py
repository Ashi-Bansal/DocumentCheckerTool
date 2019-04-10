from tkinter import *
import os.path

import sys
import time

from copyleaks.copyleakscloud import CopyleaksCloud
from copyleaks.processoptions import ProcessOptions
from copyleaks.product import Product

window = Tk()
 
window.title("Plagarism Checker")
window.geometry('450x300')

mrg1=Label(window,text='')
mrg1.grid(column=0, row=0)

mrg2=Label(window,text='')
mrg2.grid(column=1, row=1)

mrg3=Label(window,text='')
mrg3.grid(column=2, row=2)

mrg4=Label(window,text='')
mrg4.grid(column=3, row=3)

mrg5=Label(window,text='')
mrg5.grid(column=4, row=4)

mrg5=Label(window,text='')
mrg5.grid(column=4, row=6)

lbl = Label(window, text="Website Plagarism Checker",font=("Arial Bold", 10))
 
lbl.grid(column=6, row=5)

txt = Entry(window,width=40)
 
txt.grid(column=6, row=7,columnspan=2)

def clicked():
    text = txt.get()

    cloud = CopyleaksCloud(Product.Education, 'nukuul@gmail.com', '56D7207D-32D9-4758-A84E-E17F5F8068E3')
    options = ProcessOptions()
    options.setSandboxMode(True)
    process = cloud.createByUrl(text)
    results = process.getResults()
    f = open("WebsitePlagarismChecker.txt", "w")
    result="\nFound "+str(len(results))+" results..."
    for r in results:
        global result
        result+=r

    lbl.configure(text=str(result))
    f.write(result)

btn = Button(window, text="Click Me",bg="orange", fg="red",command=clicked)
 
btn.grid(column=6, row=9)

 
window.mainloop()

