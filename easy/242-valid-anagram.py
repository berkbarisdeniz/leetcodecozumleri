class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t) :
            return False
        else:
            s_d = dict()
            t_d = dict()
            for k in s:
                s_d[k] = s_d.get(k,0)+1
            for k in t:
                t_d[k] = t_d.get(k,0)+1
            return s_d == t_d