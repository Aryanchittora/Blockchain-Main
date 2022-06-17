from web3 import Web3

url = 'HTTP://127.0.0.1:7545'
connect = Web3(Web3.HTTPProvider(url))

for i in range(0, 5):
    block = connect.eth.getBlock(i)
    print('Block Number -', block['number'])
    print('Block Hash -', block['hash'].hex())
    print('Nonce -', block['nonce'].hex())
    print('Parent Hash -', block['parentHash'].hex())
    print('Transactions -', block['transactions'])
    print('---------------------------------\n')

transaction = connect.eth.get_transaction('0xa653477325ee2866d640acaaa3c8e1db78be4311ad63cbce6eb1d3b78d13828f')
print('Transaction Data -', transaction)
print('To -', transaction['to'])
print('From -', transaction['from'])
print('Value -', transaction['value'])
print('====================================')