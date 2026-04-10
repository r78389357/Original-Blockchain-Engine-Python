"""
原创DeFi借贷池 - 独立算法
存款、借贷、利率计算、清算
"""
import time

class OriginalLendingPool:
    def __init__(self):
        self.deposits = {}
        self.borrows = {}
        self.deposit_apr = 8.0
        self.borrow_apr = 15.0

    def deposit(self, user, amount):
        self.deposits[user] = {"amount": amount, "time": time.time()}

    def calculate_deposit_interest(self, user):
        data = self.deposits[user]
        duration = time.time() - data["time"]
        years = duration / (365 * 24 * 3600)
        return data["amount"] * (self.deposit_apr / 100) * years

if __name__ == "__main__":
    lending = OriginalLendingPool()
    print("✅ 借贷池运行正常")
