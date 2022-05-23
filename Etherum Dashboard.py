from web3 import Web3
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2, font=('bold', 15))
block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.4, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

url = 'https://mainnet.infura.io/v3/b1ba1b2a375249b484fa1b643f4f7fee'
API = Web3(Web3.HTTPProvider(url))

def ethereum_block():
    block_num = block_entry.get()
    try:
        block = API.eth.get_block(block_num)
        block_name_label['text'] = str(block["number"])
    except(ValueError):
        block = API.eth.get_block(int(block_num))

    transaction = API.eth.get_transaction(block["transactions"][-1].hex())
    value = transaction["value"]/10**18
    dollarValue = value * 2024
    gas = transaction["gas"]

    gasused_info_label['text'] = 'Value - $' + str(dollarValue)
    gaslimit_info_label['text'] = 'gas -' + str(gas)

    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=RAISED)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()

