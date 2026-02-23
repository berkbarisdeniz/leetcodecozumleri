class Solution(object):
    def longestCommonPrefix(self, strs): 
        prefix = strs[0]
        for word in strs[1:len(strs):]:
            temp_prefix = ""
            for char1, char2 in zip(word,prefix):
                if char1 == char2 :
                    temp_prefix += char1
                else:
                    break
            prefix=temp_prefix
        return prefix 


