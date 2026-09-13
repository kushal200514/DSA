class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        answer = 0

        # Try every possible row shift
        for dr in range(-n + 1, n):

            # Try every possible column shift
            for dc in range(-n + 1, n):

                overlap = 0

                # Check every cell
                for r in range(n):
                    for c in range(n):

                        # Position in img1 after translation
                        nr = r + dr
                        nc = c + dc

                        # Make sure translated position is inside matrix
                        if 0 <= nr < n and 0 <= nc < n:

                            if img1[r][c] == 1 and img2[nr][nc] == 1:
                                overlap += 1

                answer = max(answer, overlap)

        return answer