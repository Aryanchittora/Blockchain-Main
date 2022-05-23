from web3 import Web3
from web3.middleware import geth_poa_middleware

API = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3_API = Web3(Web3.HTTPProvider(API))

block_data = web3_API.eth.get_block(14766453)
print('Block data -', block_data)

print('Gas Used -', block_data['gasUsed'])
print('Total Difficulty -', block_data['totalDifficulty'])
print('Transactions -', block_data['transactions'])

tranData = web3_API.eth.get_transaction('0x6de38f069cda3f56d3e52abc33db060f6c6601d4a097a50892a241c2c8047bbb')
print('\nTransaction Data -', tranData)