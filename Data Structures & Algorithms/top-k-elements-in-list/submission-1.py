#Bucket sort
#we are using the indexes of an array as de frecuency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuency_list=[[] for i in range(len(nums)+1)]
        dict_count=defaultdict(int)
        
        for number in nums:
            dict_count[number]+= 1
        
        for number , freq in dict_count.items():
            frecuency_list[freq].append(number)

        result=[]
        for i in range(len(frecuency_list)-1,0,-1):
            for element in frecuency_list[i]:
                result.append(element)
                if len(result)==k:
                    return result