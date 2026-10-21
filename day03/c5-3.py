# 317p. 
# 튜플이란? 여러 자료들을 저장하는 리스트와 비슷한 자료형 
# 특징 : 초기화 이후 수정 불가능
# 사용처: 읽기 모드용 VO , 리스트보다 메모리 효율좋다
# (요소, 요소, 요소)

# 1. 튜플선언
tuple_test = (10, 20, 30)
# 2. 요소값 호출
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
# 3. 요소값 수정, 불가능
tuple_test[0] = 40
# 4. 요소 하나인 경우
tuple_test2 = (273, )   # 뒤에 ,쉼표 없으면 일반값 취급
print(tuple_test2)
# 5. 튜플은 소괄호 생략 가능
(a,b) = (10,20)
print(a,b)
a,b = 10,20
print(a,b)
# - 스왑 / 구조분해
a,b = b,a
print(a,v)
# - 리액트(js)에서 비슷한 문법 존재 -> 구조분해
c,d = [30,40]
print(c,d)

# 6. 함수/연산 결과는 항상 1개
def test():
    return 10,20    # 결과는 1개(10과20 튜플로 묶은 튜플 1개)

# 7. 콜백함수 : 함수 그자체를 매개변수로 전달해 전달받은 곳에서 전달받은 함수 호출
# 리액트: onClick(회원가입()) [x] ---> onClick(회원가입) [o]
def call_10_items(func):
    func()
def print_hello():
    print("안녕하세요")

call_10_items(print_hello())    # print_hello() 결과값 전달
call_10_items(print_hello)      # print_hello 함수 정보 전달
