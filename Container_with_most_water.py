class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        left = 0
        right = len(height)-1
        while(left<right):
            area = 0
            if height[left]>height[right]:
                area = height[right]* (right-left)
                right = right-1
            else:
                area = height[left]*(right-left)
                left = left+1

            if area>result:
                result=area
           

        return result
