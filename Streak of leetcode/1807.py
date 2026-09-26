class Solution:
    def evaluate(self, s, knowledge):

        # Create dictionary
        know = {}

        for key, value in knowledge:
            know[key] = value

        result = []
        i = 0

        while i < len(s):

            # Normal character
            if s[i] != '(':
                result.append(s[i])
                i += 1

            else:
                # Find closing bracket
                j = i + 1

                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Replace with value or ?
                if key in know:
                    result.append(know[key])
                else:
                    result.append('?')

                # Move after ')'
                i = j + 1

        return ''.join(result)