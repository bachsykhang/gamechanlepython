import random
import os

def random_number(): 
    return random.randint(1, 2) 

tienvnd = 500000
bankvnd = 0
cauhoi = "Bạn có muốn tiếp tục không ?"
luachon = "0. Không || 1. Có"
lichsu = []
while True:
    print("Số dư của bạn hiện tại là:",tienvnd)
    # Chọn điều kiện chẵn lẻ
    print("Mời chọn chẵn hoặc lẻ:")
    print("1. Lẻ || 2. Chẵn")
    print("Chọn:")
    chon = int(input())
    print("Con số random ra là: ",random_number())
    if chon == 1:
        print("Bạn chọn lẻ")
    elif chon == 2:
        print("Bạn chọn chẵn")
    else:
        while True:
            print("Vui lòng chỉ chọn 1 hoặc 2")
            print("Chọn:")
            chon = int(input())
            if chon == 1 or chon == 2:                
                break
    # Cải tiến khi chọn đúng or sai
    if(chon == random_number()):
        print("Chúc mừng bạn chọn đúng ^_^")
        tienvnd += 50000
        bankvnd = tienvnd
        lichsu.append(bankvnd)
        print("Lịch sử giao dịch của bạn:",lichsu)
    else:
        print("Rất tiếc, bạn chọn sai :(")
        tienvnd -= 50000
        bankvnd = tienvnd
        lichsu.append(bankvnd)
        print("Lịch sử giao dịch của bạn:",lichsu)
    
    print(cauhoi)
    print(luachon) 
    x = int(input())
    if x == 0:
        break
    else:
        os.system("cls")




