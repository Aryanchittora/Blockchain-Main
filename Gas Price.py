from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import requests

API_url = 'https://mainnet.infura.io/v3/b1ba1b2a375249b484fa1b643f4f7fee'
web3_API = Web3(Web3.HTTPProvider(API_url))

request = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
info = json.loads(request.content)

print('safeLow -', info['safeLow'])
print('average -', info['average'])
print('fast -', info['fast'])
print('fastest -', info['fastest'])
print('Block Number -', info['blockNum'])

gas_price = web3_API.eth.gasPrice
print('Gas Price(Gwei) -', gas_price/(10**9))