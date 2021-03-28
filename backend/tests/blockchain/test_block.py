from backend.blockchain.block import Block, FIRSTBLOCK_DATA

def test_mine_block():
    last_block= Block.generate_first_block()
    data = 'test-data'
    block = Block.mine_block(last_block,data)

    assert isinstance(block,Block)
    assert block.data == data
    assert block.last_hash == last_block.hash

def test_first_Block():
    firstBlock = Block.generate_first_block()

    assert isinstance(firstBlock, Block)
    # assert firstBlock.timestamp == FIRSTBLOCK_DATA['timestamp']
    # assert firstBlock.last_hash == FIRSTBLOCK_DATA['last_hash']
    # assert firstBlock.hash == 'ee78d2c7a5a7ed76940a3a500eb99aa7b942244e1f6db8a80592ee72e9dab948'
    # assert firstBlock.data == FIRSTBLOCK_DATA['data']
    for key, value in FIRSTBLOCK_DATA.items():
        getattr(firstBlock, key) == value