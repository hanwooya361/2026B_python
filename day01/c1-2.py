# 파이썬 파일 만들기
# 파일명 뒤에 확장자(.py) 만든다,
# 파이썬 주석: #

print("hello python") # shift + enter 한줄 실행

# 70p.
import keyword
print(keyword.kwlist)

# 77p.
print("#하나만 출력합니다.")
print("Hello Python Programming!")
print("")
# 주의할점: 쉼표 기준으로 공백 자동포함
print("#여러개 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "제", "이름은", "조현우입니다.")
print("#아무것도 출력하지 않습니다")
print("---확인전용선---")
print()
print()
print("---확인전용선---")

# 85p. 타입 확인하기
print(type("안녕하세요"))   # <class 'str'>
print(type(123))            # <class 'int'>
print(type(1.23))           # <class 'float'>
print(type(True))           # <class 'bool'>
print(type(None))           # <class 'NoneType'>
print(type([]))             # <class 'list'>
print(type({}))             # <class 'dict'>
print(type(()))             # <class 'tuple'>

# 86p. 문자열만들기
print("ABC")                # 큰따옴표 감싼
print('ABC')                # 작은따옴표 감싼
print("""A
B
C""")                       # """여러줄""" 감싼
print("A'B'C")              # 작은따음표 출력
print('A"B"C')              # 큰따음표 출력
print("\"A\'B\nC\tD\\E")    # 제어문자
