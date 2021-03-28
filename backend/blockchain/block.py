import time

from backend.util.crypto_hash import crypto_hash

FIRSTBLOCK_DATA = {
    'timestamp': 1,
    'last_hash': 'first_last_hash',
    'hash': 'ee78d2c7a5a7ed76940a3a500eb99aa7b942244e1f6db8a80592ee72e9dab948',
    'data' : [],
    'difficulty' : 3,
    'nonce' : 'first_nonce'
}

class Block:
    """
    Block: aunit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self,timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = crypto_hash(timestamp, last_hash, data)
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'Block-data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the givin last_block and data, until ablock hash is found that meets the leading 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        # hash = f'{timestamp}-{last_hash}'
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        while hash[0:difficulty] != '0'* difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def generate_first_block():
        """
        Generate the first block.
        """
        # return Block(1,'first_last_hash', 'first_hash', [])
        # return Block(
        #     timestamp=FIRSTBLOCK_DATA['timestamp'],
        #     last_hash=FIRSTBLOCK_DATA['last_hash'],
        #     hash=FIRSTBLOCK_DATA['hash'],
        #     data=FIRSTBLOCK_DATA['data']
        # )
        return Block(**FIRSTBLOCK_DATA)

def main():
        first_block = Block.generate_first_block()
        block = Block.mine_block(first_block,'foo')
        print(block)
        

if __name__ == '__main__' :
    main()
