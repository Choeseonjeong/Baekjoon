def solution(brown, yellow):
    ab = brown + yellow
    for b in range(1, ab + 1):  # a,b를 구해야 함
        if (ab % b) == 0:  # ab의 약수
            a = int(ab / b)
            if a >= b:
                if (a - 2) * (b - 2) == yellow:
                    return [a, b]
