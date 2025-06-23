def solution(s):
    cntzero = 0
    cntnum = 0
    while True:
        if s == '1':
            break
        cntzero+=s.count("0")
        s = s.replace("0","")
        cntnum+=1
        length = len(s)
        s = bin(length)[2:]
    return [cntnum,cntzero]