"""
原创交易池管理器 - 独立实现
待打包交易、手续费排序、防双花
"""
import time
from typing import List, Dict

class OriginalTransactionPool:
    def __init__(self):
        self.pool: List[Dict] = []
        self.max_pool_size = 100

    def add_transaction(self, tx: dict):
        if len(self.pool) < self.max_pool_size and tx not in self.pool:
            tx["time"] = time.time()
            self.pool.append(tx)

    def sort_by_fee(self) -> List[Dict]:
        """原创手续费优先排序"""
        return sorted(self.pool, key=lambda x: x.get("fee", 0), reverse=True)

    def clear_processed(self, processed_txs: List[Dict]):
        self.pool = [tx for tx in self.pool if tx not in processed_txs]

    def get_pool_size(self):
        return len(self.pool)

if __name__ == "__main__":
    pool = OriginalTransactionPool()
    print("✅ 交易池初始化完成")
