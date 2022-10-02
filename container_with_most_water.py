class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = len(height)
        for i in range(l):
            bar = height[i]
            if (bar * (l-(i+1)) > area ):
                space = 1
                for j in range(i+1,l):
                    area1 = 0
                    if (bar > height[j]):
                        area1 = space * height[j]
                    else:
                        area1 = space * bar
                    if (area1 > area) : 
                        area = area1
                    space += 1
                space = 1
            
        return area
