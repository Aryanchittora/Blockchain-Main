import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
    transaction = {
        'sender':'Satoshi',
        'reciever':'Mike',
        'amount':'5 ETH'
    }

    data = {
        'timestamp':time(),
        'transaction':transaction,
        'block reward':'2.5546257 Ether (2 + 0.5546257)',
        'uncles reward':'0',
        'difficulty':'7,313,161,775,076,869',
        'total difficulty':'28,115,534,355,622,634,754',
        'size':'56,528 bytes',
        'gas used':'14,935,987 (99.83%)',
        'gas limit':'14,955,955',
        'proof':proof
    }
    chain.append(data)
    print('Block Info -', data)
    block_str = json.dumps(data).encode()
    hash_str = hashlib.sha512(block_str).hexdigest()
    print('Hash Of Block -', hash_str)

block(previous_hash='265f7754ac6b704ec5955a0e4b1c9ee2715c7082ba24a975db126b9aa6b933f4', proof=23)