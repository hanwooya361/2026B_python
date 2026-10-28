import numpy as np
np.set_printoptions(suppress=True, precision=2)
data = np.genfromtxt('./경찰청_연도별 사이버 범죄 통계 현황_20251231.csv', delimiter=',', skip_header=1)

year = data[0::2,0]
검거건수 = data[1::2,2:]
발생건수 = data[0::2,2:]
연도별검거 = np.sum(검거건수, axis=1)
연도별발생 = np.sum(발생건수, axis=1)
검거율 = (연도별검거/연도별발생) * 100
검거율낮은년도 = year[np.argmin(검거율)]
print(year[검거율 < 60])

위험범죄 = (발생건수 >= 10000) & (검거건수 <= 3000)
해당년도 = np.sum(위험범죄, axis=1) > 0
print(year[해당년도])

미검거 = np.sum(발생건수-검거건수, axis=0)
정규화 = (미검거 - np.min(미검거)) / (np.max(미검거) - np.min(미검거))
최우선 = 정규화 >= 0.9
print(np.sum(최우선))