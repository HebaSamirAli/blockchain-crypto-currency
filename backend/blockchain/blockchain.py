from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain : apublic ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.generate_first_block()]

    def add_block(self,data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('One')
    blockchain.add_block('Two')
    print(blockchain)

if __name__ == '__main__':
    main()