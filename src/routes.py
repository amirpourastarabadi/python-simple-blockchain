from crypt import methods
import imp
from uuid import uuid4
from flask import Flask, jsonify, request
from  src.blockchain import BlockChain

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')


blockchain = BlockChain()


@app.route('/mine')
def mine():
    if len(blockchain.current_transactions) != 0:
        blockchain.new_transaction(0, node_identifier, 50)
        blockchain.full_mempool()
        nonce, previus_hash = blockchain.mine()

        blockchain.new_block(previus_hash=previus_hash)

        return jsonify({
            'message': 'block mined',
            'nonce': nonce
        }), 201
    
    index = blockchain.last_block['index']
    return jsonify({'message': f'mine in progres on block: {index}'})

@app.route('/transactions', methods=['POST'])
def new_transaction():
    values = request.get_json()

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    return jsonify({'message': f'transaction created in block: {index}'}), 201
    
@app.route('/chain')
def full_chain():
    chain = {
        'chain' : blockchain.chain,
        'length': len(blockchain.chain),
    }

    return jsonify(chain), 200


@app.route('/node/register', methods=['POST'])
def node_register():
    values = request.get_json()
    registered_node = values['node']
    blockchain.register_node(registered_node)

    return jsonify({'message': f'node {registered_node} registerd'}), 201


@app.route('/node/resolve')
def node_resolve():
    return "it will resolve chain conflict"


@app.route('/nodes')
def nodes():
    print(blockchain.nodes)
    return jsonify({'nodes': list(blockchain.nodes)})