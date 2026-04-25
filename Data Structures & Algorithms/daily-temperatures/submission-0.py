#We are going to use a monotonic decreasing stack
#What we add to the stack will be always in decreasing order
# As soon as we find a greater value than the one at the top of the stack,
# we start removing the values from the stack and calculating until stack is empty 
# or the value is no longer greater that the top.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] #We will add pairs of [temperature , index]
        
        for index, temp_value in enumerate(temperatures):
            # While stack is not empty and
            # the current temp_value is greater than the
            # temperature at the top of the stack 
            # we will pop value from stack.
            while stack and temp_value>stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                # Calculate result for stack_index
                # index indicates day where we found a greater value than 
                # the value at stack_index
                result[stack_index] = index - stack_index #stack_index<index always because if it was on the stack means we already passed it 
            #We don't add values to the stack that are greater than the previous
            stack.append([temp_value, index])
        return result