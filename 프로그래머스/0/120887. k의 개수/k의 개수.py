def solution(i, j, k):
    answer = 0
    arr = [str(num) for num in range(i,j+1)]
    for word in arr:
        for n in word:
            if n == str(k):
                answer+=1
    return answer