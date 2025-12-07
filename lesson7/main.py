import wifi_connect as wifi
import time
from umqtt.simple import MQTTClient

# MQTT 設定
MQTT_BROKER = "10.188.131.25"  # 公開測試用 Broker
MQTT_PORT = 1883
CLIENT_ID = "pico_w_publisher"
TOPIC = "pico/#"
KEEPALIVE = 60  # 保持連線時間（秒）

# 嘗試連線 WiFi
wifi.connect()

# 顯示 IP
print("IP:", wifi.get_ip())

# 建立 MQTT 連線函式
def connect_mqtt():
    """建立並連線到 MQTT Broker"""
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, keepalive=KEEPALIVE)
    client.connect()
    return client

# 建立 MQTT 連線
print("正在連接 MQTT Broker...")
client = connect_mqtt()
print(f"已連接到 {MQTT_BROKER}")

# 每隔 10 秒發布一次訊息
counter = 0
while True:
    try:
        counter += 1
        message = f"Hello from Pico W! #{counter}"
        
        print("-" * 30)
        client.publish(TOPIC, message)
        print(f"已發布訊息: {message}")
        print(f"主題: {TOPIC}")
        
        print("等待 10 秒後再次發布...")
        time.sleep(10)
        
    except OSError as e:
        print(f"❌ 連線錯誤: {e}")
        print("嘗試重新連線...")
        try:
            client.disconnect()
        except:
            pass
        
        # 重新連線
        time.sleep(2)
        try:
            client = connect_mqtt()
            print(f"✅ 重新連線成功！")
        except Exception as reconnect_error:
            print(f"❌ 重新連線失敗: {reconnect_error}")
            print("等待 5 秒後再試...")
            time.sleep(5)