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
df = pd.DataFrame(data_np)
print(df)