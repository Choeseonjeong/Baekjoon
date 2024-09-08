def solution(arr, n, v):
    count = 0
    for i in range(arr + 1):
        if v in n:
            count += 1
    return count


arr = int(input())
n = map(int, input().split(" "))
v = int(input())

print(solution(arr, n, v))
