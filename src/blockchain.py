import hashlib
import json
import sys
from time import time

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create genesis block
        self.new_block()

    def new_block(self, nonce=None, previus_hash=None):
    
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions' : [],
            'nonce': nonce,
            'previus_hash': previus_hash,
        }

        self.current_transactions = []

        self.chain.append(block)

        return block

    def full_mempool(self):
        self.last_block['transactions'] = self.current_transactions
        self.current_transactions = []

    def new_transaction(self, sender, recipient, amount):
        
        self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

        return self.last_block['index']

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine(self):
        last_block = self.last_block
        last_block['nonce'] = 0

        while self.valid_nonce(last_block) is False:
     
            last_block['nonce'] += 1
        

        data = json.dumps(last_block, sort_keys=True).encode()
        previous_hash = hashlib.sha256(data).hexdigest()

        return last_block['nonce'], previous_hash

    @staticmethod
    def valid_nonce(last_block):
        data = json.dumps(last_block, sort_keys=True).encode()
        return hashlib.sha256(data).hexdigest()[:4] == '0000'

    @property
    def last_block(self):
        return self.chain[-1]

