class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            for i in range(len(nums)):
                num1 = nums[i]
                for j in range(i+1,len(nums)):
                    if num1 == nums[j]:
                        return True
            return False
        else:
            for i in range(len(nums)):
                num1 = nums[i]
                end1 = min(len(nums),i+k+1)
                for j in range(i+1,end1):
                    if num1 == nums[j]:
                        return True
            return False
