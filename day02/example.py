앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 100
memo = {}

def 문제(남은사람수, 최소사람수) :
    key = str([남은사람수, 최소사람수])
    if key in memo:
        memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1








print(문제(전체사람의수, 앉힐수있는최소사람수))

numbers= [1, 2, 3, 4, 5, 6]
print("::".join(str(numbers)))