def solution(n):
    nnum = bin(n)[2:].count("1")
    exn = n+1
    while True:
        if bin(exn)[2:].count("1") == bin(n)[2:].count("1"):
            break
        else:
            exn+=1
    return exn
        