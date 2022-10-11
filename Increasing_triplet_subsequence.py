class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = nums[0]
        num2 = 'a'
        for i in nums :
            if i <= num1:
                num1 = i 
            elif num2 == 'a':
                num2 = i 
            elif i <= num2:
                num2 = i 
            else:
                return True
        else :
            return False
            
