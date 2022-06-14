from web3 import Web3

url = 'HTTP://127.0.0.1:7545'
connect = Web3(Web3.HTTPProvider(url))

sender = '0x31643dCe300CCe519c802F7a1D6807D9a14d1c5f'
recipient = '0x5042CC3E721a8CD4fe4bd15E3Cc697e19e1F0b2a'
nonce = connect.eth.getTransactionCount(sender)

transaction = {
    'nonce': nonce,
    'to': recipient,
    'value': connect.toWei(1, 'ether'),
    'gas': 21000,
    'gasPrice': connect.toWei(50, 'gwei')
}

private_key = '71be5b31376249c2c42d8b1be4d59221ee2af64596cca1ff3762595d2771da67'

sign = connect.eth.account.signTransaction(transaction, private_key)
tx_hash = connect.eth.sendRawTransaction(sign.rawTransaction)

print(connect.toHex(tx_hash))