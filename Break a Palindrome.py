class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        else:
            ans = ""
            for i in range(len(palindrome)):
                if (ord(palindrome[i]) != 97):
                    ans += chr(ord(palindrome[i]) - 1) + palindrome[i+1:]
                    return ans
                    break
                else:
                    ans += palindrome[i]
            else:
                return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)            
