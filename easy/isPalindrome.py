class Solution(object):
    def isPalindrome(self, x):
        x = str(x) 
        if x == x[::-1]:
            return True
        else:
            return False

solution = Solution()
x = 101
print(solution.isPalindrome(x))