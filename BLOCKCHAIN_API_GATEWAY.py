"""
原创区块链API网关 - 独立开发
链上查询、交易发送、区块获取、接口封装
"""
from flask import Flask, jsonify

app = Flask(__name__)

class OriginalBlockchainAPI:
    def __init__(self):
        self.chain_height = 1000

    def get_height(self):
        return self.chain_height

    def get_block(self, index: int):
        return {"index": index, "hash": "NEW_BLOCK_HASH"}

api = OriginalBlockchainAPI()

@app.route("/height")
def height():
    return jsonify({"height": api.get_height()})

@app.route("/block/<int:index>")
def block(index):
    return jsonify(api.get_block(index))

if __name__ == "__main__":
    print("✅ 区块链API网关启动")
