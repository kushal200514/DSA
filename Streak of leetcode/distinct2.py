#940-Distinct Subsequnces -2


class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = [1] * (len(s) + 1)
        last = {}

        for i in range(1, len(s) + 1):
            ch = s[i - 1]

            dp[i] = (2 * dp[i - 1]) % MOD

            if ch in last:
                dp[i] -= dp[last[ch] - 1]
                dp[i] %= MOD

            last[ch] = i

        return (dp[len(s)] - 1) % MOD