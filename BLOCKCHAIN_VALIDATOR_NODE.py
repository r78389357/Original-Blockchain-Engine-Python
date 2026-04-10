"""
原创区块链验证节点 - 全新逻辑
区块验证、交易校验、共识参与
"""
import hashlib

class OriginalValidatorNode:
    def __init__(self):
        self.stake = 10000

    def validate_block(self, block: dict) -> bool:
        """原创区块验证规则"""
        if not block.get("hash"):
            return False
        test_hash = hashlib.sha256(str(block).encode()).hexdigest()
        return test_hash == block["hash"]

    def validate_transaction(self, tx: dict) -> bool:
        required_fields = ["sender", "recipient", "amount"]
        return all(field in tx for field in required_fields)

if __name__ == "__main__":
    validator = OriginalValidatorNode()
    print("✅ 验证节点运行正常")
