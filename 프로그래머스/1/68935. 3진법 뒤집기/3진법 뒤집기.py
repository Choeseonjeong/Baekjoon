def solution(n):
    arr = ''
    while n>0:
        num,numBin = divmod(n,3)
        arr += str(numBin)
        n = num
        result = int(arr,3)
    return result
