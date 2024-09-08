def solution(n):
    k = bin(n)
    KC = k.count("1")
    a = []
    while True:
        n += 1
        h = bin(n)
        HC = h.count("1")
        if KC == HC:
            break

    return int(h, 2)