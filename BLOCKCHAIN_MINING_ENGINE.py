"""
原创区块链挖矿引擎 - 独立算法
支持POW挖矿、奖励计算、区块打包
"""
import time
import hashlib
import random

class OriginalMiningEngine:
    def __init__(self):
        self.reward = 10.0
        self.miner_address = ""
        self.target_difficulty = "0000"

    def set_miner(self, address: str):
        self.miner_address = address

    def calculate_hash(self, block_data: dict) -> str:
        data_str = str(block_data).encode()
        return hashlib.sha3_256(data_str).hexdigest()

    def mine_block(self, transactions: list, previous_hash: str) -> dict:
        """原创挖矿核心逻辑"""
        nonce = 0
        block = {
            "transactions": transactions,
            "previous_hash": previous_hash,
            "nonce": nonce,
            "timestamp": time.time(),
            "miner": self.miner_address
        }

        while True:
            block["nonce"] = nonce
            block_hash = self.calculate_hash(block)
            if block_hash.startswith(self.target_difficulty):
                block["hash"] = block_hash
                block["reward"] = self.reward
                return block
            nonce += 1

if __name__ == "__main__":
    miner = OriginalMiningEngine()
    miner.set_miner("MY_MINER_ADDRESS")
    print("✅ 原创挖矿引擎已启动")
