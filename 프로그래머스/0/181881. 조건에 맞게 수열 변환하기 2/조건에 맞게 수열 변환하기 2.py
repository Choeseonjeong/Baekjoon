def solution(arr):
    count = 0
    while True:
        ex = arr[:]
        for n in range(len(arr)):
            if arr[n] >= 50 and arr[n]%2==0:
                arr[n] //= 2
            elif arr[n] < 50 and arr[n] % 2 == 1:
                arr[n] = arr[n] * 2 + 1
        count += 1
        if ex == arr:
            return count - 1