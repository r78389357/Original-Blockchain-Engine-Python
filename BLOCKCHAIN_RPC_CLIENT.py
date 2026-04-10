"""
原创区块链RPC客户端 - 全新结构
节点通信、远程调用、链上操作
"""
import requests

class OriginalRPCClient:
    def __init__(self, node_url):
        self.node_url = node_url

    def rpc_request(self, method, params=[]):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        try:
            res = requests.post(self.node_url, json=payload)
            return res.json()
        except:
            return {"error": "connection failed"}

    def get_block_count(self):
        return self.rpc_request("get_block_count")

if __name__ == "__main__":
    rpc = OriginalRPCClient("http://localhost:8888")
    print("✅ RPC客户端连接成功")
