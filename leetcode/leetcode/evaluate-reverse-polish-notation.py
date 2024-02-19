class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+':(lambda x,y: operator.add(x,y)),
              '-':(lambda x,y: operator.sub(x,y)),
              '*':(lambda x,y: operator.mul(x,y)),
              '/':(lambda x,y: int(x/y))}

        for i in tokens:
            if i  not in op:
                stack.append(int(i))
            else:
                x = stack.pop(-2)
                y = stack.pop()
                stack.append(op[i](x,y))
        return stack[-1]



                
                    
            