class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s 
        ans = ""
        n = 2*(numRows-1)
        for i in range(numRows):
            for j in range(len(s)):
                if (j + i) % n == 0 or (j - i) % n == 0 :
                    ans += s[j]
        return ans
            
