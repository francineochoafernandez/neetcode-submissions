# Koko needs to eat all the bananas in the piles in less or equal hours
# than the value h. With a rate k of bananas/hour
# As a brute force we could test all possible values of k
# posible values of k : 1 2 .... max(piles) 
# Optimizing it, we could do a "binary search" of the posible values of k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles=max(piles)
        left, right= 1, max_piles
        result= max_piles

        while left<=right:

            k_middle=(left+right)//2
            hours_taken=0
            for pile in piles:
                hours_taken += math.ceil(pile/k_middle)

            # If hours_taken with k_middle value, is less or equal than what we need
            # that is great! Save it as a result if it is a minimum compared with
            # previous value. But we can keep looking for a hours_taken value that is 
            # smaller, that is why we reduce from the right. 
            if hours_taken<=h: 
                right=k_middle-1
                result=min(result,k_middle)
            # If hours_taken with k_middle value, is greater than what we need,
            # that means we need a bigger k_middle value, so let's adavance the
            # left pointer forward.
            elif hours_taken>h: 
                left=k_middle+1

        return result
        
#Time complexity: O(n∗log⁡m) where m is max_piles and n the len(piles)
#Space complexity: O(1)