class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums=len(nums)
        output=[1]*len_nums

        prefix=1
        for index in range(len_nums):
            output[index] = prefix
            prefix *= nums[index]

        postfix=1

        for index in range(len_nums-1,-1,-1):
             output[index] *= postfix
             postfix *= nums[index]

        return output