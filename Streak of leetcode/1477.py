class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        # best[i] = shortest valid subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        current_sum = 0
        answer = INF
        shortest = INF

        for right in range(n):
            current_sum += arr[right]

            # Shrink window if sum is too large
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            # Found a subarray with sum = target
            if current_sum == target:
                length = right - left + 1

                # Need a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                # Keep the shortest valid subarray seen so far
                shortest = min(shortest, length)

            # Store the best answer up to this index
            best[right] = shortest

        if answer == INF:
            return -1

        return answer