def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    aCount, bCount, cCount = 0, 0, 0

    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            aCount += 1
        if b[i % len(b)] == answers[i]:
            bCount += 1
        if c[i % len(c)] == answers[i]:
            cCount += 1

    k = max(aCount, bCount, cCount)
    result = []
    if k == aCount:
        result.append(1)
    if k == bCount:
        result.append(2)
    if k == cCount:
        result.append(3)

    return result