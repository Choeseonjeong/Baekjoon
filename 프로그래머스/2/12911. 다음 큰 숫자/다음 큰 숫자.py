def solution(n):
    num = n+1
    while True:
        num_s = bin(num)[2:]
        n_s = bin(n)[2:]
        if num_s.count("1") == n_s.count("1"):
            return num
        else:
            num+=1