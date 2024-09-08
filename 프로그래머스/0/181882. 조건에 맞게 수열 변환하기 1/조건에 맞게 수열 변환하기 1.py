def solution(arr):
    n = []
    for i in arr:
        if int(i) >= 50 and int(i) % 2 == 0:
            n.append(i / 2)
        elif int(i) < 50 and int(i) % 2 != 0:
            n.append(i * 2)
        else:
            n.append(i)
    return n
