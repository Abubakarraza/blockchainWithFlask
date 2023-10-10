import datetime


class BlockChain:
    def __init__(self):
        self.chains = []
        # Genesis block
        self.createBlock(owner='creator', Reg_no="00",
                         proof="00", prev_hash="98")
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
        self.chains.append(block)
        return block
