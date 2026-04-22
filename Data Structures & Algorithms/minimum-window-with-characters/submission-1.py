#Substring of s can include more characters than t, 
#as long as is the minimum,
#but must include all characters in t
#Expand right until the window is valid
#Shrink left as much as possible while still valid
#Record the smallest valid window seen

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        countT={} #Count needed chars from t 
        for c in t: #Initialize countT with values of t
            countT[c]= countT.get(c,0) +1

        window={} #Current window char counts
        have=0 # how many unique chars we've currently satisfied
        need=len(countT)  # how many UNIQUE chars we need to fully satisfy
        result = [-1, -1] # Window indexes
        result_len = float("infinity") #Len of best window.
        left=0

        for right in range(len(s)): #Moving right pointer
            window[s[right]]= window.get(s[right],0) +1 #Add it to the window with the count

            if s[right] in countT and window[s[right]]==countT[s[right]]:
                have +=1
            
            #The window is a valid answer (not necessarily the best). 
            #Every character in t appears in the window at least as many times as required.
            #Once we have what we need we can start the shrinking 
            while have==need: 
                
                if right-left +1 < result_len: #If current window is less than last result, update it
                    result=[left,right]
                    result_len = right-left +1

                #Remove the leftmost character from the window count. We haven't moved left yet — just reduced that character's count
                window[s[left]] -= 1

                #Did removing that character break a satisfied requirement?
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have -=1 #if The character s[left] is one we need and Its count in the window just dropped below what's required
                            #this would exit the while loop
                
                left +=1 #move the left pointer forward.
                #every time we remove a non-required character from the left, the window stays valid and can be shrunk again. 
                #The while keeps squeezing until it can't anymore.

        left, right = result

        if result_len!= float("infinity"):
            return s[left : right+1]
        else:
            return ""




    #Time complexity: O(n+m)
    #Space complexity: O(m)

    #Where n is the length of the string s and m is the total number of unique characters in the strings t and s. 


