from machine import Pin
import time

# 紅色組 (按鍵 GP19 控制 LED GP20)
RED_BUTTON = 19
RED_LED = 20
red_led = Pin(RED_LED, Pin.OUT)
red_button = Pin(RED_BUTTON, Pin.IN, Pin.PULL_DOWN)
red_state = False
red_last = False

# 綠色組 (按鍵 GP17 控制 LED GP19)
GREEN_BUTTON = 17
GREEN_LED = 19
green_led = Pin(GREEN_LED, Pin.OUT)
green_button = Pin(GREEN_BUTTON, Pin.IN, Pin.PULL_DOWN)
green_state = False
green_last = False

while True:
    # 紅色按鍵控制
    red_current = red_button.value()
    if red_current and not red_last:
        red_state = not red_state
        red_led.value(red_state)
        time.sleep(0.3)
    red_last = red_current
    
    # 綠色按鍵控制
    green_current = green_button.value()
    if green_current and not green_last:
        green_state = not green_state
        green_led.value(green_state)
        time.sleep(0.3)
    green_last = green_current
    
    time.sleep(0.01)
