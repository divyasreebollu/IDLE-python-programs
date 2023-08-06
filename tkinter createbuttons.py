from tkinter import *
def buttonClick(self):
    print('you have clicked me')
root=Tk()
b=Button(root,text='click',width=20,height=4,bg='yellow',fg='orange',activebackground='green',activeforeground='whitefro')
b.pack()
b.bind("<Button-1>",buttonClick)
root.mainloop()
