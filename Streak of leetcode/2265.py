# Definition for a binary tree node.
class Solution:
    def averageOfSubtree(self, root):

        self.answer = 0

        def dfs(node):
            if node is None:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Calculate current subtree's sum and count
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            # Calculate average
            average = total_sum // total_count

            # Check if node value equals average
            if node.val == average:
                self.answer += 1

            return total_sum, total_count

        dfs(root)

        return self.answer