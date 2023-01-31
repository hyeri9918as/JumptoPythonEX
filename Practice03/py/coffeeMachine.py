coffee = 5

while True : 
    money = int(input("돈을 넣어 주세요: "))    # 입력 받은 int 값을 money 변수에 대입 
    
    if money == 300 :   # 돈을 300원 입력하면 
        print("커피가 나옵니다.")   # print 문과 함께 커피 개수가 하나 줄어든다. 
        coffee = coffee - 1
        print("남은 커피의 양은 %d개 입니다." % coffee)
        
    elif money > 300 :  # 돈을 300원 이상으로 입력하면 
        print("거스름돈 %d가 나옵니다. 거스름 돈과 커피를 받으세요. " % (money-300))
        coffee = coffee -1   #입력한 돈에서 300원을 뺀 후 남은 돈과 함께 print 문 출력 / 커피 개수가 하나 줄어든다. 
        print("남은 커피의 양은 %d개 입니다." % coffee)
        
    else:    # 입력한 돈이 300원 미만인 경우 
        print("돈을 다시 돌려드립니다. 커피가 나오지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
        
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break