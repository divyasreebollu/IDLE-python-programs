import tkinter as tk
from tkinter import *
root=tk.Tk()
A=Label(root,text="username").place(x=40,y=60)
B=Label(root,text="password").place(x=40,y=100)
C=Button(root,text="submit").place(x=90,y=140)
D=Entry(root,width=30).place(x=110,y=60)
E=Entry(root,width=30).place(x=110,y=100)
root.mainloop()
