import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 윈도우 기준 한글 폰트 설정 및 마이너스 부호 깨짐 방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 시본 기본 테마 적용 (폰트 설정 유지)
sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')

np.random.seed(42)
n = 100
df = pd.DataFrame({
  '나이': np.random.randint(20, 60, size=n),
  '소득': np.random.randint(2500, 9000, size=n),
  '신용점수': np.random.randint(500, 850, size=n),
  '멤버십': np.random.choice(['일반', 'VIP'], size=n, p=[0.7, 0.3]),
  '이탈여부': np.random.choice([0, 1], size=n, p=[0.75, 0.25]) # 0: 유지, 1: 이탈
})
# 나이가 많을수록 소득이 높은 경향 부여
df['소득'] += df['나이'] * 40

# 1] 카운트플롯(범주형 빈도 집계), sns.countplot(data=데이터프레임, x="범주컬럼명", hue="그룹컬럼명", palette="색상테마")
sns.countplot(data=df, x="멤버십", hue="이탈여부", palette="Set1")
plt.title("멤버십 등급별 이탈빈도")
# 범례
plt.legend(title="이탈 여부", labels=['유지(0)', '이탈(1)'])
plt.show()

# 2] 박스플롯(범주형 수치 분포) , sns.boxplot(data=데이터프레임, x="범주컬럼명". y="수치컬럼명", hue="그룹컬럼명")
sns.boxplot(data=df, x="멤버십", y="소득", hue="이탈여부", palette="Pastel2")
plt.title("멤버십 이탈 여부에 따른 연소득")
plt.xlabel("멤버십 등급")
plt.ylabel("연소득")
plt.show()

# 3] 히트맵(서로다른 변수들 간의 상관관계 파악)
# 상관관계 : 하나의 변수의 값이 변하면 다른 변수의 값은 증가/감소 관계 수치     
# 데이터프레임.corr() 상관계수 행렬 계산
# 문자열(범주형) 제외한 수치형만 추출
numeric_df = df[['나이', '소득', '신용점수']]
corr_matrix = numeric_df.corr() # 상관계수 행렬 계산
# 1) 히트맵 sns.heatmap(상관관계행렬, cmap="색상맵", fmt="소수점형식" )
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("상관관계 히트맵")
plt.show()

# 4] 산점도