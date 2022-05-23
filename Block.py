import hashlib
import json 
from time import time

chain = []

def block(proof, previous_hash=None):
    transaction = {
        'sender':'Mike',
        'reciever':'John',
        'ammount': '2 ETH'
    }

    data = {
        'index':1,
        'timestamp':time(),
        'transactions':transaction,
        'gas/fee':0.1,
        'proof':proof,
        'previous_hash':previous_hash
    }

    chain.append(data)
    print('Block information -', data)
    block_str = json.dumps(data).encode()
    hash_str = hashlib.sha256(block_str).hexdigest()
    print(f'Hash Code of Block - {hash_str}')

block(previous_hash='No previous hash beacause this is the first block', proof=000)