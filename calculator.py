from tkinter import *


def button_click(number):
    current = display.get()  
    display.delete(0, END)    
    display.insert(0, current + str(number))  


def evaluate():
    try:
        result = eval(display.get())  
        display.delete(0, END)
        display.insert(0, result)
    except Exception :
        display.delete(0, END)
        display.insert(0, "Error")


def clear():
    display.delete(0, END)


window = Tk()
window.geometry("380x440")
window.title("Calculator")


display = Entry(window, width=16, font=("Arial", 24), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, pady=10)


button_7 = Button(window, text="7", width=5, height=2, font=("Arial", 18), command=lambda: button_click(7))
button_8 = Button(window, text="8", width=5, height=2, font=("Arial", 18), command=lambda: button_click(8))
button_9 = Button(window, text="9", width=5, height=2, font=("Arial", 18), command=lambda: button_click(9))
button_4 = Button(window, text="4", width=5, height=2, font=("Arial", 18), command=lambda: button_click(4))
button_5 = Button(window, text="5", width=5, height=2, font=("Arial", 18), command=lambda: button_click(5))
button_6 = Button(window, text="6", width=5, height=2, font=("Arial", 18), command=lambda: button_click(6))
button_1 = Button(window, text="1", width=5, height=2, font=("Arial", 18), command=lambda: button_click(1))
button_2 = Button(window, text="2", width=5, height=2, font=("Arial", 18), command=lambda: button_click(2))
button_3 = Button(window, text="3", width=5, height=2, font=("Arial", 18), command=lambda: button_click(3))
button_0 = Button(window, text="0", width=5, height=2, font=("Arial", 18), command=lambda: button_click(0))


button_add = Button(window, text="+", width=5, height=2, font=("Arial", 18), command=lambda: button_click('+'))
button_sub = Button(window, text="-", width=5, height=2, font=("Arial", 18), command=lambda: button_click('-'))
button_mul = Button(window, text="*", width=5, height=2, font=("Arial", 18), command=lambda: button_click('*'))
button_div = Button(window, text="/", width=5, height=2, font=("Arial", 18), command=lambda: button_click('/'))
button_point = Button(window, text=".", width=5, height=2, font=("Arial", 18), command=lambda: button_click('.'))

button_eq = Button(window, text="=", width=5, height=2, font=("Arial", 18), command=evaluate)
button_clear = Button(window, text="C", width=5, height=2, font=("Arial", 18), command=clear)

button_clear.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)


button_point.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_div.grid(row=5, column=3)
button_eq.grid(row=5, column=2)


window.mainloop()
