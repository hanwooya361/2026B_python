import numpy as np
# 1] 병합 , vstack([배열1, 배열2])
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])
z = np.vstack([x,y])    # 수직 병합
print(z)
z = np.hstack([x,y])    # 수평 병합
print(z)

# 2] 병합2 , concatenate((배열1, 배열2), axis = 0,1) 0 세로 1 가로
z = np.concatenate((x,y), axis=0)   # axis = 0 세로방향 =1 가로방향
print(z)
z = np.concatenate((x,y), axis=1)
print(z)

# 3] 정렬 , np.sort(배열): 오름차순 , [::-1]: 내림차순
x = np.array([3,1,4,2,5])
print(np.sort(x))
print(np.sort(x)[::-1])
print(x)    # 원본 변경 안됨
x.sort()    # 배열.sort()
print(x)    # 원본 자체 변경
# 4] 값 자체 정렬하지 않고 배열을 정렬 위치순번 반환
score = np.array([75,95,60,88])
z = np.argsort(score)   # 오름차순 기준으로 정렬했을 때 각 위치 번호, [2 0 3 1]
print(z)

# 5] 필터링 , *for 사용안함(장점): 내부적으로는 for사용*
x = np.array([10,20,30,40,50])
print(x>30)
print(x[x>30])  # 인덱싱 안에서 조건식 사용하면 True 값 추출
y = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(y&2==0)
print(y[y%2==0])

# 6] 삼항연산자 , np.where(조건, 참, 거짓)
print(np.where(x>30, x, 0))
print(np.where(y%2==0, 0, 1))

# 7] 다수 조건, & | ~
# 조건 2개 이상이면 () or 변수
a = y%2==0
print(y[a & (y%4==0)])
print(y[a | (y%4==0)])
print(y[~a])    # 짝수가 아닌 