# We will use the same output array to save the product of every value to the left
# we will use pretfix to save the last product of every value to the left
# Then we will use postfix to save the last product of every value to the right
# Then we use the same output (that already has the products to the left) to multiply it
# with each postfix (with the products to the right.)

#Pass 1 → output[i] = product of everything LEFT  of i
#Pass 2 → output[i] = output[i] × product of everything RIGHT of i
# two running variables prefix and postfix are just the memory of what we've multiplied 
#so far as we walk in each direction 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums=len(nums)
        output=[1]*len_nums

        prefix=1
        for index in range(len_nums):
            output[index] = prefix
            prefix *= nums[index] #memory of what was multiplied lo the left, each time we go forward (to the right)

        postfix=1

        for index in range(len_nums-1,-1,-1):
             output[index] *= postfix #multiply results of products to the left with postfix (products to the right)
             postfix *= nums[index] #memory of what was multiplied lo the right, each time we go back (to the left)

        return output