from machine import Timer,Pin
import time
#全域變數，避免每次callback都創建新Pin物件
led = Pin("LED",mode=Pin.OUT)

def callback1000(n):   
for i in range(2):  #閃爍2次 
    led.on() #打開LED
    time.sleep_ms(100) # 亮100毫秒
    led.off()
    if i <1: #最後一次閃爍不要等待
        time.sleep_ms(100) # 亮100毫秒
    led.off()
    
        
    
def main():
    timer = Timer(period=5000, callback=callback1000)
    
if __name__ == "__main__":
    main()