"""
原创简易智能合约虚拟机 - 全新结构
合约部署、执行、状态存储
"""
class OriginalSVM:
    def __init__(self):
        self.contracts = {}

    def deploy_contract(self, address, code):
        self.contracts[address] = {
            "code": code,
            "storage": {}
        }

    def execute(self, address, function, params):
        if address not in self.contracts:
            return "error"
        return f"executed {function} with {params}"

if __name__ == "__main__":
    svm = OriginalSVM()
    print("✅ 原创智能合约虚拟机SVM启动")
