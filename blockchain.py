import datetime
import json
import hashlib
from flask import Flask , jsonify


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

    def proof_of_work(self,previous_nonce):
        #อยากไได้ค่า nonce ที่ส่งผลให้ได้ target hash => 4 หลักแรก => 0000xxxxxx
        new_nonce = 1 #ค่า nonce ที่ต้องการ
        check_proof = False #ตัวแปรเช็คค่า nonce ให้ได้ตาม target ที่กำหนด

        #แก้โจทย์ทางคณิตศาสตร์
        while check_proof is False:
            hashoperation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce+=1
        return new_nonce

#web server
app = Flask(__name__)
#ใช้งาน Blockchain
blockchain = Blockchain()

#routing
@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

@app.route('/get_chain',methods=["GET"])
def get_chain():
    response={
        "chain":blockchain.chain,
        "lenght":len(blockchain.chain)
    }
    return jsonify(response),200

#run server
if __name__ =="__main__":
    app.run()
