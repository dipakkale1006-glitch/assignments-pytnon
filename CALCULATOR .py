from tkinter import *
window=Tk()
window.title("CALCULATOR")
window.geometry("300x300")

def click(num):
     result=e.get()
     e.delete(0,END)
     e.insert(0,str(result)+str(num))

e=Entry(window,width=50,borderwidth=5)
e.place(x=0,y=0)


def cler():
     e.delete(0,END)
b=Button(window,text='AC',width=10,command=cler)
b.place(x=0,y=40)

# EXTRA TWO BUTTON
b=Button(window,text='.',width=10,)
b.place(x=140,y=160)

b=Button(window,text='%',width=10,)
b.place(x=70,y=40)

def cler():
    e.delete(len(e.get())-1,END)
b=Button(window,text='x',width=10, command=cler,fg='red')
b.place(x=140,y=40)


b=Button(window,text='1',width=10,command=lambda:click(1),bg='gray',fg='white')
b.place(x=0,y=130)

b=Button(window,text='2',width=10,command=lambda:click(2),bg='gray',fg='white')
b.place(x=70,y=130)

b=Button(window,text='3',width=10,command=lambda:click(3),bg='gray',fg='white')
b.place(x=140,y=130)

b=Button(window,text='4',width=10,command=lambda:click(4),bg='gray',fg='white')
b.place(x=0,y=100)

b=Button(window,text='5',width=10,command=lambda:click(5),bg='gray',fg='white')
b.place(x=70,y=100)

b=Button(window,text='6',width=10,command=lambda:click(6),bg='gray',fg='white')
b.place(x=140,y=100)

b=Button(window,text='7',width=10,command=lambda:click(7),bg='gray',fg='white')
b.place(x=0,y=70)

b=Button(window,text='8',width=10,command=lambda:click(8),bg='gray',fg='white')
b.place(x=70,y=70)

b=Button(window,text='9',width=10,command=lambda:click(9),bg='gray',fg='white')
b.place(x=140,y=70)

b=Button(window,text='00',width=10,command=lambda:click(00),bg='gray',fg='white')
b.place(x=0,y=160)

b=Button(window,text='0',width=10,command=lambda:click(0),bg='gray',fg='white')
b.place(x=70,y=160)

def add():
    n1 = e.get()
    global math
    math ='addition'
    global i
    i = int(n1)
    e.delete(0,END)
b=Button(window,text='+',width=10,command=add)
b.place(x=210,y=130)

def sub():
    n1 = e.get()
    global math
    math ='subtraction'
    math=sub
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='-',width=10,command=sub,)
b.place(x=210,y=100)

def mul():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='*',width=10,command=mul)
b.place(x=210,y=70)

def div():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='/',width=10,command=div)
b.place(x=210,y=40)


def equal():
    n2 = e.get()
    e.delete(0,END)
    if math =='addition':
       e.insert(0,i + int(n2))
    elif math =='subtraction':
         e.insert(0, i - int(n2))
    elif math =='multiplication':
        e.insert(0, i * int(n2))
    elif math =='division':
        e.insert(0, i / int(n2))

b=Button(window,text='=',width=10,command=equal)
b.place(x=210,y=160)

window.mainloop()

