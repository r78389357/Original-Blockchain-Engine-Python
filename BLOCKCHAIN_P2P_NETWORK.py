"""
原创区块链P2P网络节点 - 全新通信架构
节点发现、数据同步、交易广播
"""
import socket
import threading
import json
from typing import Set

class OriginalP2PNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers: Set[tuple] = set()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"✅ P2P节点启动: {self.host}:{self.port}")
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        data = conn.recv(4096).decode()
        msg = json.loads(data)
        if msg["type"] == "PEER_DISCOVERY":
            self.peers.add(addr)
            conn.send(json.dumps({"status": "PEER_ADDED"}).encode())
        conn.close()

    def broadcast_transaction(self, tx_data):
        for peer in self.peers:
            try:
                s = socket.socket()
                s.connect(peer)
                s.send(json.dumps({"type": "TRANSACTION", "data": tx_data}).encode())
                s.close()
            except:
                continue

if __name__ == "__main__":
    node = OriginalP2PNode("localhost", 8888)
    threading.Thread(target=node.start_server).start()
