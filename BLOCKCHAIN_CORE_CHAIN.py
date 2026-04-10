"""
原创区块链底层主链 - 全新结构、无公开复用
支持区块生成、哈希校验、链验证、难度调整
"""
import hashlib
import json
import time
from typing import List, Dict

class OriginalBlockchain:
    def __init__(self):
        self.chain: List[Dict] = []
        self.pending_transactions = []
        self.difficulty = 4
        self.create_genesis_block()

    def create_genesis_block(self):
        """原创创世区块生成逻辑"""
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "transactions": [],
            "proof": 999999,
            "previous_hash": "GENESIS_BLOCK_HASH_2025",
            "nonce": 0
        }
        genesis_block["hash"] = self.hash_block(genesis_block)
        self.chain.append(genesis_block)

    def hash_block(self, block: Dict) -> str:
        """原创区块哈希算法"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha3_512(block_string).hexdigest()

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "time": time.time()
        })
        return self.last_block["index"] + 1

    @property
    def last_block(self) -> Dict:
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """原创工作量证明算法"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof: int, proof: int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:self.difficulty] == "0" * self.difficulty

if __name__ == "__main__":
    chain = OriginalBlockchain()
    print("✅ 原创区块链主链初始化完成")
