import hashlib
import json
from time import time

class Block:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.count = 0
        self.new_block(previous_hash="No Previous hash since it is the genisis block")

    def new_block(self, previous_hash=None):
        block = {
            'block no':self.count,
            'timestamp':time(),
            'transaction':self.transactions or 'It is Genisis Block',
            'gas_fee':0.1,
            'previous_hash':previous_hash
        }

        self.count += 1
        self.chain.append(block)

        block_str = json.dumps(block).encode()
        hash_str = hashlib.sha256(block_str).hexdigest()

        self.chain.append(('Current Hash -', hash_str))
        return block

obj1 = Block()
print(obj1.chain)