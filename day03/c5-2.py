# 293p. 재귀함수, 자기 자신 호출
# 1] 팩토리얼
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output
print(factorial(2))
print(factorial(3))
# 2] 팩토리얼 재귀
def factorial2(n):
    if n == 0:
        return 1
    else :  # 재귀 
        return n * factorial2(n-1)
print(factorial2(2))
print(factorial2(3))

# 구구단
for 단 in range(2, 10, 1) :
    for 곱 in range(1, 10, 1) :
        print(단*곱)
# 3단/4곱 까지의 반복문 순서도
# 단이 2일때 
# 단이 3일때  

# 구구단 재귀
def 구구단(단=2, 곱=1):
    if 단 > 9 :
        return 
    if 곱 > 9 : # 단 올리기
        구구단(단+1, 1)
        return 
    print(단*곱)
    구구단(단 , 곱+1)   # 곱 올리기
구구단()
    