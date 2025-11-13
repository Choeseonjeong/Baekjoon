def solution(polynomial):
    arr = [i.strip() for i in polynomial.split("+")]
    xnum = 0
    num = 0
    for n in arr:
        if n[-1] == 'x':
            if n == 'x':
                xnum += 1
            else:
                xnum += int(n[:-1])
        else:
            num += int(n)
    
    if num != 0 and xnum != 0:
        if xnum == 1:
            return "x + " + str(num)
        else:
            return str(xnum) + "x + " + str(num)
    elif xnum == 0:
        return str(num)
    else:
        return "x" if xnum == 1 else str(xnum) + "x"
