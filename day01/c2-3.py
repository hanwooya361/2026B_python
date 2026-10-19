# 115p. 변수
pi = 3.1415926535   # 변수명 = 값
r = 10              # 변수명 = 값
# r2                # 초기값 없으면 NameError;
print(pi , r)  # 변수의참조
print(2 * pi * r)

# 116p. 복합대입연산자
number = 100
number += 10    # 110
number -= 10    # 100
number *= 2     # 200
number /= 2     # 100.0
number %= 3 
print(number)
number = "안녕하세요"
number += "!"   # 안녕하세요!
number *= 3     # 안녕하세요!안녕하세요!안녕하세요!
print(number)

# 118p. 입력함수 , 반환타입: 문자열str
input("인사말을 입력하세요>")
string = input("입력>")     # 입력받은값 변수에 저장
print(type(string))         # 123 -> str , 안녕 -> str
# 121p. 타입변환 , str -> int/float
string_int = int(string)
string_float = float(string)
print(type(string_int) , type(string_float))
# <class 'int'> <class 'float'>
string_str = str(string_int)
print(type(string_str))
# 주의할점: "a3" --> 숫자타입 변환 안됨, 소수점있는 문자열을 int 변환 안됨

# 125p.
raw_input = input("inch 단위의 숫자를 입력해주세요: ")
inch = int(raw_input)
cm = inch * 2.54
print(inch, "inch는 cm 단위로", cm, "cm입니다.")