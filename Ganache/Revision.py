from web3 import Web3

url = 'HTTP://127.0.0.1:7545'
web3_API = Web3(Web3.HTTPProvider(url))

account1 = '0xF2199B58358D98fA48e2B2bfaf3b3759fE01Ee8e'
account2 = '0xC9A6244a197A1823F1FCCbe5620Df334571BDfB8'
private_key = '3f787134558526cc92b43668b8ee5d02580b4b1daaa200235f90716c1de5ad72'
nonce = web3_API.eth.getTransactionCount(account1)

transaction = {
    'nonce': nonce,
    'to': account2,
    'value': web3_API.toWei(5, 'ether'),
    'gas': 22`000,
    'gasPrice': web3_API.toWei(0.00025, 'gwei')
}

sign = web3_API.eth.account.signTransaction(transaction, private_key)
tx_hash = web3_API.eth.sendRawTransaction(sign.rawTransaction)

print('Transaction 1 -', web3_API.toHex(tx_hash))