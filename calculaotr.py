from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        master.title("CALCULATOR")
        master.geometry('510x600')
        master.config(bg='gray')
        master.resizable(True,True)
        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=43, bg='#ccddff',bd=5,relief='sunken',highlightthickness=2,highlightcolor='blue',justify='right', font=('Arial Bold',), textvariable=self.equation).place(x=6, y=0)
        
        Button(master, width=11, height=4, text='AC',relief='raised',bg='red', font=('Arial', 12, 'bold'), command=self.clear).place(x=10, y=40)
        Button(master, width=11, height=4, text='(', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('(')).place(x=130, y=40)
        Button(master, width=11, height=4, text=')', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show(')')).place(x=250, y=40)
        Button(master, width=11, height=4, text='/', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('/')).place(x=370, y=40)
        
        Button(master, width=11, height=4, text='X^2',relief='raised',bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('X^2')).place(x=10, y=130)
        Button(master, width=11, height=4, text='X^3', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('X^3')).place(x=130, y=130)
        Button(master, width=11, height=4, text='√', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('√')).place(x=250, y=130)
        Button(master, width=11, height=4, text='1/X', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('1/X')).place(x=370, y=130)
        
        Button(master, width=11, height=4, text='7', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(7)).place(x=10, y=220)
        Button(master, width=11, height=4, text='8', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(8)).place(x=130, y=220)
        Button(master, width=11, height=4, text='9', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(9)).place(x=250, y=220)
        Button(master, width=11, height=4, text='+', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('+')).place(x=370, y=220)
        
        Button(master, width=11, height=4, text='4', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(4)).place(x=10, y=310)
        Button(master, width=11, height=4, text='5', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(5)).place(x=130, y=310)
        Button(master, width=11, height=4, text='6', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(6)).place(x=250, y=310)
        Button(master, width=11, height=4, text='-', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('-')).place(x=370, y=310)
        
        Button(master, width=11, height=4, text='1', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(1)).place(x=10, y=400)
        Button(master, width=11, height=4, text='2', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(2)).place(x=130, y=400)
        Button(master, width=11, height=4, text='3', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(3)).place(x=250, y=400)
        Button(master, width=11, height=4, text='', relief='raised', bg='orange', font=('Arial', 12, 'bold'), command=lambda: self.show('')).place(x=370, y=400)
        
        Button(master, width=11, height=4, text='0', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show(0)).place(x=10, y=490)
        Button(master, width=11, height=4, text='.', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show('.')).place(x=130, y=490)
        Button(master, width=11, height=4, text='%', relief='raised', bg='white', font=('Arial', 12, 'bold'), command=lambda: self.show('%')).place(x=250, y=490)
        Button(master, width=11, height=4, text='=', relief='raised', bg='light blue', font=('Arial', 12, 'bold'), command=self.solve).place(x=370, y=490)
        

    def show(self, value):
        if value == 'X^2':
          if self.entry_value and self.entry_value[-1].isdigit():
            self.entry_value += '**2'
          else:
            self.entry_value += '0**2'
        elif value == 'X^3':
          if self.entry_value and self.entry_value[-1].isdigit():
            self.entry_value += '**3'
          else:
            self.entry_value += '0**3'
        elif value == '√':
            if self.entry_value and self.entry_value[-1].isdigit():
                self.entry_value += '**0.5'
            else:
                self.entry_value += '0**0.5'
        elif value == '1/X':
            if self.entry_value and self.entry_value[-1].isdigit():
                self.entry_value = '1/' + self.entry_value  
            else:
                self.entry_value += '1/'
        else:
         self.entry_value += str(value)
         self.equation.set(self.entry_value)
        

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()