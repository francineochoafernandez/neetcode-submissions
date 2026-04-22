#Substring of s can include more characters than t, 
#as long as is the minimum,
#but must include all characters in t

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        countT={} #Count needed chars from t 
        for c in t: #Initialize countT with values of t
            countT[c]= countT.get(c,0) +1

        window={} #Current window char counts
        have=0 #Chars that meet the required count
        need=len(countT) #Amount of unique characters we need to match.
        result = [-1, -1] # Window indexes
        result_len = float("infinity") #Len of best window.
        left=0

        for right in range(len(s)): #Moving right pointer
            window[s[right]]= window.get(s[right],0) +1 #Add it to the window with the count

            if s[right] in countT and window[s[right]]==countT[s[right]]:
                have +=1
            
            while have==need: #The window is a valid answer (not necessarily the best)
                
                if right-left +1 < result_len: #If current window is less than last result, update it
                    result=[left,right]
                    result_len = right-left +1

                #shrink from the left of the window
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have -=1
                
                left +=1

        left, right = result

        if result_len!= float("infinity"):
            return s[left : right+1]
        else:
            return ""






