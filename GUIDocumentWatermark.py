from tkinter import *
from tkinter import filedialog
import PyPDF2

txt=None
txt1=None
lbl=None

def add_watermark(wmFile, pageObj): 
    # opening watermark pdf file 
    wmFileObj = open(wmFile, 'rb') 
     
    # creating pdf reader object of watermark pdf file 
    pdfReader = PyPDF2.PdfFileReader(wmFileObj)  
      
    # merging watermark pdf's first page with passed page object. 
    pageObj.mergePage(pdfReader.getPage(0)) 
      
    # closing the watermark pdf file object 
    wmFileObj.close() 
      
    # returning watermarked page object 
    return pageObj 
def browsewmfunc1():
    global txt
    filename = filedialog.askopenfilename()
    txt.insert(0,filename)

def browsewmfunc2():
    global txt1
    filename = filedialog.askopenfilename()
    txt1.insert(0,filename)

def clicked():
    global txt
    global txt1
    global lbl
    
    # watermark pdf file name 
    mywatermark = txt1.get()
     
    # original pdf file name 
    origFileName = txt.get()
      
    # new pdf file name 
    newFileName = 'watermarked_example.pdf'
      
    # creating pdf File object of original pdf 
    pdfFileObj = open(origFileName, 'rb') 
      
    # creating a pdf Reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
    # creating a pdf writer object for new pdf 
    pdfWriter = PyPDF2.PdfFileWriter() 
      
    # adding watermark to each page 
    for page in range(pdfReader.numPages): 
        # creating watermarked page object 
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page)) 
          
        # adding watermarked page object to pdf writer 
        pdfWriter.addPage(wmpageObj) 
  
    # new pdf file object 
    newFile = open(newFileName, 'wb') 
      
    # writing watermarked pages to new file 
    pdfWriter.write(newFile) 
    lbl.configure(text="Water Mark Added Successfully")
    # closing the original pdf file object 
    pdfFileObj.close() 
    # closing the new pdf file object 
    newFile.close()
def fileWaterMark():
    window = Tk()
    window.title("Document Watermarker")
    window.geometry('450x300')
    window.configure(background='violet')
    
    mrg1=Label(window,text='')
    mrg1.grid(column=0, row=0)
    mrg1.configure(background='violet')

    mrg2=Label(window,text='')
    mrg2.grid(column=1, row=1)
    mrg2.configure(background='violet')

    mrg3=Label(window,text='')
    mrg3.grid(column=2, row=2)
    mrg3.configure(background='violet')
    
    mrg4=Label(window,text='')
    mrg4.grid(column=3, row=3)
    mrg4.configure(background='violet')
    
    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=4)

    mrg5=Label(window,text='')
    mrg5.grid(column=4, row=6)
    global txt
    global txt1
    global lbl
    lbl = Label(window, text="Enter PDF File Path and WaterMark File Path",font=("Arial Bold", 10))
    lbl.grid(column=6, row=5)

    txt = Entry(window,width=40)
    txt.grid(column=6, row=7,columnspan=2)

    browsebutton1 = Button(window, text="Browse", command=browsewmfunc1)
    browsebutton1.grid(column=6, row=8)

    txt1 = Entry(window,width=40)
    txt1.grid(column=6, row=9,columnspan=2)

    browsebutton2 = Button(window, text="Browse", command=browsewmfunc2)
    browsebutton2.grid(column=6, row=10)
    
    btn = Button(window, text="Click Me",bg="orange", fg="white",command=clicked)
    btn.grid(column=6, row=11)

     
    window.mainloop()
