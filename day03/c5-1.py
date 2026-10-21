# 함수란? 코드의 집합
    # 값저장 = 변수 , 실행코드저장 = 함수
    # 값여러개저장 = 리스트/딕셔너리/튜플
# 매개변수? 함수를 호출할 때는 괄호 내부에 여러가지를 넣는 변수
# 리턴값? 함수를 호출해 최종적으로 나오는 결과

# def 함수명(매개변수명) :
#    실행문

# 값 재사용 = 변수 , 코드 재사용 = 함수 / 반복문(반복패턴존재)
# 회원가입 함수 , 회원목록에서 중복아이디찾기 = 반복문

# 1. 기본적인 함수
def print_3_time() :
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_time()
# vs , 식별자 차이 71p. 변수/함수명
for i in range(0, 3, 1) :
    print("안녕하세요")
# 2. 매개변수? 매개(중매-서로 다른 곳에서 연결), 인수/인자값 -> 매개변수
def print_n_times(value, n) :
    for i in range(n) :
        print(value)
print_n_times("안녕하세요", 5)  # 인수/인자값? 함수 호출할 때 매개변수에 전달하는 값
print_n_times("안녕하세요", 3) 
# print_n_times("안녕하세요")     # 매개변수는 약속이고 어기면 실행x 

# 278p. 가변 매개변수
# 조건1: 가변매개변수가 가장 뒤로 정의한다 , 조건2: 1번만 사용
# def 함수명(매개변수, 매개변수, *가변 매개변수) :
def print_n_times2(n , *values) :
    for i in range(n) : # 3번반복
        for value in values :
            print(value)
        print()
print_n_times2(3, "안녕하세요", "즐거운", "파이썬")
print_n_times2(2, "안녕하세요", "즐거운")

# 279p. 기본 매개변수, 매개변수에 기본값 대입 형태, 인수/인자 값 생략시 적용
def print_n_times3(value, n=2):
    for i in range(n) :
        print(value)
print_n_times3("안녕하세요")        # 생략시 2번 기본값
print_n_times3("안녕하세요", 3)     # 3번

# 280p. 
# 기본매개변수가 가변매개변수보다 앞에 올때, 오류
# 가변매개변수가 기본매개변수보다 앞에 올때, 기본매개변수 인자값 없다
# 해결방안: 키워드 매개변수
print("안녕하세요", end="\n")   # end매개변수는 출력 후 무엇을 할지 # \n 기본값 = 기본매개변수
print("안녕하세요", end="")     # 키워드매개변수란? 인수 대입시 매개변수명 지정
def print_n_times4(*values, n=2):
    # *매개변수 --> 가변매개변수 , 매개변수명 = 기본값 --> 기본매개변수
    for i in range(n) :
        for value in values :
            print(value)
        print()
print_n_times4("안녕하세요", "즐거운", "파이썬", n=3)   # 인수 전달시 매개변수명 지정 , 3번반복
print_n_times4("안녕하세요", "즐거운", "파이썬", 3)     # 2번반복

# 285p. 