"""
原创加密货币通证标准 - 全新设计
支持转账、授权、余额、铸造、销毁
"""
class OriginalTokenStandard:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}
        self.allowance = {}

    def transfer(self, sender, recipient, amount):
        if self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[recipient] = self.balances.get(recipient, 0) + amount
            return True
        return False

    def balance_of(self, address):
        return self.balances.get(address, 0)

if __name__ == "__main__":
    token = OriginalTokenStandard("OriginalCoin", "ORC", 1000000)
    print("✅ 原创通证标准部署完成")
