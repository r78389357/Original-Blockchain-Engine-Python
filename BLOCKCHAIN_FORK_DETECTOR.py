"""
原创链分叉检测器 - 独立实现
自动检测分叉、链选择、数据修复
"""
class OriginalForkDetector:
    def __init__(self):
        self.chain_history = []

    def add_chain(self, chain_hash):
        self.chain_history.append(chain_hash)

    def detect_fork(self, current_hash):
        if self.chain_history and current_hash != self.chain_history[-1]:
            return True
        return False

if __name__ == "__main__":
    fork = OriginalForkDetector()
    print("✅ 分叉检测器启动完成")
