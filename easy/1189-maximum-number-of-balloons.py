class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        result = []
        target_hm = {}
        hm = {}
        for letter in target:
            target_hm[letter] = target_hm.get(letter,0)+1
        for letter in text:
            if letter in target:
                hm[letter] = hm.get(letter,0)+1
        for k in target_hm:
            if k not in hm:
                return 0
        for i in target:
            ratio = hm[i]/target_hm[i]
            result.append(ratio)

        return(int(min(result)))
    
    """tek satırda extend counter da kullanılır ama anlaşılır olan bu hem aynı hızda yani :)"""