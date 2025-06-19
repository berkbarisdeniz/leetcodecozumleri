def evalRPN(tokens):
        stack=[]
        for num in tokens:
          if num in "+/-*":
            if num =="+":
              a=stack.pop()
              b=stack.pop()
              result=int(b)+int(a)
              stack.append(str(result))
              continue
            elif num =="-":
              a=stack.pop()
              b=stack.pop()
              result=int(b)-int(a)
              stack.append(str(result))
              continue
            elif num =="*":
              a=stack.pop()
              b=stack.pop()
              result=int(b)*int(a)
              stack.append(str(result))
              continue
            else:
              a=stack.pop()
              b=stack.pop()
              result=int(int(b)/int(a))
              stack.append(str(result))
              continue
          else:  
            stack.append(num)
        return int(stack[0])
          