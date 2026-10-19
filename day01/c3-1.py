# 비교연산자
    # == , != , > , < , >= , <=
# 158p. 범위논리
x = 25
print(10 < x < 30)
# 논리연산자
    # not , and , or
print(not True)             # False
print(True and True)        # True
print(True and False)       # False
print(True or False)        # True
# 163p. if조건문
# if 조건식 :
#     (tab들여쓰기) 참이면
age = 10
if age >= 19 :
    print('성인입니다.')
# if ~ else
# if 조건식 :
#     (tab들여쓰기) 참이면
# else :
#     (tab들여쓰기) 거짓이면 
number = 13
if number % 2 == 0 :
    print('짝수입니다.')
else : 
    print('홀수입니다.')
# if ~ elif ~ elif ~ elif ~ else :
point = 85
if point >= 90 :
    print('A')
elif point >= 80 :
    print('B')
elif point >= 70 :
    print('C')
else :
    print('탈락')
# 주의할점 : if ~ if ~ if ~ else vs if ~ elif ~ elif ~ else
# 다수조건에 다수결과 vs 다수조건에 1개결과

# if중첩
x = 10
if x > 5 :
    if x > 10 :
        print('10보다 크다')
    else : 
        print('5보다 크고 10보다 작다')
else : 
    print('5보다 작다')

# 182p. False 되는 경우
# None , 0 , 0.0 , 빈 문자열, 리스트 , 객체 등
# 그 외 true
