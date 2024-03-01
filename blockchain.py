# import Required lib
import datetime
import hashlib
import json


class BlockChain:
    def __init__(self):
        self.chains = []
        # Genesis block
        self.createBlock(owner='creator', Reg_no="00",
                         proof=00, prev_hash='genesis_hash')
    # create block function

    def createBlock(self, owner, Reg_no, proof, prev_hash):
        block = {
            "owner": owner,
            "Reg_no": Reg_no,
            "proof": proof,
            "pev_hash": prev_hash,
            "index": len(self.chains)+1,
            "timestamp": str(datetime.datetime.now())
        }
        block['hash'] = self.hash(block)
        self.chains.append(block)
        return block

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash = hashlib.sha256(
                str(new_proof**2-previous_proof**2).encode()).hexdigest()

            if hash[:3] == "000":
                check_proof = True
            else:
                new_proof += 1
        print("new_proof", new_proof)
        return new_proof

    def hash(self, block):
        encode_block = json.dumps(block).encode()
        return hashlib.sha256(encode_block).hexdigest()

    def is_valid_chain(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash = hashlib.sha256(
                str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash[:3] != '000':
                return False
            previous_block = block
            block_index += 1
        return True

    def previous_block(self):

        return self.chains[-1]
