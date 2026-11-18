# 지도학습 X특성(독립)과 Y타깃(쫑속) 모델에 학습해 예측
# 비지도학습: X특성(독립) 모델 이용해 거리/밀도 군집/클러스터/그룹

import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')
X = df[['studytime', 'absences', 'G1', 'G2', 'G3']]
# 타깃/종속 없다. -> 비지도학습 이라서
from sklearn.model_selection import train_test_split    # 학습98% 검증용2%
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 1) 스케일링/단위표준화 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.fit_transform(X_test)
# 2) 군집=그룹만들기=클러스터, K개의 군집을 찾는 KMeans 모델 , KMeans(n_clusters=k)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)    # 모델생성  주의할점: if 최대학생이 10명일때 클러스터수가 10개이면 
model.fit(X_train_scaled)  # 군집 학습
train_labels = model.predict(X_train_scaled)    # 군집 확인
print('앞에서 20명 그룹 확인:', train_labels[ : 20])  # [0 2 2 0 2 1 2 1 0 1 2 0 2 2 2 0 0 2 1 1] 0 or 1 or 2 집합으로 클러스터링
print('테스트학생:', model.predict(X_test_scaled))

# 3) 시각화 : 특성 여러개 이므로 2d시각화 한계 
import matplotlib.pyplot as plt
plt.scatter(X_train_scaled[ : ,4 ], X_train_scaled[ : , 1 ], c=train_labels)
plt.scatter(X_test_scaled[ : , 4], X_test_scaled[ : , 1], c="red", marker='*')
plt.show()

# 4) 최적의 K(그룹/군집) 수 찾기 VS 지도학습(F1 분류/ R2 회귀)
from sklearn.metrics import silhouette_score
sse_list = []
sil_list = []
for k in range(2,20):
    k_teamp = KMeans(n_clusters=k, random_state=42) # k반복마다 학습 모델생성
    preds = k_teamp.fit_predict(X_train_scaled) # 모델 학습/추론 동시에
    sse_list.append(k_teamp.inertia_)   # 군집 결과 각 샘플과 중심점 거리 제곱의 합 저장
    sil_list.append(silhouette_score(X_train_scaled, preds))   # 실루엣 점수를 저장
plt.plot(range(2,20), sse_list, marker="o")
plt.show()
plt.plot(range(2,20), sil_list, marker="o")
plt.show()
# sse: 엘보우지점(기울기가 완만하게 꺾이는 변곡점) 5~10
# 실루엣: 높은 값 일 수록 이상적                    2
# 두 차트 해석해 최적의 K 해석, 5
# 최적 k 군집하기
best_model = KMeans(n_clusters=5)
pred = best_model.fit_predict(X_train_scaled)
print(pred[:10])    # [4 0 3 1 3 0 3 0 4 0]

# 5) HDBSCAN k-means 다르게 밀도 기반으로 군집 , 이상치(-1) 자동 탐지
from sklearn.cluster import HDBSCAN
# model = HDBSCAN(min_cluster=군집마다의 최소데이터 수, min_samples=군집판별할 떄 계산되는 이웃 수)
# min_cluster_size: 클수록 군집 수 적어진다, min_samples: 클수록 이상치 많아진다.
model = HDBSCAN(min_cluster_size=30, min_samples=2)
pred = model.fit_predict(X_train_scaled)
print(pred) # 군집4개 이상치1개
X_train['hdb_cluster'] = pred   # 군집 결과 판다스열에 추가
print(X_train['hdb_cluster'].value_counts())
# hdb_cluster
# 0    194      1   184
# 1     85      2   89
# 2     56      0   81
#-1     32     -1   33
# 3     20
# min_cluster_size, min_samples   15,5 -> 15,2
# 시각화
noise_mask = (X_train['hdb_cluster']==-1)
plt.scatter(X_train.loc[~noise_mask, 'G3'], X_train.loc[~noise_mask, 'absences'], c=X_train.loc[~noise_mask, 'hdb_cluster'])
plt.scatter(X_train.loc[noise_mask, 'G3'], X_train.loc[noise_mask, 'absences'], c='red', marker='*')
plt.show()
# 지도학습 X특성(독립)과 Y타깃(쫑속) 모델에 학습해 예측
# 비지도학습: X특성(독립) 모델 이용해 거리/밀도 군집/클러스터/그룹

import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')
X = df[['studytime', 'absences', 'G1', 'G2', 'G3']]
# 타깃/종속 없다. -> 비지도학습 이라서
from sklearn.model_selection import train_test_split    # 학습98% 검증용2%
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 1) 스케일링/단위표준화 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.fit_transform(X_test)
# 2) 군집=그룹만들기=클러스터, K개의 군집을 찾는 KMeans 모델 , KMeans(n_clusters=k)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)    # 모델생성  주의할점: if 최대학생이 10명일때 클러스터수가 10개이면 
model.fit(X_train_scaled)  # 군집 학습
train_labels = model.predict(X_train_scaled)    # 군집 확인
print('앞에서 20명 그룹 확인:', train_labels[ : 20])  # [0 2 2 0 2 1 2 1 0 1 2 0 2 2 2 0 0 2 1 1] 0 or 1 or 2 집합으로 클러스터링
print('테스트학생:', model.predict(X_test_scaled))

# 3) 시각화 : 특성 여러개 이므로 2d시각화 한계 
import matplotlib.pyplot as plt
plt.scatter(X_train_scaled[ : ,4 ], X_train_scaled[ : , 1 ], c=train_labels)
plt.scatter(X_test_scaled[ : , 4], X_test_scaled[ : , 1], c="red", marker='*')
plt.show()

