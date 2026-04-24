class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        start = sentence[0]
        end = sentence[-1]
        for k in range(len(sentence)):
            if sentence[k] == " " and sentence[k+1] != sentence[k-1]:
                return False
        return start == end
        