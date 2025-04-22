class Solution(object):
    def isValid(self, s):

        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in parentheses.keys():
                stack.append(char)
            elif char in parentheses.values():
                if stack and (parentheses.get(stack[-1]) == char):
                    stack.pop()
                else:
                    return False
        return not stack

solution = Solution()
print(solution.isValid("([])"))