from tkinter import *
from GUI import *
from GUICodeSimilar import *
from GUIFilePlagarismChecker import *
from GUIDocumentEncrypt import *
from GUIDocumentWatermark import *
root = Tk()

root.geometry('650x700')
w = Button(root, text="Stylometric Analysis", bg="red", fg="white",command=stylo)
w.pack(fill=X,padx=40,pady=40)
w = Button(root, text="Degree of Similarity between Two Python Code Files", bg="grey", fg="white",command=pySimilar)
w.pack(fill=X,padx=40,pady=40)
w = Button(root, text="Degree of Similarity between Two Files", bg="white", fg="black",command=fileSimilar)
w.pack(fill=X,padx=40,pady=40)
w = Button(root, text="Plagarism in Website", bg="blue", fg="white")
w.pack(fill=X,padx=40,pady=40)
w = Button(root, text="Document Locker", bg="orange", fg="white",command=fileEncrypt)
w.pack(fill=X,padx=40,pady=40)
w = Button(root, text="Document Watermarker", bg="violet", fg="white",command=fileWaterMark)
w.pack(fill=X,padx=40,pady=40)

mainloop()
