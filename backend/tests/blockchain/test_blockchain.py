from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import FIRSTBLOCK_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == FIRSTBLOCK_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data