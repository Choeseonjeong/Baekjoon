def solution(n, arr1, arr2):
    answer = []
    for idx in range(n):
        num = bin(arr1[idx] | arr2[idx])
        num = num[2:].zfill(n)
        num = num.replace('1',"#").replace('0'," ")
        answer.append(num)
    return answer