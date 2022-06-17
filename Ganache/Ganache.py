from web3 import Web3

url = 'HTTP://127.0.0.1:7545'
connect = Web3(Web3.HTTPProvider(url))

sender = '0xC85Fd27c6F3D6C43282ff55e5433245A0526269E'
recipient = '0x20c76de49A64c819Be642715D576Cb324Ed4C1E8'
nonce = connect.eth.getTransactionCount(sender)

transaction = {
    'nonce': nonce,
    'to': recipient,
    'value': connect.toWei(10, 'ether'),
    'gas': 21000,
    'gasPrice': connect.toWei(50, 'gwei')
}

private_key = '6175219490c9bd59706fb4b14b78f7c81a219325b8b46be5a97bd6fc91d909da'

sign = connect.eth.account.signTransaction(transaction, private_key)
tx_hash = connect.eth.sendRawTransaction(sign.rawTransaction)

print(connect.toHex(tx_hash))