from tkinter import *
import math

#basic code 
root=Tk()

#defining title 
root.title("Calculator")

#definig icon 
root.iconbitmap("D:\GUI\calculator\calculator.ico")

#display bar to show input and outputs 
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=1,columnspan=3,pady=20)


#display numbers
def button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

#clear button
def buttonclear():
    e.delete(0,END)
    
#add button
def buttonadd():
    first=e.get()
    global fn
    global abc
    abc=str('addition')
    fn=float(first)
    e.delete(0,END)

#subtract button
def buttonsub():
    first=e.get()
    global fn
    global abc
    abc=str('subtraction')
    fn=float(first)
    e.delete(0,END)

#multiplication button 
def buttonmul():
    first=e.get()
    global fn
    global abc
    abc=str('multiplication')
    fn=float(first)
    e.delete(0,END)
 
#divide button 
def buttondiv():
    first=e.get()
    global fn
    global abc
    abc=str('division')
    fn=float(first)
    e.delete(0,END)

#modulus button 
def buttonmodulus():
    first=e.get()
    global fn
    global abc
    abc=str('modulus')
    fn=int(first)
    e.delete(0,END) 

#power button     
def buttonpow():
    first=e.get()
    global fn
    global abc
    abc=str('power')
    fn=float(first)
    e.delete(0,END)

#factorial button
def buttonfact():
    first=e.get()
    global fn
    global abc
    abc=str('fact1')
    fn=int(first)
    e.delete(0,END)

#square root button
def buttonsqrt():
    first=e.get()
    global fn
    global abc
    abc=str('square root')
    fn=float(first)
    e.delete(0,END)

#sine function button    
def buttonsin():
    first=e.get()
    global fn
    global abc
    abc=str('sin')
    fn=float(first)
    e.delete(0,END)
 
#cosine function button
def buttoncos():
    first=e.get()
    global fn
    global abc
    abc=str('cos')
    fn=float(first)
    e.delete(0,END)
 
#tan function button
def buttontan():
    first=e.get()
    global fn
    global abc
    abc=str('tan')
    fn=float(first)
    e.delete(0,END)
    
#define equal
def buttonequal():
    if abc=='fact1':
        if fn=='0':
            e.insert(0,'1')
        else:
            s=int(fn)
            x=1
            temp=1
            while(x!=s+1):
                temp=temp*x
                x=x+1
            e.insert(0,temp)
    elif abc=='square root':
       e.insert(0,float(fn) ** (0.5))
    elif abc=='sin':
        s=float(fn)
        x=math.sin(s)
        e.insert(0,x)
    elif abc=='cos':
        s=float(fn)
        x=math.cos(s)
        e.insert(0,x)
    elif abc=='tan':
        s=float(fn)
        x=math.tan(s)
        e.insert(0,x)
    else:
        second=e.get()
        e.delete(0,END)
        if abc=='addition':
            e.insert(0,float(fn) + float(second))
        if abc=='subtraction':
            e.insert(0,float(fn) - float(second))
        if abc=='multiplication':
            e.insert(0,float(fn) * float(second))
        if abc=='division':
            e.insert(0,float(fn) / float(second))
        if abc=='modulus':
           e.insert(0,int(fn) % int(second))
        if abc=='power':
           e.insert(0,float(fn) ** int(second))
    



#defining buttons
button1=Button(root,text="1",padx=25,pady=10,command=lambda:button(1),bg='grey',fg='white')
button2=Button(root,text="2",padx=25,pady=10,command=lambda:button(2),bg='grey',fg='white')
button3=Button(root,text="3",padx=25,pady=10,command=lambda:button(3),bg='grey',fg='white')
button4=Button(root,text="4",padx=25,pady=10,command=lambda:button(4),bg='grey',fg='white')
button5=Button(root,text="5",padx=25,pady=10,command=lambda:button(5),bg='grey',fg='white')
button6=Button(root,text="6",padx=25,pady=10,command=lambda:button(6),bg='grey',fg='white')
button7=Button(root,text="7",padx=25,pady=10,command=lambda:button(7),bg='grey',fg='white')
button8=Button(root,text="8",padx=25,pady=10,command=lambda:button(8),bg='grey',fg='white')
button9=Button(root,text="9",padx=25,pady=10,command=lambda:button(9),bg='grey',fg='white')
button0=Button(root,text="0",padx=25,pady=10,command=lambda:button(0),bg='grey',fg='white')
button_dot=Button(root,text=".",padx=10,pady=2,command=lambda:button('.'),bg='grey',fg='white')
button_add=Button(root,text="+",padx=24,pady=10,command=buttonadd,bg='black',fg='white')
button_subtract=Button(root,text="-",padx=25,pady=10,command=buttonsub,bg='black',fg='white')
button_multiply=Button(root,text="*",padx=25,pady=10,command=buttonmul,bg='black',fg='white')
button_divide=Button(root,text="/",padx=25,pady=10,command=buttondiv,bg='black',fg='white')
button_equals=Button(root,text="=",padx=23,pady=10,command=buttonequal,bg='blue',fg='white')
button_modulus=Button(root,text="%",padx=23,pady=10,command=buttonmodulus,bg='black',fg='white')
button_power=Button(root,text="^",padx=24,pady=10,command=buttonpow,bg='black',fg='white')
button_fact=Button(root,text="x!",padx=23,pady=10,command=buttonfact,bg='black',fg='white')
button_clear=Button(root,text="clear ",padx=13,pady=10,command=buttonclear,bg='red',fg='white')
button_sqrt=Button(root,text="sq",padx=22,pady=10,command=buttonsqrt,bg='black',fg='white')
button_sin=Button(root,text="sin",padx=20,pady=10,command=buttonsin,bg='black',fg='white')
button_cos=Button(root,text="cos",padx=19,pady=10,command=buttoncos,bg='black',fg='white')
button_tan=Button(root,text="tan",padx=19,pady=10,command=buttontan,bg='black',fg='white')
button_exit=Button(root,text="exit",padx=18.5,pady=10,command=root.destroy,bg='black',fg='white')


#fitting buttons in calculator
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=3)
button0.grid(row=4,column=2)
button_add.grid(row=4,column=1)
button_subtract.grid(row=4,column=3)
button_multiply.grid(row=4,column=4)
button_divide.grid(row=3,column=4)
button_equals.grid(row=2,column=4)
button_clear.grid(row=1,column=4)
button_modulus.grid(row=5,column=1)
button_power.grid(row=5,column=2)
button_fact.grid(row=5,column=3)
button_sqrt.grid(row=5,column=4)
button_sin.grid(row=6,column=1)
button_cos.grid(row=6,column=2)
button_tan.grid(row=6,column=3)
button_dot.grid(row=0,column=4)
button_exit.grid(row=6,column=4)

root.mainloop()