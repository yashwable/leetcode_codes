class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = min(strs,key = len)
        ans = ""
        
        for i in range (len(minstr)):
            iscontain = False
            for j in strs :
                if minstr[i] == j[i]:
                    iscontain = True
                else : 
                    iscontain = False
                    break
            if iscontain == True:
                ans += minstr[i]
            else:
                return ans
        return ans
