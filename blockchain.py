import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.new_block(previous_hash = 1, proof = 100) # genesis block

    def new_block(self, proof, previous_hash=None):

        """
        Creates new block + adds to blockchain

        proof: integer; proof given by POW alg
        previous_hash: string, optional; hash of previous block
        returns the new block
        """

        block = {
            "index": len(self.chain) + 1,
            "timestamp" : time(),
            "transactions" : self.current_transactions,
            "proof" : proof,
            "previous_hash" : previous_hash
        }

        self.current_transactions = [] # reset list
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates new transactions to go into next mined block

        sender: str; address of sender
        recipient: str; address of recipient
        amount: int; amount
        returns the index of the current Block
        """

        self.current_transactions.append({
            "sender" : sender,
            "recipient": recipient,
            "amount": amount
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        hash of a blockchain

        block: dictionary; Block
        returns a string; hash

        """

        block_string = json.dumps(block, sort_keys = True).encode()
        return haslib.sha256(block_string).hexdigest()


    def proof_of_work(self, last_proof):
        """
        POW Alg -- find num q where hash(pq) contains 4 zeroes at the front.
        (p is previous proof, q is the new proof)

        last_proof: int;
        return: int; q, the new hash
        """

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof + = 1

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        validates proof_of_work

        last_proof: int; previous proof
        proof: int; current proof
        return: boolean; true/false
        """

        guess = f'{last_proof}{proof}'.encode()
        guess-hash = hashlib.sha256(guess).hexdigest()
        
                                        # TO MAKE MORE DIFFICULT: change req to more zeroes
        return guess_hash[:4] == "0000" # return if the first four digits are zeroes



# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# https://hyperledger-fabric.readthedocs.io/en/release-1.2/ -- HYPERLEDGER FABRIC
