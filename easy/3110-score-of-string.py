class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for letter in range(len(s)-1):
            sum=abs(ord(s[letter])-ord(s[letter+1]))
            score += sum
        return score
        