s = "{[][]}[(])]"
stack = []
def asdsad(s):
    vhash = {"}":"{",")":"(","]":"["}
    for v in s:
        if v in vhash:
            stack.append(vhash[v])
            print(v)
            print(stack)
        else:
            if v == vhash[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
    

print(asdsad(s))              