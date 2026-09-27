class Solution:
    def reverseParentheses(self, s):

        stack = []
        current = ""

        for ch in s:

            if ch == '(':
                # Save the string before '('
                stack.append(current)

                # Start a new string
                current = ""

            elif ch == ')':
                # Reverse the current inner string
                current = current[::-1]

                # Add it to the previous string
                previous = stack.pop()

                current = previous + current

            else:
                current += ch

        return current