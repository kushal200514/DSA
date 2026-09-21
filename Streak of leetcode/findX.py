class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        answer = [0] * k

        for num in nums:
            num %= k

            new_dp = [0] * k

            # Start a new subarray with num
            new_dp[num] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_r = (r * num) % k
                new_dp[new_r] += dp[r]

            dp = new_dp

            # Add subarrays ending here to the answer
            for r in range(k):
                answer[r] += dp[r]

        return answer