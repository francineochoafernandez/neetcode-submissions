class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams=defaultdict(list)
        for word in strs:
            key_word_array=[0]*26
            for char in  word:
                key_word_array[ord(char)-ord("a")]+=1
            
            map_anagrams[tuple(key_word_array)].append(word)
        print(map_anagrams)
        return list(map_anagrams.values())