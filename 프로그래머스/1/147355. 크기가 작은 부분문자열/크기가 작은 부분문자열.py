def solution(t, p):
    arr = []
    answer = 0
    for i in range(len(t)-len(p)+1):
        arr.append(t[i:i+len(p)])
    return len([i for i in arr if i<=p])