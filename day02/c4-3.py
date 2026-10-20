# 231p.
# 범위함수: range()
# 1. range(끝값) , 시작값 생략시 0부터
print(range(5)) # range(0,5)
print(list(range(5)))   # [0, 1, 2, 3, 4]
# 2. range(시작값, 끝값) 
print(list(range(3,6)))
# 3. rnage(시작값, 끝값, 단계)
print(list(range(0,10,2))) # 0부터 2씩증가

# 233p.
# for과 range함수 함께, for 반복변수 in range() :
# 1] 1부터 10까지 출력
for i in range(1, 11) :
    print(i)
# 2] 10부터 1까지 출력
for i in range(10, 0, -1) : 
    print(i)
# 3] 1부터 10까지 홀수만 출력
for i in range(1, 11, 2) :
    print(i)

# 4] 구구단
for 단 in range(2, 10, 1) :
    for 곱 in range(1, 10, 1) :
        print(단*곱)

# 240p.
# while 조건식: 조건이 True이면 실행코드 반복실행, False 반복 종료
#       실행코드
# 1] 1부터 10까지 출력
i = 1
while i < 10 :
    print(i)
    i += 1
# 2] while과 리스트
list_a = [1,2,1,2]
value = 2
while value in list_a :
    list_a.remove(value)

# 244p. break, continue 키워드 : 반복문에서 사용하는 키워드
for i in range(1, 11, 1) :
    print(i)
    if i == 3 :
        break
for i in range(1, 11, 1) :
    print(i)
    if i == 3 : 
        continue
