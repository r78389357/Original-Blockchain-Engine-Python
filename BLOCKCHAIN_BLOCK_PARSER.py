"""
原创区块解析工具 - 独立开发
解析区块、提取交易、统计数据
"""
import json

class OriginalBlockParser:
    def parse_block(self, block: dict) -> dict:
        return {
            "index": block.get("index"),
            "hash": block.get("hash"),
            "tx_count": len(block.get("transactions", [])),
            "miner": block.get("miner"),
            "time": block.get("timestamp")
        }

    def get_transactions(self, block: dict):
        return block.get("transactions", [])

if __name__ == "__main__":
    parser = OriginalBlockParser()
    print("✅ 区块解析器加载完成")
