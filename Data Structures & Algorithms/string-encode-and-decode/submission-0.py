#We will use a number and a # to map the list of string to a string.
#The number and # will be the incicaotrs of a new word, the number 
#indicates the lenght of the following word.
#Example: strs= ["cat","crazy"], encode=3#cat5#crazy
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string_val in strs:
            encoded_string += str(len(string_val)) + "#" + string_val
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs=[]
        str_position=0

        while str_position < len(s):
            str_pointer=str_position
            while s[str_pointer] != "#":
                str_pointer += 1
            str_lenght = int(s[str_position:str_pointer]) #Not including str_pointer (in is the #)
            #Getting word from char after # 
            strs.append(s[str_pointer+1: str_pointer + 1 + str_lenght])
            str_position=str_pointer + 1 + str_lenght
        return strs