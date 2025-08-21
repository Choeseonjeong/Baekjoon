def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        num = int(i[s:s+l])  
        if num > k:
            result.append(num)
    return result



# s번 인덱스에서 시작하는 l길이를 잘라 정수로 변환
# 정수의 값이 k보다 큰 값들을 담은 배열 

