import wifi_connect as wifi #把原本wifi_connect改成wifi
import time

# 嘗試連線 WiFi
wifi.connect()
##def connect(ssid=WIFI_SSID, password=WIFI_PASSWORD, retry=20):
##    """
##    連線到 WiFi。
##    retry = 嘗試次數（每次間隔 1 秒）
##    回傳：連線後的 WLAN 物件
##    """
##1 引述名稱呼叫 (ssid=WIFI_SSID, password=WIFI_PASSWORD, retry=20)
##2 引述位置呼叫 ("ID","password",10)<<改成10次也OK
##3 混和呼叫 : 引述位置+引述名稱呼叫 wifi.connect(retry=10)

# 每隔 10 秒執行一次

# 顯示 IP
print("IP:", wifi.get_ip())
    
# 測試外部網路
while True:
    print("_" * 30)
    if wifi.test_internet():
        print("外部網路 OK")
    else:
        print("外部網路無法連線")
    
    # 等待 10 秒
    print("等待10秒後再次測試......")
    time.sleep(10)