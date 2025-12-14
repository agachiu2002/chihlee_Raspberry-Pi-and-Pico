from machine import ADC, Pin, PWM
from time import sleep
import math

# 初始化
potentiometer = ADC(Pin(28))
led = PWM(Pin(15))
led.freq(1000)

while True:
    # 讀取可變電阻值決定速度
    pot_value = potentiometer.read_u16()
    
    # 映射到 0.5 ~ 5 秒的週期
    period = 5 + (pot_value / 65535) * 4.5
    
    # 呼吸效果
    for i in range(100):
        # 使用正弦函數產生平滑的亮度變化
        brightness = int((math.sin(i * math.pi / 50) ** 2) * 65535)
        led.duty_u16(brightness)
        sleep(period / 100)