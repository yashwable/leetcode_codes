class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        int1 = 0 
        int2 = 0 
        nums3 = []

        while int1 != len(nums1) and int2 != len(nums2) :
            if nums1[int1] <= nums2[int2] :
                nums3.append(nums1[int1])
                int1 += 1
            else :
                nums3.append(nums2[int2])
                int2 += 1
        if int1 == len(nums1) :
            nums3.extend(nums2[int2:])
        else :
            nums3.extend(nums1[int1:])
        l = len(nums3)  
        if l%2 == 0 :
            return (nums3[l//2 -1] + nums3[l//2]) /2
        else :
            return nums3[l//2]
