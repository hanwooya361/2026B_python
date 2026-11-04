# 사이킷런? 방대한 머신러닝 알고리즘 모델 라이브러리

# 머신러닝 목표: 추론/예측 과정
# 특성: 모델이 학습하는 자료 정보 , 타깃 : 모델이 맞혀야하는 정답 정보

# 지도학습: 특성과 타깃을 모두 제공해 학습 (회귀/분류)
# 비지도학습 타깃없이 특성만으로 제공해 학습 (군집/토픽/주성분분석)

# 1] 단순 선형 회귀
# 1) 판다스로 자료 불러오기
import pandas as pd
df= pd.read_csv('./Fish.csv')
df.info()
# 2) 모델 학습에 사용할 데이터 추출
feature = ['Length2'] # 특성: Length2 (물고기의 대각선 cm), 사이킷런 모델 구조상 학습할 특성은 2차원
target = 'Weight'   # 타깃: Weight  (물고기의 무게 g)
# 3) 독립변수/입력변수/특성/x , 종속변수/목표변수/타깃/y 구조
X = df[feature] # 2차원
Y = df[target]  # 1차원

# 4) 데이터 분리, 학습용/테스트용 나누기, 학습과 평가/예측성능 자료 구분
from sklearn.model_selection import train_test_split
# 특성학습자료, 특성테스트자료, 타깃학습자료, 타깃테스트자료 = train_test_split(특성, 타깃, test_size=비율, random_state=난수시드값)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# 훈련세트: 모델에서 규칙을 찾는 자료
# 테스트세트: 모델 학습 후 모델 평가/예측성능 점수/지표

# 5) 단순 선형회귀 모델
from sklearn.linear_model import LinearRegression
model = LinearRegression()  # 파이썬 객체화
# 6) 모델 학습, model.fit(특성자료, 타깃자료)
model.fit(X_train, Y_train)
# 7) 모델 가중치/기울기 확인, model.coef_ 
print(model.coef_)  # [30.43452394]
# 8) 모델 편향 (y절편) 확인, model.intercept_
print(model.intercept_) # -477.30634978973194
# 9) 학습한 모델 예측, 새로운 x값을 넣어서 y값 구하기, model.predict(2차원특성자료)
print(model.predict([[30]]))    # if 물고기 길이가 30일때 무게 예측
# *) 단순회귀모델: y=ax+b, a=[30.43452394]*[30] + [-477.30634978973194]





