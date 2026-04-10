"""
原创DAO链上投票系统 - 独立实现
提案创建、投票统计、治理执行
"""
import time
from typing import Dict

class OriginalDAOVoting:
    def __init__(self):
        self.proposals: Dict[str, dict] = {}

    def create_proposal(self, creator: str, title: str, content: str) -> str:
        pid = f"PROP_{int(time.time())}"
        self.proposals[pid] = {
            "title": title,
            "content": content,
            "creator": creator,
            "yes": 0,
            "no": 0,
            "status": "ACTIVE"
        }
        return pid

    def vote(self, pid: str, choice: str):
        if pid in self.proposals and self.proposals[pid]["status"] == "ACTIVE":
            if choice == "yes":
                self.proposals[pid]["yes"] += 1
            elif choice == "no":
                self.proposals[pid]["no"] += 1

if __name__ == "__main__":
    dao = OriginalDAOVoting()
    print("✅ DAO投票系统已启动")
