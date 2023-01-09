

import tkinter as tk

window = tk.Tk()
window.title('Calculator')

'''hello_world = tk.Label(window, text='Hello, World!')
hello_world.pack()


button1 = tk.Button(window, text='Button1')
button1.pack()

input = tk.Entry(window, width=10)
input.pack()

from tkinter import ttk
combolist = ttk.Combobox(window, width=20, state='readonly')
combolist.pack()

from tkinter import scrolledtext

multi_text = scrolledtext.ScrolledText(window, width=30, height=5, wrap=tk.WORD)
multi_text.pack()'''

first, second = 0, 0

str_value = tk.StringVar()
str_value.set(str(first))
display = tk.Entry(window, textvariable=str_value, justify='right').grid(columnspan=5, row=0)

operator=0


def number_click(number=0):
    global first, second
    if operator == 0:
        if str_value.get() == '0':
            str_value.set(str(number))
            first=number
        else:
            first *= 10
            first += number
            str_value.set(str(first))
    else:
        if str_value.get() == '0' or second == 0:
            str_value.set(str(number))
            second=number
        else:
            second *= 10
            second += number
            str_value.set(str(second))


def operator_click(op):
    global operator
    if op == '+':
        operator = 1
    elif op == '-':
        operator = 2
    elif op == 'x':
        operator = 3
    elif op == '/':
        operator = 4


def clear():
    global first
    first=0
    str_value.set('0')

def check_length(var):
    str_var = str(var)
    if len(str_var) > 9:
        return 'Error: Length Limits'
    else:
        return var


def calc_add(var1, var2):
    res = var1 + var2
    return check_length(res)


def calc_subtract(var1, var2):
    res = var1 - var2
    return check_length(res)


def calc_multiply(var1, var2):
    res = var1 * var2
    return check_length(res)


def calc_divide(var1, var2):
    if var2 == 0:
        return 'Error: Divide by Zero'
    else:
        res = var1 / var2
        return check_length(res)

def calculate():
    global first, second, operator
    if operator == 1:
        first = calc_add(first, second)
    elif operator == 2:
        first = first - second
    elif operator == 3:
        first = first * second
    elif operator == 4:
        first = first / second

    str_value.set(str(first))
    second = 0
    operator = 0


tk.Button(window, text='7', command=lambda: number_click(7)).grid(column=0, row=1)
tk.Button(window, text='8', command=lambda: number_click(8)).grid(column=1, row=1)
tk.Button(window, text='9', command=lambda: number_click(9)).grid(column=2, row=1)
tk.Button(window, text='C', command=clear).grid(column=3, columnspan=2, row=1)
tk.Button(window, text='4', command=lambda: number_click(4)).grid(column=0, row=2)
tk.Button(window, text='5', command=lambda: number_click(5)).grid(column=1, row=2)
tk.Button(window, text='6', command=lambda: number_click(6)).grid(column=2, row=2)
tk.Button(window, text='x', command=lambda: operator_click('x')).grid(column=3, row=2)
tk.Button(window, text='/', command=lambda: operator_click('/')).grid(column=4, row=2)
tk.Button(window, text='1', command=lambda: number_click(1)).grid(column=0, row=3)
tk.Button(window, text='2', command=lambda: number_click(2)).grid(column=1, row=3)
tk.Button(window, text='3', command=lambda: number_click(3)).grid(column=2, row=3)
tk.Button(window, text='+', command=lambda: operator_click('+')).grid(column=3, row=3, rowspan=2)
tk.Button(window, text='-', command=lambda: operator_click('-')).grid(column=4, row=3)
tk.Button(window, text='0', command=lambda: number_click(0)).grid(column=0, columnspan=2, row=4)
tk.Button(window, text='.').grid(column=2, row=4)
tk.Button(window, text='=', command=calculate).grid(column=4, row=4)


window.mainloop()





