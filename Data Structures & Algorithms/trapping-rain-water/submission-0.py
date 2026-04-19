#To know how much water we need to trap in index i
#we need to know the max height to the left and to the right
#then we need the minimum of those 2 max values
#result += min(max(L),max(R))- height[i])
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        l, r = 0 , len(height)-1
        leftMax= height[l]
        rightMax= height[r]
        result=0

        while l < r:

            if leftMax < rightMax: 
                #I don't need to know the overall rightMax
                #I already know that current rightMax is bigger 
                #than my current leftMax. That covers min(max(L),max(R)).
                # If the process enters this loop it means min(max(L),max(R)) = max(L)
                #If the current value of rightMax is the actual overall Max to the right, 
                #great that covers it, but if the value of rightMax is less than the actual 
                #overall Max to the right, that would also cover it!
                l += 1
                leftMax=max(leftMax,height[l])
                #After the previous line we know the new value of 
                # leftMax>=height[l] always.
                # So the next line will always sum positive numbers.
                result += leftMax - height[l]
                #I update leftMax with height[l] because the current bar might be taller than 
                #the previous left wall — making it the new left wall. The update ensures I 
                #never add negative water and that future positions use the correct tallest-left-bar seen so far.
            else:
                r -= 1
                rightMax= max(rightMax, height[r])
                result += rightMax - height[r]
                
        return result