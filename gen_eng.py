import random
from tkinter import *
from tkinter import ttk

characters = ('A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'Ö', 'Ő',
              'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ü', 'Ű', 'V', 'Z', 'a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h',
              'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v',
              'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '_', '-', '?', '!', '/', '*')

def gen():
    number = int(db.get())
    password = ''
    num = number
    if number == 0:
        ttk.Label(root, text="Enter a number!", width=80, background='red').grid(row=2, column=0, columnspan=2)
    if number > 0:
        while num != 0:
            passw = '{}'.format(password) + '{}'.format(random.choice(characters))
            num -= 1
            password = passw
        ttk.Label(root, text="The generated password", width=40).grid(row=2, column=0)
        p = ttk.Entry(root, width=40)
        p.grid(row=2, column=1)
        p.insert(0, password)


root = Tk()


root.resizable(False, False)

root.title('Welcome to the password generator!')
root.config(bg='#DCDCDC')

ttk.Label(root, text="How long will be your password?", width=40).grid(row=0, column=0)
db = ttk.Entry(root, width=40)
db.grid(row=0, column=1)
db.insert(0, '0')

Button(root, text='Generate', command=gen, width=40).grid(row=1, column=0, columnspan=2)

root.mainloop()