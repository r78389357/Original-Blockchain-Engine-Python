"""
原创区块链椭圆曲线签名工具 - 独立实现
用于交易签名、身份验证、防篡改
"""
import ecdsa
import hashlib
import binascii

class OriginalECDSACrypto:
    def __init__(self):
        self.curve = ecdsa.SECP256k1

    def generate_key_pair(self) -> tuple:
        """原创密钥对生成"""
        sk = ecdsa.SigningKey.generate(curve=self.curve)
        vk = sk.get_verifying_key()
        private_key = sk.to_string().hex()
        public_key = vk.to_string().hex()
        return private_key, public_key

    def sign_transaction(self, private_key: str, data: str) -> str:
        sk = ecdsa.SigningKey.from_string(binascii.unhexlify(private_key), curve=self.curve)
        hash_data = hashlib.sha256(data.encode()).digest()
        signature = sk.sign(hash_data).hex()
        return signature

    def verify_signature(self, public_key: str, data: str, signature: str) -> bool:
        try:
            vk = ecdsa.VerifyingKey.from_string(binascii.unhexlify(public_key), curve=self.curve)
            hash_data = hashlib.sha256(data.encode()).digest()
            return vk.verify(binascii.unhexlify(signature), hash_data)
        except:
            return False

if __name__ == "__main__":
    crypto = OriginalECDSACrypto()
    priv, pub = crypto.generate_key_pair()
    print("✅ 原创ECDSA密钥对生成成功")
