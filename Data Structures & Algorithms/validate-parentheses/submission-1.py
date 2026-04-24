#Stack
#A closing paranthesis always has to match the closest opening parentheses.
#Hash map to map closing to open parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open={")":"(","}":"{","]":"["}
        stack_parentheses= []

        for element in s:
            if element not in close_to_open: #If it is an open parentheses
                stack_parentheses.append(element)
            else:#Case for closed parentheses
                #If is not empty (can't start with closed parentheses) and if 
                #last element added to the stack is exactly the corresponding open version
                # of the closing parentheses we have in the element.
                if stack_parentheses and stack_parentheses[-1]==close_to_open[element]:
                    stack_parentheses.pop()
                else:
                    return False #We would know immediately that it doesnt work
            
        if  not stack_parentheses:#if the stack is empty
            return True
        else:
            return False
                
                 