def solution(n):
    if int(n**0.5)==n**0.5:
        return int(n**0.5+1)*int(n**0.5+1)
    return -1