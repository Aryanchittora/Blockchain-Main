from web3 import Web3
from tkinter import *
from PIL import Image, ImageTk

url = 'HTTP://127.0.0.1:7545'
api = Web3(Web3.HTTPProvider(url))


count = 1

entry_1 = ''
entry_2 = ''
entry_3 = ''
entry_4 = ''
entry_5 = ''
text_area = ''
main = ''


def eth():
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    global entry_5
    global text_area
    global main

    main = Tk()
    main.configure(background='#222222')
    main.title('Account Details')
    main.geometry('400x600')

    img = ImageTk.PhotoImage(Image.open('Logo2.jpg'))
    img_label = Label(main, image=img, bg='#222222').pack(side='top')

    frame = Frame(main, bg='#222222')

    Label(frame, text='Account 1 - ', bg='#222222', fg='#f2f5fa', font=('Italic', '13')).grid(row=0, column=0, pady=10, sticky=W)
    entry_1 = Entry(frame, font=('Italic', '13'), relief=FLAT)
    entry_1.grid(row=0, column=1, pady=10, sticky=W)

    Label(frame, text='Account 2 - ', bg='#222222', fg='#f2f5fa', font=('Italic', '13')).grid(row=1, column=0, pady=10, sticky=W)
    entry_2 = Entry(frame, font=('Italic', '13'), relief=FLAT)
    entry_2.grid(row=1, column=1, pady=10, sticky=W)

    Label(frame, text='Account 3 - ', bg='#222222', fg='#f2f5fa', font=('Italic', '13')).grid(row=2, column=0, pady=10, sticky=W)
    entry_3 = Entry(frame, font=('Italic', '13'), relief=FLAT)
    entry_3.grid(row=2, column=1, pady=10, sticky=W)

    Label(frame, text='Account 4 - ', bg='#222222', fg='#f2f5fa', font=('Italic', '13')).grid(row=3, column=0, pady=10, sticky=W)
    entry_4 = Entry(frame, font=('Italic', '13'), relief=FLAT)
    entry_4.grid(row=3, column=1, pady=10, sticky=W)

    Label(frame, text='Account 5 - ', bg='#222222', fg='#f2f5fa', font=('Italic', '13')).grid(row=4, column=0, pady=10, sticky=W)
    entry_5 = Entry(frame, font=('Italic', '13'), relief=FLAT)
    entry_5.grid(row=4, column=1, pady=10, sticky=W)

    frame.pack()

    text_area = Text(main, width=40, height=15, font=('Italic', '13'))
    text_area.configure(state='disabled')
    text_area.place(relx=0.5, rely=0.95, anchor=CENTER)

    button()

    loop()


def balance():
    global count

    account_no = []
    account_no.append(entry_1.get())
    account_no.append(entry_2.get())
    account_no.append(entry_3.get())
    account_no.append(entry_4.get())
    account_no.append(entry_5.get())
    print(account_no)

    for i in account_no:
        account_balance = api.eth.getBalance(i)
        ether = api.fromWei(account_balance, 'ether')
        
        text_area.configure(state='normal')
        text_area.insert(END, f'Account {count} has {ether} ETH\n')
        text_area.configure(state='disabled')

        count = count + 1

def button():
        Button(main, text='Check Balance', font=('Italic', '13'), bg='#222222', fg='#f2f5fa', command=balance, relief=FLAT).place(relx=0.5, rely=0.68, anchor=CENTER)

def loop():
    main.mainloop()
