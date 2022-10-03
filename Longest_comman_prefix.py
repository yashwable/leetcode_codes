class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr = min(strs,key = len)
        ans = ""
        for i in minstr:
            iscontain = False
            for j in strs:
                if i in j:
                    iscontain = True
                else: 
                    iscontain = False
                    break
            if iscontain == True:
                ans += i
            else :
                return ans
        return ans
