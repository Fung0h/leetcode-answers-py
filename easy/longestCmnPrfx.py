class Solution():
    def longestCommonPrefix(self, strs):
        for word in strs:
            if word == "":
                return ""

        output = ""

        for i in range(min(len(s) for s in strs)):
            for word in strs:
                if word[i] != strs[0][i]:
                    if i == 0:
                        return ""
                    return output
            output += strs[0][i]

        return output
  
solution = Solution()
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
