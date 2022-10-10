class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ""
        for i in range(len(palindrome)):
            if (ord(palindrome[i]) != 97):
                ans += chr(ord(palindrome[i]) - 1) + palindrome[i+1:]
                return ans
                break
            else :
                ans += palindrome[i] 
        return ""
            
