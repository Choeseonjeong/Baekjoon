def solution(n, x, arr):
    a = []
    for i in arr:
        if i < x:
            a.append(str(i))
    return " ".join(a)


n, x = map(int, input().split(" "))
arr = map(int, input().split(" "))


print(solution(n, x, arr))
