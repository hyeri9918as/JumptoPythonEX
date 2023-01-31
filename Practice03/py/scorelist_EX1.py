scorelist = [90, 25, 67, 45, 80]  # 학생들의 시험 점수 리스트 
number = 0     # 학생들에게 붙여줄 번호 

for score in scorelist :  # 90, 25, 67, 45, 80을 순서대로 score 변수에 대입 
    number = number + 1   
    
    if score >= 60 :    # 60점 이상일 경우 
        print("%d번 학생은 합격입니다." % number)
    else : 
        print("%d번 학생은 불합격입니다." % number)