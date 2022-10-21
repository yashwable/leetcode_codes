class Solution:
    def isPalindrome(self,s : str) -> bool:
        n = len(s) // 2 
        ans = True
        for i in range(0,n):
            if s[i] != s[-(i+1)]:
                ans = False
                break
        return ans 

    def palindome_series(self, i,e,s):
        if e+2 <= len(s) and Solution().isPalindrome(s[i:e+2]) :
            return Solution().palindome_series(i,e+1,s)
        elif i-2>=-1 and e+2 <= len(s) and Solution().isPalindrome(s[i-1 : e+2]):
            return Solution().palindome_series(i-1,e+1,s)
        else:
            return s[i:e+1]

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = len(s)
        palindrome = ""
        for i in range(0,len(s)):
            str = Solution().palindome_series(i,i,s)
            if len(str) > len(palindrome):
                palindrome = str
                print(i)
        return palindrome
