from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add original index
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # dp[i][k] = best answer starting from i
        # when we can still choose k intervals.
        #
        # Since k <= 4, use 5 arrays.
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, original_index = arr[i]

            # First interval whose start > r
            next_i = bisect_right(starts, r)

            for k in range(1, 5):

                # Option 1: skip this interval
                skip_score, skip_indices = dp[i + 1][k]

                # Option 2: take this interval
                take_score, take_indices = dp[next_i][k - 1]

                take_score += w
                take_indices = tuple(sorted(
                    (original_index,) + take_indices
                ))

                # Pick better score
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)

                else:
                    # Same score -> lexicographically smaller
                    dp[i][k] = (
                        take_score,
                        min(take_indices, skip_indices)
                    )

        return list(dp[0][4][1])