class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]
        
        # 0 segments = 1 way
        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, k + 1):
                # Don't end a segment at i
                dp[i][j] = dp[i - 1][j]

                # Choose the starting point of the last segment
                for start in range(i):
                    dp[i][j] += dp[start][j - 1]
                    dp[i][j] %= MOD

        return dp[n - 1][k]