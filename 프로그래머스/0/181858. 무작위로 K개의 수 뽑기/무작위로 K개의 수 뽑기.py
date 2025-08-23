def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))

# k len 까지 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식