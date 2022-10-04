class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            a = s[i]
            if a == 'M':
                if i != 0 and s[i-1] == 'C':
                    ans += 800
                else :
                    ans += 1000
            elif a == 'D':
                if i != 0 and s[i-1] == 'C':
                    ans += 300
                else :
                    ans += 500
            elif a == 'C':
                if i != 0 and s[i-1] == 'X':
                    ans += 80
                else :
                    ans += 100
            elif a == 'L':
                if i != 0 and s[i-1] == 'X':
                    ans += 30
                else :
                    ans += 50
            elif a == 'X':
                if i != 0 and s[i-1] == 'I':
                    ans += 8
                else :
                    ans += 10
            elif a == 'V':
                if i != 0 and s[i-1] == 'I':
                    ans += 3
                else :
                    ans += 5
            elif a == 'I':
                ans += 1
        return ans
