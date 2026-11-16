import pandas as pd
url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
df = pd.read_csv(url)
X = df[['alcohol', 'sugar', 'pH']]
Y = df['class'] 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
## 1) lightGBM
from lightgbm import LGBMClassifier # 0레드 1화이트 와인 종류 분류
model = LGBMClassifier(
    # 다양한 매개변수(파라미터) 설정
    n_estimators=100,       # 추정기(모델) 최대 개수 설정, 기본값 100, 넉넉하게 넣고 조기 종료
    learning_rate=0.05      # 2) 학습률(각 트리의 축소 비율), 기본값 0.1
    num_leaves=15,          # 3) 하나의 트리(모델) 가질 수 있는 최대 리프 노드 수()
    max_depth=6,            # 4) 하나의 트리 최대 깊이, 기본값-1(무제한), 
    min_child_samples=20,   # 5) 리프 노드 최소 샘플 수
    subsample=0.8           # 6) 매 학습마다 랜덤으로 80%만 학습
    subsample_freq=1,       # 7) 6과 같이 설정하되, 매 트리마다 배깅을 활성화
    colsample_bytree=0.8,   # 8) 매 학습마다 랜덤으로 전체 특성 중 80%만 무작위 선택 학습
    class_weight="balanced" # 9) 분류모델에서 타깃/종속 변수에 비율 불균형 보정/완화
    verbose=-1,             # 매 학습마다 로그 숨김
    random_state=42, n_jobs=-1, 
)