# umqtt.simple 使用說明

## 📚 基本概念

`umqtt.simple` 是 MicroPython 專用的輕量級 MQTT 客戶端，適合在 Pico W 這類嵌入式設備上使用。

## 🔧 安裝

如果您的 Pico W 還沒有安裝 `umqtt.simple`，可以通過以下方式安裝：

1. **下載 umqtt 模組**：
   - 從 [MicroPython umqtt GitHub](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple) 下載
   - 或使用 `mip` 工具安裝（如果支援）

2. **手動安裝**：
   ```python
   # 在 Pico W 上執行
   import mip
   mip.install("umqtt.simple")
   ```

## 📝 基本用法

### 1. 導入模組

```python
from umqtt.simple import MQTTClient
```

### 2. 建立 MQTT 客戶端

```python
client = MQTTClient(
    client_id="pico_w_client",  # 客戶端 ID（必須唯一）
    server="192.168.1.100",     # MQTT Broker IP
    port=1883                    # MQTT 埠號（通常是 1883）
)
```

### 3. 連線到 MQTT Broker

```python
client.connect()
```

### 4. 發布訊息

```python
topic = "pico/sensor"
message = "Hello MQTT!"
client.publish(topic, message)
```

### 5. 訂閱主題並接收訊息

```python
# 設定訊息回調函數
def on_message(topic, msg):
    print(f"收到訊息: {msg.decode('utf-8')}")

client.set_callback(on_message)
client.subscribe("pico/command")

# 在主循環中檢查訊息
while True:
    client.check_msg()  # 非阻塞檢查
    time.sleep(0.1)
```

### 6. 斷開連線

```python
client.disconnect()
```

## 📂 範例檔案說明

### 1. `mqtt_example.py` - 完整範例
- ✅ 同時支援發布和訂閱
- ✅ 每隔 10 秒發布一次訊息
- ✅ 持續監聽訂閱的主題

### 2. `mqtt_publisher.py` - 純發布者
- ✅ 只發布訊息，不訂閱
- ✅ 每隔 10 秒發布一次
- ✅ 適合感測器資料上傳

### 3. `mqtt_subscriber.py` - 純訂閱者
- ✅ 只訂閱訊息，不發布
- ✅ 持續監聽並處理收到的指令
- ✅ 適合接收控制指令

## ⚙️ 設定步驟

### 1. 修改 MQTT Broker 設定

在每個範例檔案中，找到以下設定並修改：

```python
MQTT_BROKER = "192.168.1.100"  # 改成您的 MQTT Broker IP
MQTT_PORT = 1883                # 確認埠號是否正確
```

### 2. 修改主題名稱

```python
MQTT_TOPIC_PUBLISH = "pico/sensor"    # 發布主題
MQTT_TOPIC_SUBSCRIBE = "pico/command" # 訂閱主題
```

### 3. 修改客戶端 ID

```python
MQTT_CLIENT_ID = "pico_w_client"  # 每個設備應該使用不同的 ID
```

## 🔍 常見問題

### Q1: 連線失敗怎麼辦？

**A:** 檢查以下項目：
- ✅ WiFi 是否已連線
- ✅ MQTT Broker IP 是否正確
- ✅ MQTT Broker 是否正在運行
- ✅ 防火牆是否阻擋埠號 1883

### Q2: 如何測試 MQTT 連線？

**A:** 可以使用以下工具：
- **MQTT.fx** (Windows/Mac/Linux)
- **MQTT Explorer** (跨平台)
- **mosquitto_pub/mosquitto_sub** (命令列工具)

### Q3: 如何發布 JSON 格式的資料？

**A:** 使用 `json` 模組：

```python
import json

data = {
    "temperature": 25.5,
    "humidity": 60.0,
    "timestamp": time.time()
}
message = json.dumps(data)
client.publish("pico/sensor", message)
```

### Q4: 如何處理多個主題？

**A:** 可以訂閱多個主題：

```python
client.subscribe("pico/topic1")
client.subscribe("pico/topic2")
client.subscribe("pico/topic3")
```

在 `on_message` 函數中根據 `topic` 參數判斷：

```python
def on_message(topic, msg):
    topic_str = topic.decode('utf-8')
    if topic_str == "pico/topic1":
        # 處理 topic1 的訊息
    elif topic_str == "pico/topic2":
        # 處理 topic2 的訊息
```

## 🚀 進階用法

### 使用 QoS 等級

```python
# 發布時指定 QoS
client.publish("pico/sensor", "message", qos=1)

# 訂閱時指定 QoS
client.subscribe("pico/command", qos=1)
```

### 保持連線（Keep Alive）

```python
client = MQTTClient(
    client_id="pico_w_client",
    server="192.168.1.100",
    port=1883,
    keepalive=60  # 60 秒
)
```

### 自動重連機制

```python
def connect_mqtt_with_retry(max_retries=5):
    for i in range(max_retries):
        try:
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, MQTT_PORT)
            client.connect()
            return client
        except Exception as e:
            print(f"連線失敗 ({i+1}/{max_retries}): {e}")
            time.sleep(5)
    return None
```

## 📖 參考資源

- [MicroPython umqtt 文件](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple)
- [MQTT 協議說明](https://mqtt.org/)

