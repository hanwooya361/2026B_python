import numpy as np
# 1] 배열의 인덱싱
x = np.array([10,20,30,40,50])
print(x[0]) # 10
print(x[-2]) # 40
print(x[[0,2]]) # [[특정인덱스, 특정인덱스]]
print(x[x>20])  # [논리조건] [30 40 50]

# 2] 2차원 인덱싱
x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(x[0,0])   # 1
print(x[1,2])   # 6
print(x[-1,-1]) # 9
print(x[x>5])

# 3] 슬라이싱, [시작인덱스 : 끝인덱스-1 : 단계]
x = np.array([10,20,30,40,50])
print(x[1:4])   # 20 30 40
print(x[ :3])   # 시작인덱스 생략시 0 , 10 20 30 
print(x[-3 : ]) # 끝인덱스 생략시 마지막인덱스 , 30 40 50
print(x[ : : 2])# 10 30 50 , 2칸씩이동

# 4] 
x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(x[ : , 1])    # 행: 전체, 열: 1 , 2 5 8
print(x[1, : ])     # 행: 1행, 열: 전체 , 4 5 6
print(x[0:2, 1:3])  # 행: 0~1, 열: 1~2열

# 5] 슬라이싱 주의할점:
x = np.array([10,20,30,40,50])
y = x[1:4]  # 20 30 40
y[0] = 100
print(x)    # 10 100 30 40 50, 원본도 같이 변경!
y2 = x[1:4].copy()  # 슬라이싱에서 .copy() , 원본 변경 안함
y2[0] = 1000
print(x)

# 6] 배열의 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)  # 같은 위치끼리 더함
print(x*y)
print(x**2)
print(np.sqrt(x))
print(x>2)  # [False False True]
print((x>1) & (x<3))    # False True False
print((x==1) | (x==3))
print(x>y)  # 같은 위치끼리 비교

# 배열 간 비교/연산 : 같은 위치끼리 비교/연산
# 스칼라(단일숫자)와 배열 비교/연산: True/False or 결과
