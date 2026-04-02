# ATH Protocol 极简Python SDK
import time
import requests

class AthClient:
    def __init__(self, agent_did: str):
        self.agent_did = agent_did
        self.version = "ath-1.0"
        self.target_endpoint = None

    # 1. 对象发现
    def discover(self, target_url: str):
        discover_url = f"{target_url}/.well-known/ath-meta"
        try:
            res = requests.get(discover_url, timeout=5)
            self.target_endpoint = res.json().get("ath_endpoint")
            print(f"✅ 发现成功：目标通信地址 = {self.target_endpoint}")
            return True
        except Exception as e:
            print(f"❌ 发现失败：{e}")
            return False

    # 2. 身份认证
    def authenticate(self, ai_token: str, user_token: str = None):
        payload = {
            "version": self.version,
            "timestamp": int(time.time()),
            "type": "auth",
            "data": {
                "agent_did": self.agent_did,
                "ai_credential": ai_token,
                "user_credential": user_token
            }
        }
        try:
            res = requests.post(self.target_endpoint, json=payload)
            if res.json()["code"] == 200:
                print("✅ 身份认证成功")
                return True
            else:
                print(f"❌ 认证失败：{res.json()['message']}")
                return False
        except Exception as e:
            print(f"❌ 认证异常：{e}")
            return False

    # 3. 访问鉴权
    def authorize(self):
        payload = {
            "version": self.version,
            "timestamp": int(time.time()),
            "type": "authz",
            "data": {
                "agent_did": self.agent_did
            }
        }
        try:
            res = requests.post(self.target_endpoint, json=payload)
            result = res.json()
            print(f"🔐 鉴权结果：{result['message']}")
            return result
        except Exception as e:
            print(f"❌ 鉴权失败：{e}")
            return {"code": 5001, "message": "Internal Error"}
