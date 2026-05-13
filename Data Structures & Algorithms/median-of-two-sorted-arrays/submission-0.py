# Given 2 arrays A and B. If A is the smallest, we will run binary search only in that one.
# We will partition both arrays by half, first A with binary search
#Left half:  [...A_left,  ...B_left ]   → total//2 elements
#Right half: [ A_right,    B_right, ...]→ total//2 + 1 elements
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B =nums1, nums2
        total_len= len(A)+len(B)
        total_half = total_len // 2

        #Forcing A to be the smallest array
        if len(A) > len(B):
            A, B =B, A
        
        #Binary search on array A, the shortest array
        left, right= 0, len(A)-1

        while True:

            middle_A=(left+right) // 2
            #Get middle of array B given the middle of A
            middle_B= (total_half-middle_A) -2 #subtracting 2 because of array indexing  total_half = (middle_A + 1) + (middle_B + 1)

            # Last element of left partition of array A
            A_left= A[middle_A] if middle_A >=0 else float("-infinity")
            # First element of right partition of array A
            A_right= A[middle_A+1] if middle_A+1 < len(A) else float("infinity")

            # Last element of left partition of array B
            B_left= B[middle_B] if middle_B >=0 else float("-infinity")
            # First element of right partition of array B
            B_right= B[middle_B+1] if middle_B+1 < len(B) else float("infinity")

            #Check if partition is correct
            if A_left<= B_right and B_left<=A_right:
                # Odd value or total_len
                if total_len % 2:
                    return min(A_right,B_right) #When odd, right half has exactly one more element than the left half, because of  total_half = total_len // 2
                #Even
                else:
                    return ( max(A_left,B_left) + min(A_right,B_right) ) / 2
            
            elif A_left > B_right:
                right= middle_A-1 #A gave too much to left  →  move A's partition LEFT
            else:
                left= middle_A+1 #B_left > A_right  →  B gave too much to left  →  move A's partition RIGHT

        