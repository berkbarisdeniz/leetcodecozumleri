class Solution(object):
    def stringMatching(self, words):
        words = sorted(words, key=len)
        results = []
        for i,word in enumerate(words):
            for m in range(i+1,len(words)):
                if word in words[m]:
                    results.append(word)
                    break
        return results