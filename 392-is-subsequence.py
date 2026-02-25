class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx= 0
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return (True)
        elif s_len > t_len :
            return (False)

        while True:
    
            if s[s_idx] == t[t_idx]:
                if s_idx +1  == s_len:
                    return (True)
                elif t_idx +1 == t_len:
                    return False
                    
                s_idx += 1
                t_idx += 1
            
            
            
        
            elif s[s_idx] != t[t_idx] :
                if t_idx +1 == t_len:
                    return (False)
                
                t_idx += 1    
        
# gereksiz değişkenlerle cok boğuşmuşum 
    
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        if t == "": return False

        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t): 
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else: 
                p2 += 1

        return len(s) == p1

"""