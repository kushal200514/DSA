class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # Each node:
        # [product modulo k, prefix counts]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def make_node(value):
            value %= k

            count = [0] * k
            count[value] = 1

            return [value, count]

        def merge(left, right):
            left_prod, left_count = left
            right_prod, right_count = right

            prod = (left_prod * right_prod) % k

            count = left_count[:]

            for r in range(k):
                new_r = (left_prod * r) % k
                count[new_r] += right_count[r]

            return [prod, count]

        def build(node, l, r):
            if l == r:
                tree[node] = make_node(nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                tree[node] = make_node(value)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Query [start, n-1]
            _, prefix_count = query(
                1, 0, n - 1, start, n - 1
            )

            answer.append(prefix_count[x])

        return answer