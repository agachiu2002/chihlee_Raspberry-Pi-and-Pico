from machine import Pin
from time import sleep

# 這是您設定的引腳號碼，例如 ESP32/ESP8266 的 GPIO 15
led_pin = 15

# 📢 修正點: 使用大寫的 Pin 類別來實例化
# led = Pin(led_pin, Pin.OUT)
led = Pin(led_pin, Pin.OUT) # 設置引腳 15 為輸出模式

while(True):
    led.toggle()
    sleep(2)
#led.value(1) # 使用 .value() 設定為高電位 (ON)
# 或者使用 led.on() 也可以，但 .value() 是更通用的方法

#print("LED 已經開啟")

# 可以加入一個小迴圈讓它閃爍
# try:
#     while True:
#         led.value(not led.value()) # 切換狀態
#         time.sleep_ms(500)         # 暫停 500 毫秒
# except KeyboardInterrupt:
#     led.value(0) # 退出時確保 LED 關閉
#     print("程式終止，LED 關閉")