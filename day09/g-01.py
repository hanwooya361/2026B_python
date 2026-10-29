import matplotlib.pyplot as plt
import numpy as np
# 맷플롯립: 파이썬에서 시각적을 표현하는 라이브러리
# 한글폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 1] 선 차트
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]
# 1) 차트의 전체크기 설정: plt.figure(figsize=(가로inch, 세로inch))
plt.figure(figsize=(7,4))
# 2) 선차트: plt.plot(x축값,y축값,label="계열명", color="색상명", linestyle="선종류", marker="점모양")
plt.plot(epochs, train_loss, label="Train Loss", color="blue", linestyle="-", marker="o")
plt.plot(epochs, val_loss, label="Var Loss", color="red", linestyle="--", marker="s")
plt.title("학습별 모델 손실 추세") # 3) 차트 제목
plt.xlabel("학습수")    # 4) x축 제목
plt.ylabel("손실")      # 5) y축 제목
plt.grid(True)          # 6) 구분선
plt.legend()            # 7) 범례 표시
plt.show()  # 차트 실행

# 2] 막대 차트(비교) plt.bar(x값, y값, color=[색상], width=막대크기) , 선 차트(추세)
classes = ['Cat', 'Dog', 'Bird', 'Fish']
counts = [120, 150, 80, 45]
bars = plt.bar(classes, counts, color=['red','blue','green','black'], width=0.5)
# 2) 막대 값 레이블
# plt.bar_label(막대차트변수, padding=막대와레이블간격, fontsize=폰트크기) 
plt.bar_label(bars, padding=3, fontsize=8) 
plt.title("클래스별 샘플수")
plt.xlabel("클래스")
plt.ylabel("샘플 수")
plt.grid(True, alpha=0.5)  # alpha= 투명도
plt.show()

# 3] 산점도(상관관계) 
x = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
y = [2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5]
# 1) 산점도 , plt.scatter(x축값, y축값, color="색상", s=점크기, alpha=투명도, edgecolors="테두리색")
plt.scatter(x, y, color="purple", s=80, alpha=0.8)
plt.title("공부시간과 시험점수의 상관관계")
plt.xlabel("공부시간")
plt.ylabel("시험점수")
plt.show()

# 4] 히스토그램 (연속형 수치/ 값 분포)
# 평균 170을 중심으로 표준편차 5만큼 퍼져있는 종모양(가우시안분포) 난수 1000개
heights = np.random.normal(loc=170, scale=5, size=1000)
# 1) 히스토그램, plt.hist(값, bins="구간수", color="색상", alpha=투명도)
plt.hist(heights, bins=30, color="skyblue", edgecolor="black")
plt.title("키 데이터의 정규분포")
plt.xlabel("키(cm)")
plt.ylabel("빈도수")
plt.show()

# 5] 박스플롯(분포 범위내 이상치) 
heights = np.random.normal(loc=170, scale=5, size=1000)
data_with_outliers = np.append(heights, [210, 215, 120])
# 1) 박스플롯, plt.boxplot(값) , 데이터들을 사분위수(25% 50% 75%) 표현
plt.boxplot(data_with_outliers)
plt.show()