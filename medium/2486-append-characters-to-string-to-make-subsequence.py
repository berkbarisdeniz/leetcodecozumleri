s = "abde"
t = "abcglkglglkhde"


if t == "":
    print(True)

s_idx = 0
t_idx = 0
s_len = len(s)
t_len = len(t)
while s_idx < s_len and t_idx < t_len :
    if s[s_idx] == t[t_idx] :
        s_idx += 1
        t_idx += 1
    else:
        t_idx += 1
print(s_len - s_idx)
