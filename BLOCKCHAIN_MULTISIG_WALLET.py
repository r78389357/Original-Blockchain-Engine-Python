"""
原创多签钱包 - 独立实现
多节点签名、联合授权、资产安全
"""
import hashlib
from typing import List

class OriginalMultiSigWallet:
    def __init__(self, owners: List[str], required: int):
        self.owners = owners
        self.required = required
        self.transactions = {}

    def create_transaction(self, tx_id: str, data: dict):
        self.transactions[tx_id] = {
            "data": data,
            "signatures": [],
            "executed": False
        }

    def sign_transaction(self, tx_id: str, signer: str):
        if signer in self.owners and tx_id in self.transactions:
            self.transactions[tx_id]["signatures"].append(signer)

    def execute_transaction(self, tx_id: str) -> bool:
        tx = self.transactions[tx_id]
        if len(set(tx["signatures"])) >= self.required and not tx["executed"]:
            tx["executed"] = True
            return True
        return False

if __name__ == "__main__":
    wallet = OriginalMultiSigWallet(["a", "b", "c"], 2)
    print("✅ 多签钱包初始化完成")
