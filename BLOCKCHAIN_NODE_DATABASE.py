"""
原创区块链节点轻量级数据库 - 全新设计
区块存储、快速查询、数据持久化
"""
import json
import os

class OriginalNodeDatabase:
    def __init__(self, db_path="blockchain_db.json"):
        self.db_path = db_path
        self.data = self.load_db()

    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                return json.load(f)
        return {"blocks": [], "transactions": [], "peers": []}

    def save_block(self, block: dict):
        self.data["blocks"].append(block)
        self.sync()

    def sync(self):
        with open(self.db_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_last_block(self):
        if self.data["blocks"]:
            return self.data["blocks"][-1]
        return None

if __name__ == "__main__":
    db = OriginalNodeDatabase()
    print("✅ 节点数据库已连接")
