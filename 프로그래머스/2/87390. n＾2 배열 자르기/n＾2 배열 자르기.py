def solution(n, left, right):
    ans = []
    for k in range(left, right + 1):
        r, c = divmod(k, n)        
        ans.append(max(r, c) + 1)
    return ans
