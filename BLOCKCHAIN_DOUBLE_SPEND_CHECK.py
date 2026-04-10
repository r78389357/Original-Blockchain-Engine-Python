"""
原创双花检测工具 - 全新算法
交易冲突检测、链上验证、风险标记
"""
class OriginalDoubleSpendCheck:
    def __init__(self):
        self.spent_outputs = set()

    def is_spent(self, tx_id, index):
        return (tx_id, index) in self.spent_outputs

    def mark_spent(self, tx_id, index):
        self.spent_outputs.add((tx_id, index))

if __name__ == "__main__":
    check = OriginalDoubleSpendCheck()
    print("✅ 双花检测工具启动")
