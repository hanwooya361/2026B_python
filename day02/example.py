sitmin = 2
sitmax = 10
total = 100
memo = {}

def 문제(남은사람수, 최소사람수) :
    key = str([남은사람수, 최소사람수])
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1
    output = 0
    for i in range(최소사람수, sitmax+1):
        output += 문제(남은사람수-i, i)
    memo[key] = output
    return output
print(문제(total, sitmin))