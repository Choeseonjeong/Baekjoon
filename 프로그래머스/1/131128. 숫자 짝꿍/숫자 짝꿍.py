from collections import Counter

def solution(x,y):
    result = []
    countX = Counter(x)
    countY = Counter(y)
    for i in range(10):
        i_str = str(i)
        if i_str in countX and i_str in countY:
            num = min(countX[i_str],countY[i_str])
            result.extend(num*[i_str])
    result.sort(reverse=True)
    if not result:
        return '-1'
    if result[0]=='0':
        return '0'
    return ''.join(result)
            