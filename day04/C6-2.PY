# 예외객체란? 발생한 예외 정보 갖는 객체
# 예외클래스: Exception(예외 최상위클래스)
# except 예외클래스명 as 변수명: 
# as 키워드 : 클래스의 객체변수 생성
# 그외 모든 예외 처리 : 여러개 except에서 Exception은 항상 마지막에 위치
# 주의할점 : Exception 앞에 위치하면 아래 에외가 작동 안함 -> 상속개념
# raise : 강제로 예외발생 , 주로 CRUD 실패 의미
 
# 383p.
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수입력: "))
    print(list_number[number_input])
    raise NotImplementedError 
except ValueError as e :    # 타입변환 예외
    print(e)
except IndexError as e :    # 인덱스 예외
    print(e)
except Exception as e :     
    print(e)

# Global
a = 10          # 전역스택
def 함수():
    global a
    # 단순 전역변수 호출이면 global 생략 o
    # 전역변수 수정하면 global 필수
    a = a + 1   # UnboundLocalError
    print(a)    # global 없어도 전역스택 호출 가능
    b = 20      # 함수스택
함수()