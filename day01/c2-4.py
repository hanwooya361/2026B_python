# 135p. , "문자열".format(값)
string_a = "age:{}".format(10)
print(string_a) # age:10
string_b = "{} {} {}".format(1 , "안녕", True)
print(string_b)
# 주의할점: {}개수와 값의 개수는 일치 해야함

# 137p~140p 생략 
# 141p. 
a = "Hello"
print(a.upper())    # HELLO
print(a.lower())    # hello
# 142p. 양쪽 여백/공백 제거
a = " hello python "
print(a.strip())
# 143p. isOOO 구성 확인 , 반환타입 True/False 
print("HELLO".isalpha())    # True
print("HELLO".isdigit())    # False
# 144p. find() vs indexOf()
output_a = "안녕안녕하세요".find("안녕")
print(output_a) # 0: 인덱스
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b) # 2: 인덱스
output_c = "안녕안녕하세요".find("hello")
print(output_c) # -1: 없다.
# 145p. 찾을값 in 문자열 , 없으면 False 있으면 True
print("안녕" in "안녕하세요")   # True
print("잘자" in "안녕하세요")   # False
# 145p. "문자열".split(기준문자) , 반환타입 : 리스트
a = "10 20 30 40 50".split(" ") # 공백 기준으로 자르기
print(a)    # 리스트 , ['10', '20', '30', '40', '50']
# 146p. f-문자열 vs format 사용하는 이유
num = 10
a1 = "age:{}".format(num)        # 숫자10 , 변수호출
a2 = f"age:{num}"                # 숫자10 , 변수호출
a3 = "age:num"                   # 문자열10 , 변수호출x



r_input = input("구의 반지름을 입력해주세요: ")
r = int(r_input)
pi = 3.141592
a = 4 / 3 * pi * (r**3)
b = 4 * pi * (r**2)
print("구의 부피는" , a , "입니다.")
print("구의 겉넓이는" , b , "입니다.")

under_input = input("밑변의 길이를 입력해주세요: ")
u = int(under_input)
height_input = input("높이의 길이를 입력해주세요: ")
h = int(height_input)
hypotenuse = (u**2 + h**2) ** (0.5)
print("빗변의길이는" , hypotenuse , "입니다.")