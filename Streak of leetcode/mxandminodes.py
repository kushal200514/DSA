#2059 _find the maximum and minimum number of nodes bet ween critical points


class Solution:
    def nodesBetweenCriticalPoints(self, head):

        # Need at least 3 nodes to have a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next
        position = 1

        first = -1
        last = -1
        min_distance = float('inf')

        while curr.next is not None:

            # Check if current node is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                # First critical point
                if first == -1:
                    first = position

                # We already found a previous critical point
                else:
                    distance = position - last
                    min_distance = min(min_distance, distance)

                # Update last critical point
                last = position

            prev = curr
            curr = curr.next
            position += 1

        # Fewer than two critical points
        if first == last:
            return [-1, -1]

        max_distance = last - first

        return [min_distance, max_distance]