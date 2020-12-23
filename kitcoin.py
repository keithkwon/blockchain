from hashlib import sha256


class Block:
    def __init__(self, nonce, data, prevhash, hash):
        self.nonce = nonce
        self.data = data
        self.prevhash = prevhash
        self.hash = hash


datas = ['Genesis Block', '2nd', '3rd', '4th', '5th']

genesisBlock = Block(0, datas[0], None, sha256(
    datas[0].encode('utf-8')).hexdigest())

blockchain = []

blockchain.append(genesisBlock)

count = 1
block_cnt = 0
nonce = 0
while True:
    if count == 3:
        break
    previous_block_hash = blockchain[block_cnt].hash
    block_data = f'{previous_block_hash}{nonce}{datas[count]}'

    temp_hash = sha256(block_data.encode('utf-8')).hexdigest()

    if temp_hash[0:5] == '00000':
        new_block = Block(nonce, datas[count], previous_block_hash, temp_hash)

        blockchain.append(new_block)
        nonce = 0
        count += 1
        block_cnt += 1
    else:
        nonce += 1


for block in blockchain:
    print(f'nonce: {block.nonce}')
    print(f'data: {block.data}')
    print(f'prevhash: {block.prevhash}')
    print(f'hash: {block.hash}')
    print()
