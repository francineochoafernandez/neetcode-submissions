#The array being rotated sums up to having 2 sorted arrays in 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1

        while left<=right:

            middle=(left+right)//2

            if target==nums[middle]:
                return middle
            
            #Given the idea of having 2 sorted arrays in one

            # Lets check the "left" array. If the left-most value is 
            # less than the middle we are currently at, it means we are
            # on the "left" sorted array.
            if nums[left] <= nums[middle]:
                #Lets check if target is inside this left array
                if target < nums[left] or target >nums[middle]:
                    #Target is not inside left array,  we no longer need to check left
                    left=middle+1
                else:
                    #Target is inside left array, we no longer need to check right
                    right=middle-1
            else: #This would be the "right" array
                #Lets check if target is inside this "right" array
                if target < nums[middle] or target >nums[right]:
                    #Target is not inside right array,  we no longer need to check right
                    right=middle-1
                else:
                    #Target is inside right array, we no longer need to check left
                    left=middle+1
        return -1
                    