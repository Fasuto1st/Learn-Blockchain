import datetime
import json
import hashlib

class Blockchain :
    def __init__(self):
        #เก็บกลุ่มของ Block
        self.chain = [] #list ที่เก็บ block
        self.create_block(nonce=1,previous_hash="0")
        self.create_block(nonce=10,previous_hash="10")
        self.create_block(nonce=30,previous_hash="20") #genesis block

    def create_block(self,nonce,previous_hash):
        #เก็บส่วนประกอบของ Block แต่ละ Block
        block = {
            "index":len(self.chain)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "previous_hash":previous_hash
        }
        self.chain.append(block)
        return block


    #.ให้บริการเกี่ยวกับ Block ก่อนหน้า
    def get_previous_block(self):
        return self.chain[-1]

    #เข้ารหัส block
    def hash(self,block):
        #แปลง python obj เป็น json obj
       encode_block = json.dumps(block,sort_keys=True).encode()
        #sha256
       return hashlib.sha256(encode_block).hexdigest()

#ใช้งาน Blockchain
blockchain = Blockchain()
# print(blockchain.chain)
print(blockchain.hash(blockchain.chain[0]))
print(blockchain.hash(blockchain.chain[1]))
# print(blockchain.get_previous_block())

