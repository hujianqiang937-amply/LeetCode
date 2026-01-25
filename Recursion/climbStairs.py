def climbStairs(n):
    # if n < 3:
    #     return n
    # start, end = 1, 2
    # for i in range(3, n + 1):
    #     start, end = end, start + end
    # return end

    # 基础动态规划版
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
