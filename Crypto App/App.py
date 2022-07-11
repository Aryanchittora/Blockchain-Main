from tkinter import messagebox
from web3 import Web3
from tkinter import *
from PIL import ImageTk, Image

url = 'https://kovan.infura.io/v3/f4b23112ae6c4e4e8e5a357d01a522a8'
kovan = Web3(Web3.HTTPProvider(url))

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
Label(frame, text='Gas Limit (GWEI) - ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=4, column=0, pady=8, sticky=W)
Label(frame, text='Gas Price - (GWEI) ', fg='#50d2fa', bg='#000000', font=('Bold', '12')).grid(row=5, column=0, pady=8, sticky=W)

account1 = Entry(frame)
account2 = Entry(frame)
privateKey = Entry(frame)
ammount = Entry(frame)
gas_limit = Entry(frame)
gas_price = Entry(frame)

account1.grid(row=0, column=1, pady=8, padx=8, sticky=W)
account2.grid(row=1, column=1, pady=8, sticky=W, padx=8)
privateKey.grid(row=2, column=1, pady=8, padx=8, sticky=W)
ammount.grid(row=3, column=1, pady=8, padx=8, sticky=W)
gas_limit.grid(row=4, column=1, pady=8, padx=8, sticky=W)
gas_price.grid(row=5, column=1, pady=8, padx=8, sticky=W)

frame.pack()

def sendETH():
    account1_id = account1.get()
    account2_id = account2.get()
    private_key = privateKey.get()
    Ether = ammount.get()
    gasLimit = gas_limit.get()
    gasPrice = gas_price.get()
    nonce = kovan.eth.getTransactionCount(account1_id)

    transaction = {
        'nonce': nonce,
        'to': account2_id,
        'value': kovan.toWei(Ether, 'ether'),
        'gas': int(gasLimit),
        'gasPrice': kovan.toWei(gasPrice, 'gwei')
    }

    sign = kovan.eth.account.signTransaction(transaction, private_key)
    tx_hash = kovan.eth.sendRawTransaction(sign.rawTransaction)

    print('Transaction Successful! Id - ', kovan.toHex(tx_hash))
    messagebox.showinfo('Transaction Successful !!', f'Transaction successfully signed please verify the transaction, here is the transaction ID - {kovan.toHex(tx_hash)}')

send = Button(root, text='Transfer ETH', font=('Italic', '13'), command=sendETH, highlightbackground='white')
send.pack(fill='both')


root.mainloop() 