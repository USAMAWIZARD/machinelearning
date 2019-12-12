#tic tac toe with ai
from tkinter import *
from functools import partial
def clicked(a):
    btn[a].config(text="X", font=("Bold",9))
window= Tk()
window.title("Tic Tac Toe")
window.geometry('500x500')
btn=[None]*9
btno=0
for i in range(10,40,10):
    for p in range(10,40,10):
        action_with_arg = partial(clicked,btno)
        btn[btno] = Button(window,command=action_with_arg)
        btn[btno].grid(column=p, row=i)
        btn[btno].config(height=10,width=20)
        btno+=1
window.mainloop()