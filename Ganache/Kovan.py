from web3 import Web3

url = 'https://kovan.infura.io/v3/f4b23112ae6c4e4e8e5a357d01a522a8'
api = Web3(Web3.HTTPProvider(url))

sender = '0xD385F13fF30D8f75d9f226f2bCcc0f58df366D17'
receiever = '0xAFb401234fE0b4060EE45c7e0004270951a8B0c9'
private_key = 'b020015166bc7023d1d7aa493a5e7710a628d66b83f82320fb00ac388ebaee88'
nonce = api.eth.getTransactionCount(sender)

transaction = {
    'nonce': nonce,
    'to': receiever,
    'value': api.toWei(0.1, 'ether'),
    'gas': 21000,
    'gasPrice': api.toWei(50, 'gwei')
}

sign = api.eth.account.signTransaction(transaction, private_key)
tx_hash = api.eth.sendRawTransaction(sign.rawTransaction)

print('Transaction Hash -', api.toHex(tx_hash))