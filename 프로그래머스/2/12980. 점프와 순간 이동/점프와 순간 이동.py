def solution(n):
    ans = 0
    bin_n = bin(n)[2:]
    return bin_n.count("1")