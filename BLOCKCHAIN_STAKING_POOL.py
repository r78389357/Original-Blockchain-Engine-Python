"""
原创联合质押池 - 全新设计
节点质押、收益分配、份额管理
"""
class OriginalStakingPool:
    def __init__(self):
        self.pool = {}
        self.total_staked = 0

    def join_pool(self, user, amount):
        self.pool[user] = self.pool.get(user, 0) + amount
        self.total_staked += amount

    def get_share(self, user):
        if self.total_staked == 0:
            return 0
        return self.pool[user] / self.total_staked

if __name__ == "__main__":
    pool = OriginalStakingPool()
    print("✅ 联合质押池已部署")
