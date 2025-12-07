"""
MQTT 使用範例 - 使用 umqtt.simple
適用於 Pico W (MicroPython)
"""

import wifi_connect as wifi
import time
from umqtt.simple import MQTTClient

# ========== MQTT 設定 ==========
MQTT_BROKER = "192.168.1.100"  # 請改成您的 MQTT Broker IP
MQTT_PORT = 1883
MQTT_CLIENT_ID = "pico_w_client"  # 客戶端 ID（每個設備應該不同）
MQTT_TOPIC_PUBLISH = "pico/sensor"  # 發布主題
MQTT_TOPIC_SUBSCRIBE = "pico/command"  # 訂閱主題

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

# ========== MQTT 訊息處理 ==========
def on_message(topic, msg):
    """收到 MQTT 訊息時的回調函數"""
    topic_str = topic.decode('utf-8')
    msg_str = msg.decode('utf-8')
    print(f"📨 收到訊息 - 主題: {topic_str}, 內容: {msg_str}")
    
    # 可以在這裡處理收到的指令
    if msg_str == "LED_ON":
        print("執行: 開啟 LED")
        # 在這裡控制 LED
    elif msg_str == "LED_OFF":
        print("執行: 關閉 LED")
        # 在這裡控制 LED

# ========== 主程式 ==========
def main():
    # 連線 MQTT
    client = connect_mqtt()
    if client is None:
        print("無法連線 MQTT，程式結束")
        return
    
    # 設定訊息回調函數
    client.set_callback(on_message)
    
    # 訂閱主題
    try:
        client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print(f"✅ 已訂閱主題: {MQTT_TOPIC_SUBSCRIBE}")
    except Exception as e:
        print(f"❌ 訂閱失敗: {e}")
    
    # 主循環
    counter = 0
    while True:
        try:
            # 檢查是否有新訊息（非阻塞）
            client.check_msg()
            
            # 每隔 10 秒發布一次訊息
            if counter % 10 == 0:  # 假設每次循環約 1 秒
                # 準備要發布的資料（可以是感測器資料）
                message = f"Hello from Pico W! Count: {counter}"
                
                # 發布訊息
                client.publish(MQTT_TOPIC_PUBLISH, message)
                print(f"📤 已發布: {message}")
            
            counter += 1
            time.sleep(1)  # 等待 1 秒
            
        except KeyboardInterrupt:
            print("\n程式中斷")
            break
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
            time.sleep(5)  # 發生錯誤時等待 5 秒再繼續
    
    # 斷開連線
    try:
        client.disconnect()
        print("已斷開 MQTT 連線")
    except:
        pass

if __name__ == "__main__":
    main()

