class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        if num >= 1000:
            n = num//1000
            ans += n*"M"
            num -= n*1000

        if num >= 900:
            ans += "CM"
            num -= 900
        elif num >= 500:
            n = num//100 - 5
            ans += "D" + n*"C"
            num -= 500 + n*100
        elif num >= 400:
            ans += "CD"
            num -= 400
        elif num >= 100:
            n = num // 100
            ans += n*"C"
            num -= n*100
            
        if num >= 90:
            ans += "XC"
            num -= 90
        elif num >= 50:
            n = num//10 - 5
            ans += "L" + n*"X"
            num -= 50 + n*10
        elif num >= 40:
            ans += "XL"
            num -= 40
        elif num >= 10:
            n = num // 10
            ans += n*"X"
            num -= n*10
            
        if num >= 9:
            ans += "IX"
            num -= 9
        elif num >= 5:
            n = num - 5
            ans += "V" + n*"I"
            num -= 5 + n
        elif num >= 4:
            ans += "IV"
            num -= 4
        elif num >= 1:
            ans += num*"I"
            num -= num*1
        return ans

        
