class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols= len(matrix), len(matrix[0])

        #First let's check in what row would we find the target
        top, bottom= 0, rows-1
        while top <= bottom:
            mid_row=(top+bottom)//2
            #If target is greater than the last element of the current row
            if target > matrix[mid_row][-1]:
                top=mid_row+1 #Target would be bellow the current row so we lower the top
            #If target is less than the first element of the current row
            elif target < matrix[mid_row][0]:
                bottom=mid_row-1 #Target would be above the current row so we up the bottom
            else:
                break #Target fits IN this current row: stop immediately
                #top and bottom are pointing at the row we need
        
        #Catches the case where the target doesn't belong in any row 
        if not (top <= bottom):
            return False

        #Now that we know in which row to look for
        row=(top+bottom)//2

        #We can do binary search again in that specific row
        left, right= 0 , cols-1

        while left <= right:
            middle= (left+right)//2
            if target > matrix[row][middle]:
                left=middle+1
            elif target < matrix[row][middle]:
                right=middle-1
            else:
                return True

        return False


#Time complexity: O(log⁡m+log⁡n)=O(log⁡(m∗n)) Where m is the number of rows and n is the number of columns of matrix.
#Space complexity: O(1)