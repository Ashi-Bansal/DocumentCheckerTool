from tkinter import *
import os.path

import PyPDF2

from docx import Document

import sys
import time

from copyleaks.copyleakscloud import CopyleaksCloud
from copyleaks.processoptions import ProcessOptions
from copyleaks.product import Product

window = Tk()
 
window.title("Stylometric Analysis")
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

lbl = Label(window, text="Report Plagarism Checker",font=("Arial Bold", 10))
 
lbl.grid(column=6, row=5)

txt = Entry(window,width=40)
 
txt.grid(column=6, row=7,columnspan=2)

def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text=res)
    extension = os.path.splitext(txt.get())[1]
    print(extension)
    text=""
    if extension=='.pdf':
        # creating a pdf file object 
        pdfFileObj = open(txt.get(), 'rb') 
  
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
        # printing number of pages in pdf file 
        for i in range(pdfReader.numPages):
            # creating a page object 
            pageObj = pdfReader.getPage(i) 
            text=text+pageObj.extractText()  
        
        # closing the pdf file object 
        pdfFileObj.close() 
    elif extension=='.doc' or extension=='.docx':
        doc = Document(txt.get())
        for para in doc.paragraphs:
            text=text+para.text+'\n'
            #print(text)
    else:
         text = open(txt.get()).read()

    cloud = CopyleaksCloud(Product.Education, 'nukuul@gmail.com', '56D7207D-32D9-4758-A84E-E17F5F8068E3')
    options = ProcessOptions()
    options.setSandboxMode(True)
    process = cloud.createByText(text)
    results = process.getResults()
    result="\nFound "+(len(results))+" results..."
    for r in results:
        result=result+r

    lbl.configure(text=str(result))

btn = Button(window, text="Click Me",bg="orange", fg="red",command=clicked)
 
btn.grid(column=6, row=9)

 
window.mainloop()

