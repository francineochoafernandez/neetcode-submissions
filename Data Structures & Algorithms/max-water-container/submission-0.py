#The container is 2D
#Chose 2 bars
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area=0

        while left<right:
            area=(right-left) * min(heights[left],heights[right])
            max_area= max(max_area,area)

            if heights[left] < heights[right]:
                left +=1
            else:
                #For case: heights[left] > heights[right]
                #Also for case heights[left] == heights[right] (if they are equal if doesn't matter wich way to go)
                right -=1
        return max_area