import random
 
def play_game(): #funtion結構化程式 定義funtion--- NAME():
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    #print(target)     #作弊用print(target)會出現目標值
   
    print("===============猜數字遊戲=================:\n")
    while(True):
        count += 1
        keyin = int(input(f"猜數字範圍{min}~{max}: "))
        if(keyin >=min and keyin <= max):
            if(keyin == target):
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"您猜了{count}次")
                break
            elif (keyin > target):
                max = keyin - 1
                print("再小一點")
            elif (keyin < target):
                min = keyin + 1
                print("再大一點")
            print("您已經猜了",count,"次\n")
        else:
            print("請輸入提示範圍內的數字") 

while(True):
    play_game()
    play_again = input("要再挑戰一次?(y,n)")
    if play_again =="n":
        break
    
print("GAME Over")