# 4) 최적의 K(그룹/군집) 수 찾기 VS 지도학습(F1 분류/ R2 회귀)
from sklearn.metrics import silhouette_score
sse_list = []
sil_list = []
for k in range(2,20):
    k_teamp = KMeans(n_clusters=k, random_state=42) # k반복마다 학습 모델생성
    preds = k_teamp.fit_predict(X_train_scaled) # 모델 학습/추론 동시에
    sse_list.append(k_teamp.inertia_)   # 군집 결과 각 샘플과 중심점 거리 제곱의 합 저장
    sil_list.append(silhouette_score(X_train_scaled, preds))   # 실루엣 점수를 저장
plt.plot(range(2,20), sse_list, marker="o")
plt.show()
plt.plot(range(2,20), sil_list, marker="o")
plt.show()
# sse: 엘보우지점(기울기가 완만하게 꺾이는 변곡점) 5~10
# 실루엣: 높은 값 일 수록 이상적                    2
# 두 차트 해석해 최적의 K 해석, 5
# 최적 k 군집하기
best_model = KMeans(n_clusters=5)
pred = best_model.fit_predict(X_train_scaled)
print(pred[:10])    # [4 0 3 1 3 0 3 0 4 0]

# 5) HDBSCAN k-means 다르게 밀도 기반으로 군집 , 이상치(-1) 자동 탐지
from sklearn.cluster import HDBSCAN
# model = HDBSCAN(min_cluster=군집마다의 최소데이터 수, min_samples=군집판별할 떄 계산되는 이웃 수)
# min_cluster_size: 클수록 군집 수 적어진다, min_samples: 클수록 이상치 많아진다.
model = HDBSCAN(min_cluster_size=30, min_samples=2)
pred = model.fit_predict(X_train_scaled)
print(pred) # 군집4개 이상치1개
X_train['hdb_cluster'] = pred   # 군집 결과 판다스열에 추가
print(X_train['hdb_cluster'].value_counts())
# hdb_cluster
# 0    194      1   184
# 1     85      2   89
# 2     56      0   81
#-1     32     -1   33
# 3     20
# min_cluster_size, min_samples   15,5 -> 15,2
# 시각화
noise_mask = (X_train['hdb_cluster']==-1)
plt.scatter(X_train.loc[~noise_mask, 'G3'], X_train.loc[~noise_mask, 'absences'], c=X_train.loc[~noise_mask, 'hdb_cluster'])
plt.scatter(X_train.loc[noise_mask, 'G3'], X_train.loc[noise_mask, 'absences'], c='red', marker='*')
plt.show()

# 6) PCA(주성분 분석): 고차원 데이터의 분산을 저차원으로 축소해 주 성분/특성만 
# 고차원이란? 다수의 특성들의 가중치/기울기 표현
from sklearn.decomposition import PCA
# PCA(n_components=차원수)
pca = PCA(n_components=2)   # 시각화 하기위한 2차원 축소
X_train_pca = pca.fit_transform(X_train_scaled)
print(X_train_pca)          # 행 마다의 가중치
print(pca.components_.T)    # 주 특성별 가중치

#     주성분1      주성분2  
# [[ 0.13219328 -0.61408979]        공부시간
# [-0.00599139  0.78051288]         결석일수
# [ 0.56213845  0.00343157]         1학기성적
# [ 0.58342273  0.03443535]         2학기성적
# [ 0.57105808  0.11178463]]        3학기성적
# 주성분1에서 강한 상관관계 1학기성정/2학기성적/3학기성적
pca_hdb = HDBSCAN(min_cluster_size=30, min_samples=5)
pca_pred = pca_hdb.fit_predict(X_train_pca) # 5차원에서 2차원으로 축소
X_train['PC1'] = X_train_pca[ : , 0 ]
X_train['PC2'] = X_train_pca[ : , 1 ]
X_train['PCA_cluster'] = pca_pred
print(X_train[['PC1', 'PC2', 'PCA_cluster']].head(5))   
# 클러스터2는 상(PC1에서 강한 양수 이므로) 
# 클러스터1는 하(PC1에서 음의 양수 이므로) 
# 클러스터0는 중(PC1에서 0에 가까운 평균 이므로) 

# 7) 이상치 제외한 G3 평균 계산
normal_clusters = X_train[X_train['PCA_cluster']!=-1]   # 예상치 제외
# pd.groupby('성별')['국어점수'].mean(): 성별끼리 국어점수열에 평균구하기
cluster_means = normal_clusters.groupby('PCA_cluster')['G3'].mean()
sorted_cluster = cluster_means.sort_values(ascending=True)   # 오름차순
print(sorted_cluster)
# PCA_cluster
# 1     9.873239
# 0    12.500000
# 2    13.641509

# 8) 라벨링
# enumerate(),  range()
labels = {}
for idx, cluster_id in enumerate(sorted_cluster.index, start=1):
    labels[cluster_id] = f'Level{idx}'
labels[-1] = 'Outlier'  # 이상치는 리스트 가장 뒤에
print(labels)
# {1: 'Level1', 0: 'Level2', 2: 'Level3', -1: 'Outlier'}
X_train['pca_cluster_label'] = X_train['PCA_cluster'].replace(labels)
print(X_train)  # 군집화한 결과가지고 추후에 지도학습
# 지도학습에서 성능 향상 하기 위한 방법: 0) 전처리,  1) 하이퍼파라미터, 2) 파생변수

# 9) 시각화 
for lbl in list(labels.values()):
    sub = X_train[X_train['pca_cluster_label']==lbl]
    if lbl == 'Outlier' :
        plt.scatter(sub['PC1'], sub['PC2'], c='red', marker='*', label=lbl)
    else :
        plt.scatter(sub['PC1'], sub['PC2'], marker='o', label=lbl)
plt.show()