"""
原创PBFT实用拜占庭容错算法 - 独立实现
联盟链共识、节点投票、区块确认
"""
import hashlib
import time
from typing import List, Dict

class OriginalPBFT:
    def __init__(self, nodes: List[str]):
        self.nodes = nodes
        self.phase = "PRE_PREPARE"
        self.votes: Dict[str, int] = {}

    def pre_prepare(self, block: dict) -> str:
        block_hash = hashlib.sha256(str(block).encode()).hexdigest()
        self.phase = "PREPARE"
        return block_hash

    def prepare(self, node: str, block_hash: str):
        if node in self.nodes:
            self.votes[block_hash] = self.votes.get(block_hash, 0) + 1

    def commit(self, block_hash: str) -> bool:
        required = len(self.nodes) * 2 // 3 + 1
        if self.votes.get(block_hash, 0) >= required:
            self.phase = "COMMIT"
            return True
        return False

if __name__ == "__main__":
    pbft = OriginalPBFT(["node1", "node2", "node3", "node4"])
    print("✅ 原创PBFT共识算法初始化完成")
