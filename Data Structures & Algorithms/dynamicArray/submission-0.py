class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity


    def get(self, i: int) -> int:
        #will return the element at index i. Assume that index i is valid.
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        # will set the element at index i to n. Assume that index i is valid.
        self.array[i]=n

    def pushback(self, n: int) -> None:
        #will push the element n to the end of the array.
        #If we call void pushback(int n) but the array is full, we should resize the array first.
        if self.size == self.capacity:
            self.resize()

        self.array[self.size]=n
        self.size=self.size+1
            
    def popback(self) -> int:
        #will pop and return the element at the end of the array. Assume that the array is non-empty.
        
        self.size=self.size-1
        end_element=self.array[self.size]
        return end_element

    def resize(self) -> None:
        #will double the capacity of the array.
        self.capacity = self.capacity * 2
        new_double_array = [0] * self.capacity
        for i in range(0,self.size):
            new_double_array[i]= self.array[i]
        self.array=new_double_array
        


    def getSize(self) -> int:
        #will return the number of elements in the array.
        return self.size
    
    def getCapacity(self) -> int:
        #will return the capacity of the array.
        return self.capacity
