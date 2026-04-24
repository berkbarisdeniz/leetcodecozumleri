class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append((stack[-1])+(stack[-2]))   
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(op))
        return sum(stack)