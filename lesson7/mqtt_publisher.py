"""
MQTT 發布者範例 - 只發布訊息，不訂閱
適用於 Pico W (MicroPython)
"""

import wifi_connect as wifi
import time
from umqtt.simple import MQTTClient

# ========== MQTT 設定 ==========
MQTT_BROKER = "192.168.1.100"  # 請改成您的 MQTT Broker IP
MQTT_PORT = 1883
MQTT_CLIENT_ID = "pico_publisher"  # 客戶端 ID
MQTT_TOPIC = "pico/sensor"  # 發布主題

# ========== WiFi 連線 ==========
print("正在連線 WiFi...")
wifi.connect()
print("IP:", wifi.get_ip())

# ========== MQTT 連線 ==========
def connect_mqtt():
    """連線到 MQTT Broker"""
    try:
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, MQTT_PORT)
        client.connect()
        print(f"✅ 已連線到 MQTT Broker: {MQTT_BROKER}:{MQTT_PORT}")
        return client
    except Exception as e:
        print(f"❌ MQTT 連線失敗: {e}")
        return None

# ========== 主程式 ==========
def main():
    # 連線 MQTT
    client = connect_mqtt()
    if client is None:
        print("無法連線 MQTT，程式結束")
        return
    
    # 主循環 - 每隔 10 秒發布一次
    counter = 0
    while True:
        try:
            # 準備要發布的資料
            # 這裡可以加入感測器資料，例如：
            # temperature = 25.5
            # humidity = 60.0
            # message = f'{{"temp": {temperature}, "humidity": {humidity}}}'
            
            message = f"測試訊息 #{counter}"
            
            # 發布訊息
            client.publish(MQTT_TOPIC, message)
            print(f"📤 [{counter}] 已發布: {message} 到主題: {MQTT_TOPIC}")
            
            counter += 1
            time.sleep(10)  # 等待 10 秒
            
        except KeyboardInterrupt:
            print("\n程式中斷")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
            time.sleep(5)
    
    # 斷開連線
    try:
        client.disconnect()
        print("已斷開 MQTT 連線")
    except:
        pass

if __name__ == "__main__":
    main()

