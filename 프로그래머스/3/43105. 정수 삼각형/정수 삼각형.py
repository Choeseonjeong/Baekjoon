def solution(triangle):
    dp = triangle
    ldp = len(triangle)
    
    answer = 0
    
    for i in range(1,ldp):
        for j in range(i+1):
            if (j==0):
                dp[i][j] += dp[i-1][j]
            elif (i==j):
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
    return max(dp[ldp-1])