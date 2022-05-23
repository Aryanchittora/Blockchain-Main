from ast import Return
import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="No previous Hash. Since this is the first block.")

    def new_block(self, previous_hash=None):
        block = {
            'Block No': self.count,
            'timestamp': time(),
            'transactions': self.new_transactions or 'No Transactions First Genesis Block',
            'gasfee': 0.1,
            'previous hash':previous_hash or self.hash(self.chain[-1])
        }
        self.new_transactions = []
        self.count = self.count + 1
        self.chain.append(block)

        return block

    def transaction(self, sender, reciever, ammount):
        sender_hash = hashlib.sha256(sender.encode()).hexdigest()
        reciever_hash = hashlib.sha256(reciever.encode()).hexdigest()

        data = {
            'sender':sender_hash,
            'receiver':reciever_hash,
            'ammount': ammount
        }

        self.new_transactions.append(data)
        return self.lastBlock()

    def lastBlock(self):
        return self.chain[-1]

    def hash(self, block):
        string_object = json.dumps(block)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        self.chain.append(("Current Hash: ", hex_hash))
        return hex_hash

blockchain = Block()

tran1 = blockchain.transaction('Jhon', 'Ron', '5 ETH')
tran2 = blockchain.transaction('Mike', 'Kanto', '1 ETH')
tran3 = blockchain.transaction('Galar', 'Hisui', '2 ETH')
blockchain.new_block()

tran4 = blockchain.transaction('Sinnoh', 'Nike', '3 ETH')
tran5 = blockchain.transaction('Jhon', 'Mike', '4 ETH')
blockchain.new_block()

print(blockchain.chain)
