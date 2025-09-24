def solution(absolutes, signs):
    ans = 0
    for num, flag in zip(absolutes, signs):
        if flag == True:
            ans += num
        else:
            ans -= num
    return ans