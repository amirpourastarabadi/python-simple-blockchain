from crypt import methods
import hashlib
import json
import sys
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previus_hash=None)

    def new_block(self, previus_hash=None):
        ''' create a new block'''
    
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions' : [],
            'proof': None,
            'previus_has': previus_hash,
        }

        self.chain.append(block)

        return block

    def full_mempool(self):
        self.last_block['transactions'] = self.current_transactions

    def new_trx(self, sender, recipient, amount):
        ''' add a new trx to the mempool '''
        self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})
        return self.current_transactions[-1]

    @staticmethod
    def hash(block):
        ''' hash a block '''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine(self):    
        proof = 0
        last_block = self.last_block
        last_block['proof'] = proof

        while self.valid_proof(last_block) is False:
            proof += 1
            last_block['proof'] = proof
        
        data = json.dumps(last_block, sort_keys=True).encode()
        self.new_block(hashlib.sha256(data).hexdigest())
        self.current_transactions = []

        return proof

    @staticmethod
    def valid_proof(last_block):
        data = json.dumps(last_block, sort_keys=True).encode()
        print(data)
        return hashlib.sha256(data).hexdigest()[:4] == '0000'

    @property
    def last_block(self):
        ''' return last block '''
        print(self.chain[-1], len)
        return self.chain[-1]

app = Flask(__name__)
clien_id = str(uuid4())


blockchain = BlockChain()


@app.route('/mine')
def mine():
    blockchain.new_trx(0, clien_id, 50)
    blockchain.full_mempool()
    proof = blockchain.mine()
    return jsonify({
        'message': 'block mined',
        'proof': proof
    }), 201

@app.route('/transactions', methods=['POST'])
def new_transaction():
    values = request.get_json()
    transaction = blockchain.new_trx(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'transaction created in block:{transaction}'}), 201
    

@app.route('/chain')
def full_chain():
    chain = {
        'chain' : blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(chain), 200


if __name__ == '__main__':
    app.run('0.0.0.0', sys.argv[1])