from tkinter  import *
from tkinter import messagebox
window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x300")
chance=1
def click1():
    global chance
    if b1["text"]==" ":
        if chance==1:
            chance=2
            b1["text"]="X"
        elif chance==2:
            chance=1
            b1["text"]="O"    
        check()    
    
def click2():
    global chance
    if b2["text"]==" ":
        if chance==1:
            chance=2
            b2["text"]="X"
        elif chance ==2:
            chance=1
            b2["text"]="O"
        check()      
    
def click3():
    global chance
    if b3["text"]==" ":
        if chance==1:
            chance=2
            b3["text"]="X"
        elif chance ==2:
            chance=1
            b3["text"]="O"
        check()      
    
def click4():
    global chance
    if b4["text"]==" ":
        if chance==1:
            chance=2
            b4["text"]="X"
        elif chance ==2:
            chance=1
            b4["text"]="O"
        check()      
    
def click5():
    global chance
    if b5["text"]==" ":
        if chance==1:
            chance=2
            b5["text"]="X"
        elif chance ==2:
            chance=1
            b5["text"]="O"
        check()      
    
def click6():
    global chance
    if b6["text"]==" ":
        if chance==1:
            chance=2
            b6["text"]="X"
        elif chance ==2:
            chance=1
            b6["text"]="O"
        check()      
    
def click7():
    global chance
    if b7["text"]==" ":
        if chance==1:
            chance=2
            b7["text"]="X"
        elif chance ==2:
            chance=1
            b7["text"]="O"
        check()      
    
def click8():
    global chance
    if b8["text"]==" ":
        if chance==1:
            chance=2
            b8["text"]="X"
        elif chance ==2:
            chance=1
            b8["text"]="O"
        check()      
    
def click9():
    global chance
    if b9["text"]==" ":
        if chance==1:
            chance=2
            b9["text"]="X"
        elif chance ==2:
            chance=1
            b9["text"]="O"
        check()      
     
counter=1      
def check():
    global counter
    btn1=b1["text"]
    btn2=b2["text"]
    btn3=b3["text"]
    btn4=b4["text"]
    btn5=b5["text"]
    btn6=b6["text"]
    btn7=b7["text"]
    btn8=b8["text"]
    btn9=b9["text"]
    counter= counter+1
    if btn1 == btn2 and btn2 == btn3 and btn3 == "X" or btn1 == btn2 and btn2 == btn3 and btn3 == "O":
        winner(btn1)
    if btn4 == btn5 and btn5 == btn6 and btn4 == "X" or btn4 == btn5 and btn5 == btn6 and btn4 == "O":
        winner(btn4)
    if btn7 == btn8 and btn8 == btn9 and btn7 == "X" or btn7 == btn8 and btn8 == btn9 and btn7 == "O":
        winner(btn7)
    if btn1 == btn4 and btn4 == btn7 and btn1 == "X" or btn1 == btn4 and btn4 == btn7 and btn1 == "O":
        winner(btn1)
    if btn1 == btn5 and btn5 == btn9 and btn1 == "X" or btn1 == btn5 and btn5 == btn9 and btn1 == "O":
        winner(btn1)
    if btn2 == btn5 and btn5 == btn8 and btn2 == "X" or btn2 == btn5 and btn5 == btn8 and btn2 == "O":
        winner(btn2)
    if btn3 == btn6 and btn6 == btn9 and btn3 == "X" or btn3 == btn6 and btn6 == btn9 and btn3 == "O":
        winner(btn3)
    if btn3 == btn5 and btn5 == btn7 and btn3 == "X" or btn3 == btn5 and btn5 == btn7 and btn3 == "O":
        winner(btn3)
    if counter == 10:
        messagebox.showinfo("Match Tie", "Try again!!")    
        window.destroy()
 
def winner(player):
    if player=="X":
        messagebox.showinfo("Congratulations", "Player--1 Wins")    
        window.destroy()
    elif player=="O":
        messagebox.showinfo("Congratulations", "Player--2 Wins")    
        window.destroy()
      

lab1=Label(window,text="Player 1---X",font="Times  20")
lab1.grid(row=1,column=0)
lab2=Label(window,text="Player 2---O",font="Times  20")
lab2.grid(row=2,column=0)
lab3=Label(window,text="Tic-Tac-Toe",font="Times 20")
lab3.grid(row=0,column=0)
b1=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click1)
b1.grid(row=1,column=1)
b2=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click2)
b2.grid(row=1,column=2)
b3=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click3)
b3.grid(row=1,column=3)
b4=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click4)
b4.grid(row=2,column=1)
b5=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click5)
b5.grid(row=2,column=2)
b6=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click6)
b6.grid(row=2,column=3)
b7=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click7)
b7.grid(row=3,column=1)
b8=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click8)
b8.grid(row=3,column=2)
b9=Button(window, text=" ",bg="red",fg="white",width=3,height=1,font=('times','20'),command=click9)
b9.grid(row=3,column=3)

window.mainloop()
