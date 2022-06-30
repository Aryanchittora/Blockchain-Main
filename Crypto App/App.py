from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Crypto Banking')
root.configure(background='#000000')
root.geometry('400x500')

img = ImageTk.PhotoImage(Image.open('.\Crypto App\Logo.jpg'))
img_label = Label(root, image=img, bg='#000000').pack(side='top')

frame = Frame(root, bg='#000000', padx=5, pady=5)

Label(frame, text='Account 1 - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=0, column=0, pady=8, sticky=W)
Label(frame, text='Account 2 - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=1, column=0, pady=8, sticky=W)
Label(frame, text='Private Key - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=2, column=0, pady=8, sticky=W)
Label(frame, text='Ether Ammount - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=3, column=0, pady=8, sticky=W)
Label(frame, text='Gas Limit - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=4, column=0, pady=8, sticky=W)
Label(frame, text='Gas Price - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=5, column=0, pady=8, sticky=W)

frame.pack()

root.mainloop() 