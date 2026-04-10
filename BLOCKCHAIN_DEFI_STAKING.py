"""
原创DeFi质押挖矿合约 - 全新逻辑
质押、收益计算、解押、奖励发放
"""
import time

class OriginalDeFiStaking:
    def __init__(self):
        self.stake_records = {}
        self.apr = 12.0

    def stake(self, user: str, amount: float):
        self.stake_records[user] = {
            "amount": amount,
            "start_time": time.time(),
            "claimed_reward": 0.0
        }

    def calculate_reward(self, user: str) -> float:
        """原创收益算法"""
        record = self.stake_records.get(user)
        if not record:
            return 0.0
        duration = time.time() - record["start_time"]
        years = duration / (365 * 24 * 3600)
        reward = record["amount"] * (self.apr / 100) * years
        return round(reward, 4)

    def unstake(self, user: str) -> float:
        reward = self.calculate_reward(user)
        total = self.stake_records[user]["amount"] + reward
        del self.stake_records[user]
        return total

if __name__ == "__main__":
    staking = OriginalDeFiStaking()
    staking.stake("user1", 1000)
    print("✅ DeFi质押合约已就绪")
