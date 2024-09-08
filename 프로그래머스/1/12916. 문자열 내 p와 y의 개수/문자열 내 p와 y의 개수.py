def solution(s):
    Pcount = 0
    Ycount = 0
    for i in s:
        if i == "p" or i == "P":
            Pcount += 1
        elif i == "y" or i == "Y":
            Ycount += 1
    if Pcount == Ycount:
        return True
    else:
        return False
