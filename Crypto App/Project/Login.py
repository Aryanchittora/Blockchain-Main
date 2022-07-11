from tkinter import *
from PIL import ImageTk, Image
import Account_Details

loginWin = Tk()
loginWin.title('Login')
loginWin.configure(background="#222222")
loginWin.minsize(width=400, height=350)
loginWin.maxsize(width=400, height=350)

img = ImageTk.PhotoImage(Image.open('Logo2.jpg'))
imgLabel = Label(loginWin, image=img, bg='#222222').pack(side='top')

frameLogin = Frame(loginWin, bg='#222222')

Label(frameLogin, text='Username - ', bg='#222222', fg='white', font=('Calibri', '12')).grid(row=0, column=0, pady=10, sticky=W)
name = Entry(frameLogin, font=('Calibri', '12'))
name.grid(row=0, column=1, pady=10, padx=5, sticky=W)

Label(frameLogin, text='Password - ', bg='#222222', fg='white', font=('Calibri', '12')).grid(row=1, column=0, pady=10, sticky=W)
password = Entry(frameLogin, font=('Calibri', '12'), show='*')
password.grid(row=1, column=1, pady=10, padx=5, sticky=W) 

def login():
    user = name.get()
    passwordEntry = password.get()

    if user == 'Aryan' and passwordEntry == 'arch1234':
        loginWin.destroy()
        Account_Details.eth()

Button(loginWin, text='Login', bg='#252830', fg='white', font=('JetBrains Mono', '12'), command=login, width=25).place(relx=0.5, rely=0.9, anchor=CENTER)

frameLogin.pack()

loginWin.mainloop()
