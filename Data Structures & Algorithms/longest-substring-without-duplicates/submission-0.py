class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars=set()
        left=0
        result=0

        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            
            unique_chars.add(s[right])
            result=max(result,right-left +1)
        return result