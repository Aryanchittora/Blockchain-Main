from web3 import Web3

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

latest_block = web3.eth.get_block('latest')
print('latest block:', latest_block)

tranData = web3.eth.get_block_transaction_count('latest')
print('\ntransaction count:', tranData)

fee_history = web3.eth.fee_history(block_count=10, reward_percentiles=None, newest_block='latest')
print('\nfee history:', fee_history)