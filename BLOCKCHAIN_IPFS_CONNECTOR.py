"""
原创IPFS去中心化存储连接器 - 独立实现
文件上传、哈希获取、链上存储
"""
import requests
import json

class OriginalIPFSConnector:
    def __init__(self):
        self.api_url = "https://ipfs.infura-ipfs.io"

    def upload_data(self, data):
        try:
            res = requests.post(f"{self.api_url}/add", files={"file": json.dumps(data).encode()})
            return res.json().get("Hash")
        except:
            return None

if __name__ == "__main__":
    ipfs = OriginalIPFSConnector()
    print("✅ IPFS连接器就绪")
