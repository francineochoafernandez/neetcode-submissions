# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current= None, head

        while current:
            next_node=current.next #save next of current node for later use
            current.next= previous #We are reverting, the next of current should be the previous
            #Now for the following iterations:
            previous= current #move the previous forward 
            current= next_node  #move the current forward (the next value saved initially)
        return previous #We move forward untill there is no more current.
        #That means: next_node in the last iteration, did not exist, meaning, we reached the end/new head

            