from web3 import Web3
from web3.middleware import geth_poa_middleware

API = 'https://mainnet.infura.io/v3/b1ba1b2a375249b484fa1b643f4f7fee'
web3 = Web3(Web3.HTTPProvider(API))

block = web3.eth.get_block(14791590)
transaction = web3.eth.get_transaction('0x6ce921d1ebdbd267081950b070b71c27d9ce3ae10bfa604e8cc5651fc8aaa046')

print('Block Hash:', transaction['blockHash'].hex())
print('Block Number:', transaction['blockNumber'])
print('from :', transaction['from'])
print('to:', transaction['to'])
print('input:', transaction['input'])
print('gas :', transaction['gas'])
print('Gas Price In Ether:', transaction['gasPrice'])
print('hash:', transaction['hash'].hex())
print('nonce:', transaction['nonce'])
print('Signature:', transaction['s'].hex())
print('values:', transaction['value'])