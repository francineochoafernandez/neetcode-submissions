#Filter spaces, special characters and convert everything to lowercase
#Go through each element from both ends and compare.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not self.isAlphanumeric(s[l]):
                l +=1
            while r>l and not self.isAlphanumeric(s[r]):
                r -=1

            if s[r].lower()!=s[l].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlphanumeric(self, val):
        return( ord("A") <= ord(val) <= ord("Z") or
                ord("a") <= ord(val) <= ord("z") or
                ord("0") <= ord(val) <= ord("9"))