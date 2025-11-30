import paho.mqtt.client as mqtt
import time

# MQTT 代理器設定
BROKER_ADDRESS = "localhost"
PORT = 1883
TOPIC = "客廳"

# 當連接到 MQTT 代理器時觸發
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("連接到 MQTT 代理器成功！")
    else:
        print(f"連接失敗，返回碼為 {rc}")

# 建立 MQTT 客戶端實例
client = mqtt.Client()
client.on_connect = on_connect

# 連接到 MQTT 代理器
client.connect(BROKER_ADDRESS, PORT, 60)

# 啟動迴圈以處理網路流量和回調
client.loop_start()

try:
    while True:
        message = "Hello, MQTT!"
        client.publish(TOPIC, message)
        print(f"發布訊息: {message} 到主題: {TOPIC}")
        time.sleep(5)  # 每 5 秒發布一次
except KeyboardInterrupt:
    print("Publisher 停止。")
finally:
    client.loop_stop() # 停止迴圈
    client.disconnect() # 斷開連接
