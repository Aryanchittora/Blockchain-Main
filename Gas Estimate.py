from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(infura_url)) #establish the connection

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json') #get the data from the API in json format.
latest_block_info = json.loads(req_ethgas_data.content) # convert the json formatted data to normal data.

#access various costs of transactions depending upon the speed.
print('safeLow', latest_block_info['safeLow'])
print('average', latest_block_info['average'])
print('fast', latest_block_info['fast'])
print('fastest', latest_block_info['fastest'])
print('Block number:', latest_block_info['blockNum'])

gas_price = web3.eth.gasPrice
print(gas_price)
gasEther = gas_price/10**9
print('Gas Price (Ether) -', gasEther)
gasDollar = gasEther * 1953.43
print('Gas Price ($) -', '$' + str(gasDollar))

block = web3.eth.get_block(1352346)
# print('block Data', block) 
latest_transaction = block['transactions'][-1].hex()
print('transaction hash -', latest_transaction)
transaction_data = web3.eth.get_transaction(latest_transaction)
gas_estimate = web3.eth.estimateGas({'to':transaction_data['to'], 'from':transaction_data['from']})
print('Gas used -', gas_estimate)
print('Gas limit -', transaction_data['gas'])