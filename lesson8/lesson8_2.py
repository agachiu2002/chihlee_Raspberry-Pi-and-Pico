from machine import Pin
from time import sleep

# --- 參數設定 ---
BUTTON_PIN = 14 # 設定按鈕連接的引腳為 GPIO 14
led_pin = 15

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)


while (True):
    #print(button.value())
    #sleep(1) 通常寫程式不寫Sleep
    if button.value() == 1:
        #print("沒按")
        led.off()
    else:
        #print("按下")
        led.on()
    #sleep(1)