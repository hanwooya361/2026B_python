# 판다스 : 데이터 조작 및 분석(표형태) 라이브러리
import pandas as pd
print(pd.__version__)

# 1] 데이터프레임: 2차원(표), pd.DataFrame(리스트/딕셔너리, colums=['열이름','열이름'])
data_list = [ [ 'ant' , 25 , 'seoul'] , ['bee' , 30 , 'busan'] , ['cat' , 35 , 'incheon'] ]
x = pd.DataFrame(data_list)
print(x)
x = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print(x)
# 2] 데이터프레임2, pd.DataFrame(딕셔너리), 키(열이름)
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] }
df = pd.DataFrame(data_dict)
print(x)
# 3] 특정 컬럼 값들을 추출, df['열이름'],
ages = df['age']    
print(ages) # Series(1차원)
print(type(ages))   # <class 'pandas.Series'>
print(type(ages.values))  # <class 'numpy.ndarray'>

# 4] 데이터프레임3 : 넘파이
import numpy as np
data_np = np.array(data_list)   # 넘파이 자료
df = pd.DataFrame(data_np, columns=['name', 'age', 'city'], index=['A', 'B', 'C'])
print(df)

# 매크로(프로그램) -> RPA

# 5] 주요 속성
print(df.shape)     # 행/열 크기 / 확인해서 전처리 많이함
print(df.columns)   # Index(['name', 'age', 'city'], dtype='str')
print(df.index)     # 컬럼목록
print(df.values)    # 값만 목록
print(df.head(2))   # 상위 n개만 반환
print(df.tail(2))   # 하위 n개만 반환
df.info()   # 컬럼이름, 결측치, 타입 확인

# 6] 인덱싱 = df.iloc[행인덳, 열인덱스] / df.loc[행라벨, 열라벨]
print(df.iloc[1])           # 1행
print(df.iloc[1,2])         # busan
print(df.loc['B'])          # 1행
print(df.loc['B', 'city'])  # busan
# 7] 슬라이싱, [시작인덱스:끝인덱스], [행슬라이싱, 열슬라이싱]
print(df.iloc[0:2, 0:1])
print(df.loc['A':'C', 'name':'age'])

# 8] 열 추가, df[새로운열] = 새로운값
df['score'] = [100,80,95]
print(df)
# 9] 값 수정, df[수정할열] = 새로운값
df['age'] = [31,52,40]
print(df)
df.loc['B', 'age'] = 70 # B행age열
print(df)
df.iloc[0,0] = 'apple'
print(df)
# 10] 여러개 수정, [[수정할행,수정할행], 수정할열]
df.loc[['A','B'], 'score'] = [50,60]
print(df)
# 11] 필터링(조건),
print(df['score']>70)
#A    False
#B    False
#C     True
print(df[df['score']>70])
#    name  age     city  score
# C  cat   40  incheon     95
cont = df['age'] >= 40
print(df[(df['score']>70) & cont])
print(df[(df['score']>70) | cont])
# 필터링 이용해 새로운 열
df['passed'] = False
df.loc[df['score'] > 70, 'passed'] = True
print(df)
