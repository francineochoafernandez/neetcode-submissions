class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_m=len(t)
        if  len_s==len_m:
            dict_s={}
            dict_t={}
            for char in s:
                dict_s[char]=dict_s.get(char,0)+1
            
            for char in t:
                dict_t[char]=dict_t.get(char,0)+1
            
            if dict_s==dict_t:
                return True
            else:
                return False
        else:
            return False
        