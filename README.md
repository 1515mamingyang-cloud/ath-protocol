# ath-protocol
Agent Trust Handshake Protocol
# 协议本质：面向智能体生态的纯应用层轻量化安全通信协议，与业务能力调用、工具执行无关，仅聚焦智能体跨平台 / 跨节点通信的可信准入问题。
与 MCP 核心区别：
MCP：规范智能体「能力调用、工具交互」的业务层协议
ATHP：规范智能体「通信前握手、身份核验、权限准入」的安全底座协议（轻量化、无侵入、可兼容所有上层协议）
核心目标：解决智能体通信无唯一身份、无统一发现、无可信认证、无细粒度鉴权的安全痛点。

# 智能体互联网可信握手协议（ATH Protocol）
## Agent Trust Handshake Protocol

🔥 **轻量化、去中心化、应用层智能体可信通信协议**
纯安全握手协议，不涉及业务逻辑，为所有智能体提供统一身份认证、对象发现、访问控制服务。

---

## 核心能力
✅ **对象发现**：统一智能体通信发现机制
✅ **数字身份**：全局唯一智能体DID身份标识
✅ **双维度认证**：AI应用身份 + 用户代表身份
✅ **访问鉴权**：最小权限通信管控
✅ **跨生态互认**：兼容所有智能体平台
✅ **轻量化**：10分钟快速集成

---

## 协议定位
- **ATH = 智能体的"安全门禁"**
- 与 MCP 协议互补：ATH 负责可信准入，MCP 负责业务调用
- 纯应用层协议，基于 HTTPS，无底层改造

---

## 快速使用（Python SDK）
```python
from ath_sdk import AthClient

# 初始化智能体
agent = AthClient(agent_did="did:ath:my-agent-123")

# 1. 发现目标智能体
agent.discover(target_url="https://api.example.com")

# 2. 身份认证
agent.authenticate(ai_token="your-ai-token")

# 3. 权限鉴权
result = agent.authorize()
print("鉴权结果:", result)
