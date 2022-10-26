class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1 = []
        l = len(nums)
        for i in range(l):
            i1 = nums[i]
            for j in range(i+1,l):
                j1 = nums[j]
                for k in range(j+1,l):
                    k1 = nums[k]
                    if i1 + j1 + k1 == 0 and [i1,j1,k1] not in list1 :
                        list1.append([i1,j1,k1])
        return list1
