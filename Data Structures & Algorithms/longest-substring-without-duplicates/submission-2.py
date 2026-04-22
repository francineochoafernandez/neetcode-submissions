#Sliding window from left to right
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars=set()
        left=0
        result=0

        for right in range(len(s)): # right keeps moving forward 
            # before adding the char in position right to the unique_chars, 
            #we check if it exists already in unique_chars
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
                #if it does exists, we remove elements from the left side 
                #until we remove the value s[right]

            #After that, we can safely add the s[right] to the unique_chars
            unique_chars.add(s[right])
            #Every time we go forward to the right we get the max of the window 
            #with unique characters (the +1 is because of the array index starting from 0)
            result=max(result,right-left +1)
        return result

#Time complexity: O(n) where n is the length of the string
#Space complexity: O(m) where m is the total number of unique characters in the string