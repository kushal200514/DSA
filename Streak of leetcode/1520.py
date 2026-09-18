class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Create valid intervals
        for c in range(26):
            if first[c] == n:
                continue

            start = first[c]
            end = last[c]
            i = start
            valid = True

            while i <= end:
                idx = ord(s[i]) - ord('a')

                # Character occurs before our interval
                if first[idx] < start:
                    valid = False
                    break

                end = max(end, last[idx])
                i += 1

            if valid:
                intervals.append((start, end))

        # Greedy: choose earliest finishing intervals
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result