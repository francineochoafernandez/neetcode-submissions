class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums=len(nums)
        for i in range(len_nums):
            value_i=nums[i]
            for j in range(len_nums):
                if i != j:
                    value_j=nums[j]
                    possible_taget=value_i+value_j
                    if possible_taget==target:
                        return [i,j]