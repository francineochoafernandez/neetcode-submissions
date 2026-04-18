#Bucket sort
#we are using the indexes of an array as de frecuency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict_count=defaultdict(int)
        
        for number in nums:
            dict_count[number]+= 1
        
        # Create buckets where index = frequency
        # frecuency_list[freq] holds all numbers that appear exactly freq times
        # max possible frequency is len(nums), so we need n+1 buckets
        frecuency_list=[[] for i in range(len(nums)+1)]
        for number , freq in dict_count.items():
            frecuency_list[freq].append(number)

        #Read buckets from highest frequency down until we have k elements
        result=[]
        for i in range(len(frecuency_list)-1,0,-1):
            for element in frecuency_list[i]:
                result.append(element)
                if len(result)==k:
                    return result

#Time Complexity 
#O(n) + O(n) + O(n) = O(3n) = O(n)
#Space Complexity 
#O(n) + O(n) + O(n) = O(3n) = O(n)