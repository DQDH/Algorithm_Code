def minnum(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for x in range(n + 1)]

    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0:
                dp[0][j] = j
            elif j == 0:
                dp[i][0] = i
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j])
    return dp[n][m]


s1 = input()
s2 = input()
print(minnum(s1, s2))