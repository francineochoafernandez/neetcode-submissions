class Node:
    def __init__(self, val, next_node=None):
        self.data=val
        self.next=next_node

class LinkedList:
    
    def __init__(self):
        self.head=Node(-1)
        self.tail=self.head

    
    def get(self, index: int) -> int:
        #will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
        current_node=self.head.next

        for i in range(index):
            if not current_node:
                return -1
            current_node=current_node.next
        
        if current_node:
            return current_node.data
        else:
            return -1

    def insertHead(self, val: int) -> None:
        #will insert a node with val at the head of the list.
        new_node=Node(val)
        new_node.next=self.head.next
        self.head.next=new_node
        if not new_node.next:
            self.tail= new_node


    def insertTail(self, val: int) -> None:
        #will insert a node with val at the tail of the list.
        new_node=Node(val)
        self.tail.next=new_node
        self.tail=self.tail.next

    def remove(self, index: int) -> bool:
        #will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
        current_node=self.head
        for i in range (index):
            if not current_node:
                return False
            current_node=current_node.next

        if current_node and current_node.next:
            if current_node.next == self.tail:
                self.tail=current_node

            current_node.next=current_node.next.next
            return True
        
        return False
        
    def getValues(self) -> List[int]:
        #return an array of all the values in the linked list, ordered from head to tail.
        current_node= self.head.next
        list_values=[]
        while current_node:
            list_values.append(current_node.data)
            current_node=current_node.next
        return list_values

