import hashlib
import json
from operator import ne
from time import time
from urllib.parse import urlparse

class BlockChain:
    def __init__(self):
        self.chain = []
        self.nodes = set()
        self.current_transactions = []

        # create genesis block
        self.new_block()

    def new_block(self, nonce=None, previous_hash=None):
    
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions' : [],
            'nonce': nonce,
            'previous_hash': previous_hash,
        }

        self.current_transactions = []

        self.chain.append(block)

        return block
    
    def register_node(self, address):
        parsed_url = urlparse(address)

        self.nodes.add(parsed_url.netloc)

    def full_mempool(self):
        self.last_block['transactions'] = self.current_transactions
        self.current_transactions = []

    def new_transaction(self, sender, recipient, amount):
        
        self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})

        return self.last_block['index']

    def validate_chain(self, chain):
        last_block = chain[0]
        index = 1

        while index < len(chain):
            block = chain[index]
            
            if block['previous_hash'] != self.hash(last_block):
                return False
            
            last_block = block
            index += 1
        
        return True

    def resolve_conflicts(self):
        new_chain = None
        max_length = self.chain

        for node in self.nodes:
            response = requests.get(f"http://{node}/chain")
            if response.status_code == 200:
                neighbour_chain = response.json()['chain']
                node_chain_length = len(neighbour_chain)

                if node_chain_length > max_length and self.validate_chain(neighbour_chain):
                    new_chain = neighbour_chain
                    max_length = node_chain_length
        
        if new_chain:
            self.chain = new_chain
            return True
        
        return False

            
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

