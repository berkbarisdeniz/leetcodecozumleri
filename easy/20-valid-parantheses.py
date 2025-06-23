def isValid(s):
  stack = []
  my_dict ={')':'(',
            '}':'{',
            ']':'['
            }
  for bracket in s:
    if bracket in my_dict and len(stack)!=0 :
      if my_dict[bracket] != stack[-1]:
        return False
      else:
        stack.pop()
        continue
    stack.append(bracket)
  if len(stack) == 0 :
    return True
  else : return False