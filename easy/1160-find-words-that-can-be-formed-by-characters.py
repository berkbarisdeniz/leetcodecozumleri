from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        target = Counter(chars)
        total = 0
        for word in words:
            check = True
            inp = Counter(word)
            for i in inp:
                if inp[i] > target[i]:
                    check = False
                    break
            if check :
                total += len(word)

        return total 