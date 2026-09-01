#3
# 567.minimum moes to clean the classroomg

from collections import deque


class Solution:
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign bit to every litter
        start = 0
        litter_count = 0
        litter_mask = [0] * (m * n)

        for r in range(m):
            for c in range(n):

                cell = classroom[r][c]

                if cell == 'S':
                    start = r * n + c

                elif cell == 'L':
                    litter_mask[r * n + c] = 1 << litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        masks = 1 << litter_count
        full_mask = masks - 1

        # best[state] = maximum energy seen for
        # (position, collected_mask)
        #
        # bytearray is much faster and smaller than
        # a Python list of integers.
        best = bytearray(m * n * masks)

        start_state = start * masks

        # Store energy + 1 because bytearray cannot store -1
        best[start_state] = energy + 1

        queue = deque([start_state])

        moves = 0

        # Precompute valid neighboring cells
        neighbors = [[] for _ in range(m * n)]

        for r in range(m):
            for c in range(n):

                pos = r * n + c

                if classroom[r][c] == 'X':
                    continue

                if r > 0 and classroom[r - 1][c] != 'X':
                    neighbors[pos].append(pos - n)

                if r + 1 < m and classroom[r + 1][c] != 'X':
                    neighbors[pos].append(pos + n)

                if c > 0 and classroom[r][c - 1] != 'X':
                    neighbors[pos].append(pos - 1)

                if c + 1 < n and classroom[r][c + 1] != 'X':
                    neighbors[pos].append(pos + 1)

        while queue:

            for _ in range(len(queue)):

                state = queue.popleft()

                pos = state // masks
                mask = state % masks

                current_energy = best[state] - 1

                if mask == full_mask:
                    return moves

                if current_energy == 0:
                    continue

                r = pos // n
                c = pos % n

                for nxt in neighbors[pos]:

                    nr = nxt // n
                    nc = nxt % n

                    new_energy = current_energy - 1

                    # Reset
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter
                    new_mask = mask | litter_mask[nxt]

                    new_state = nxt * masks + new_mask

                    # If we have already reached this state
                    # with more energy, don't visit again.
                    if best[new_state] >= new_energy + 1:
                        continue

                    best[new_state] = new_energy + 1

                    queue.append(new_state)

            moves += 1

        return -1