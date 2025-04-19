romans = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

class Solution(object):
    def romanToInt(self, s):
        acc = 0
        s = str(s)

        for i in range(len(s)):
            if i == (len(s)-1):
                acc += romans.get(s[i])
                break
            if (s[i] == "V" or s[i] == "L" or s[i] == "D" or s[i] == "M"): 
                acc += romans.get(s[i])
            else:
                if(s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")):
                    acc -= 1
                elif(s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")):
                    acc -= 10
                elif(s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                    acc -= 100
                else:
                    if(s[i] == "I"):
                        acc += 1
                    if(s[i] == "X"):
                        acc += 10                        
                    if(s[i] == "C"):
                        acc += 100
        return acc

solution = Solution()
number = "MCMXCIV"
print(solution.romanToInt(number))