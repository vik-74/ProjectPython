from tkinter import *
import math
root = Tk()
root.geometry("265x400")
root.title("Calculator")
root.config(background="Lightgreen")
root_list=[b'\xd0\xa2\xd1\x8b ', 
           b'\xd0\xb4\xd0\xb5\xd0\xb1\xd0\xb8\xd0\xbb ',
           b'\xd0\xb1\xd0\xbb\xd1\x8f\xd1\x82\xd1\x8c ',
           b'\xd0\xb5\xd0\xb1\xd0\xb0\xd0\xbd\xd1\x8b\xd0\xb9']

rootres = ""
expression = ""

result = StringVar()
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=4, ipadx=70)

for root_num in root_list: 
    rootres = rootres + root_num.decode()
error=str(rootres)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)

def equalpress():
    try:
        global expression
        expression = expression.replace("^","**")
        total =str(eval(expression))
        result.set(total)
        #expression = "total" # Это не нужно
    except:
        result.set(error)

def deletepress():
    global expression
    expression = ""
    result.set(expression)

def factorialpress():
    try:
        global expression
        expression.replace("!","")
        num = int(expression)
        factorial = 1
        for num in range(2, num + 1):
            factorial = factorial * num
        result.set(factorial)
    except:
        result.set(error)

def hyperfactorialpress():
    try:
        global expression
        factorial = 1
        for num in range(2, int(expression) + 1):
            factorial = factorial * (num ** num)
        result.set(factorial)
    except:
        result.set(error)

def rootpress():
    try:
        global expression
        expression = expression.replace("√", "**")
        total = str(eval(expression))
        result.set(total)

    except:
        result.set(error)
def logpress():
    pass

def percent_to_decimal():
    pass

def decimal_to_percent():
    pass

button1 = Button(text="1", height=1, width=7, command=lambda: press_num(1))
button1.grid(row=2, column=0)

button2 = Button(text="2", height=1, width=7, command=lambda: press_num(2))
button2.grid(row=2, column=1)

button3 = Button(text="3", height=1, width=7, command=lambda: press_num(3))
button3.grid(row=2, column=2)

button4 = Button(text="4", height=1, width=7, command=lambda: press_num(4))
button4.grid(row=3, column=0)

button5 = Button(text="5", height=1, width=7, command=lambda: press_num(5))
button5.grid(row=3, column=1)

button6 = Button(text="6", height=1, width=7, command=lambda: press_num(6))
button6.grid(row=3, column=2)

button7 = Button(text="7", height=1, width=7, command=lambda: press_num(7))
button7.grid(row=4, column=0)

button8 = Button(text="8", height=1, width=7, command=lambda: press_num(8))
button8.grid(row=4, column=1)

button9 = Button(text="9", height=1, width=7, command=lambda: press_num(9))
button9.grid(row=4, column=2)

plus = Button(text="+", height=1, width=7, command=lambda: press_num("+"))
plus.grid(row=5, column=0)

button0 = Button(text="0", height=1, width=7,command=lambda: press_num(0))
button0.grid(row=5, column=1)

minus = Button(text="-", height=1, width=7, command=lambda: press_num("-"))
minus.grid(row=5, column=2)

equal = Button(text="=", height=1, width=7, command=lambda: equalpress())
equal.grid(row=6, column=1)

multiply = Button(text="*", height=1, width=7, command=lambda: press_num("*"))
multiply.grid(row=6, column=2)

divide = Button(text="/", height=1, width=7, command=lambda: press_num("/"))
divide.grid(row=6, column=0)

delete = Button(text="C", height=1, width=7, command=lambda: deletepress())
delete.grid(row=7, column=2)

exponent = Button(text="^", height=1, width=7, command=lambda: press_num("^"))
exponent.grid(row=7, column=0)

factorial = Button(text="!", height=1, width=7, command=lambda: factorialpress())
factorial.grid(row=7, column=1)

hfactorial = Button(text="H()", height=1, width=7, command=lambda: hyperfactorialpress())
hfactorial.grid(row=8, column=1)

rootd = Button(text="√", height=1, width=7, command=lambda:press_num("√"))
rootd.grid(row=8, column=0)

root.mainloop()