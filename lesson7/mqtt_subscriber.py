"""
MQTT 訂閱者範例 - 只訂閱訊息，不發布
適用於 Pico W (MicroPython)
"""

import wifi_connect as wifi
import time
from umqtt.simple import MQTTClient

# ========== MQTT 設定 ==========
MQTT_BROKER = "192.168.1.100"  # 請改成您的 MQTT Broker IP
MQTT_PORT = 1883
MQTT_CLIENT_ID = "pico_subscriber"  # 客戶端 ID
MQTT_TOPIC = "pico/command"  # 訂閱主題

# ========== WiFi 連線 ==========
print("正在連線 WiFi...")
wifi.connect()
print("IP:", wifi.get_ip())

# ========== MQTT 訊息處理 ==========
def on_message(topic, msg):
    """收到 MQTT 訊息時的回調函數"""
    topic_str = topic.decode('utf-8')
    msg_str = msg.decode('utf-8')
    print(f"📨 收到訊息 - 主題: {topic_str}, 內容: {msg_str}")
    
    # 處理收到的指令
    if msg_str == "LED_ON":
        print("💡 執行: 開啟 LED")
        # 在這裡控制 LED
        # machine.Pin(25, machine.Pin.OUT).value(1)
    elif msg_str == "LED_OFF":
        print("💡 執行: 關閉 LED")
        # 在這裡控制 LED
        # machine.Pin(25, machine.Pin.OUT).value(0)
    elif msg_str == "RESTART":
        print("🔄 執行: 重新啟動")
        # machine.reset()
    else:
        print(f"未知指令: {msg_str}")

# ========== 主程式 ==========
def main():
    # 連線 MQTT
    try:
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, MQTT_PORT)
        client.set_callback(on_message)
        client.connect()
        print(f"✅ 已連線到 MQTT Broker: {MQTT_BROKER}:{MQTT_PORT}")
    except Exception as e:
        print(f"❌ MQTT 連線失敗: {e}")
        return
    
    # 訂閱主題
    try:
        client.subscribe(MQTT_TOPIC)
        print(f"✅ 已訂閱主題: {MQTT_TOPIC}")
        print("等待訊息中...")
    except Exception as e:
        print(f"❌ 訂閱失敗: {e}")
        return
    
    # 主循環 - 持續監聽訊息
    while True:
        try:
            # 檢查是否有新訊息（非阻塞）
            client.check_msg()
            time.sleep(0.1)  # 短暫等待，避免 CPU 使用率過高
            
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

