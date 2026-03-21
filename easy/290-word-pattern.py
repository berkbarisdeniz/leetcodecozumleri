class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mlist =s.split(" ")
        hm= {}
        seen = set()
        if len(mlist) != len(pattern):
            return False
        for i in range(len(mlist)):
            if pattern[i] not in hm:
                hm[pattern[i]]=mlist[i]
                if mlist[i] in seen:
                    return False
                seen.add(mlist[i])
                
            elif hm[pattern[i]] != mlist[i]:
                return False  
        return True
                

"""keske uzunlukların esit olacağını yazsalar bi saat ne alaka diye ekrana baktık"""