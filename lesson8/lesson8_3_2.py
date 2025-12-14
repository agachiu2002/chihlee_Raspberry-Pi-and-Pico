from machine import Pin
from time import sleep_ms

# --- 參數設定 (綠色改 GP21) ---
BUTTON_PIN = 15
RED_LED = 14
GREEN_LED = 21   # ← 綠色LED 正極接 GP21

# 初始化
red_led = Pin(RED_LED, Pin.OUT)
green_led = Pin(GREEN_LED, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

led_mode = 0  # 0=全滅, 1=紅亮, 2=綠亮
last_button_state = 0  # PULL_DOWN，預設為低電位

while True:
    current_button = button.value()
    
    # 偵測按鈕從「放開」變成「按下」的瞬間 (上升邊緣)
    if last_button_state == 0 and current_button == 1:
        # 防彈跳延遲
        sleep_ms(50)
        
        # 再次確認按鈕確實被按下
        if button.value() == 1:
            led_mode = (led_mode + 1) % 3
            
            red_led.off()
            green_led.off()
            
            if led_mode == 1:
                red_led.on()
            elif led_mode == 2:
                green_led.on()
    
    # 更新按鈕狀態
    last_button_state = current_button
    
    # 小延遲減少 CPU 使用
    sleep_ms(10)
