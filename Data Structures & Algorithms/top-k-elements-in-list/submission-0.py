class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count=defaultdict(int)
        for number in nums:
            dict_count[number]+= 1
        
        result=[]
        for _ in range(k):
            max_key = max(dict_count, key=dict_count.get)
            max_value = dict_count[max_key]
            result.append(max_key)
            dict_count.pop(max_key, None)

        return result