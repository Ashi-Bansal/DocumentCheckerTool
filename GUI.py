from tkinter import *
from tkinter import filedialog
from main import *
import os.path

import PyPDF2

from docx import Document
txt=""
lbl= None
def clicked():
    #res = "Welcome to " + txt.get()
    #lbl.configure(text=res)
    global txt
    global lbl
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

    vector = FeatureExtration(text, winSize=10, step=10)
    ElbowMethod(np.array(vector))
    result=Analysis(vector)
    lbl.configure(text=str(result))
def browsefunc():
    global txt
    filename = filedialog.askopenfilename()
    txt.insert(0,filename)

def stylo():
    window = Tk()
    window.title("Stylometric Analysis")
    window.geometry('450x300')
    window.configure(background='blue')


    mrg1=Label(window,text='')
    mrg1.grid(column=0, row=0)
    mrg1.configure(background='blue')

    mrg2=Label(window,text='')
    mrg2.grid(column=1, row=1)
    mrg2.configure(background='blue')

    mrg3=Label(window,text='')
    mrg3.grid(column=2, row=2)
    mrg3.configure(background='blue')

    mrg4=Label(window,text='')
    mrg4.grid(column=3, row=3)
    mrg4.configure(background='blue')

    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=4)

    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=6)
    global lbl
    lbl = Label(window, text="Writing Styles Classification using Stylometric Analysis",font=("Arial Bold", 10))
 
    lbl.grid(column=6, row=5)

    global txt
    txt= Entry(window,width=40)
 
    txt.grid(column=6, row=7,columnspan=2)
    browsebutton = Button(window, text="Browse", command=browsefunc)
    browsebutton.grid(column=6, row=8)
    btn = Button(window, text="Click Me",bg="orange", fg="white",command=clicked)
 
    btn.grid(column=6, row=9)

 
    window.mainloop()

