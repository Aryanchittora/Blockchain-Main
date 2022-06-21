from web3 import Web3
import time

url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(url))

account1 = '0x2a6F08f5A6A749b390aca713F66dF4096D575255'
account2 = '0x8364f8f9A4082F48A695B5b13Cd58DAe070d6643'
account3 = '0x05608F2841CF8A7cb633cC1E910af256BE0153a8'

private_key = '0091d2d56bd18a0d731f702e9df465e474fd0722c78452b3b2bb686d6b500170'
private_key2 = 'eaebfdd82e15f37c2f96b4a375b797a845b1e4372dc306408d8bb5b400d19e62'

nonce = web3.eth.getTransactionCount(account1)
nonce2 = web3.eth.getTransactionCount(account3)

transaction1 = {
    'nonce': nonce,
    'to': account2,
    'value': web3.toWei(15, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei(50, 'gwei')
}

sign1 = web3.eth.account.signTransaction(transaction1, private_key)
tx_hash1 = web3.eth.sendRawTransaction(sign1.rawTransaction)

print(f'Transaction 1 - {web3.toHex(tx_hash1)}')

print('Please Wait...')
time.sleep(5)

transaction2 = {
    'nonce': nonce2,
    'to': account2,
    'value': web3.toWei(10, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei(50, 'gwei')
}

sign2 = web3.eth.account.signTransaction(transaction2, private_key2)
tx_hash2 = web3.eth.sendRawTransaction(sign2.rawTransaction)

print(f'Transaction 2 - {web3.toHex(tx_hash2)}')