class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_previous_vals={}

        for index, value in enumerate(nums):
            difference=target-value
            if difference in map_previous_vals:
                return [map_previous_vals[difference],index]
            else:
                map_previous_vals[value]=index
                
