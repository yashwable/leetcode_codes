class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        if dividend >= 0 and divisor >= 0:
            while dividend >= divisor * (ans+1):
                ans += 1 
        elif dividend >= 0 and divisor < 0:
            while dividend >= divisor * (ans - 1):
                ans -= 1
        elif dividend < 0 and divisor >= 0:
            while dividend <= divisor * (ans - 1):
                ans -= 1
        else :
            while dividend <= divisor * (ans +1):
                ans += 1
        
        return ans 