class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == '../' and len(stack)!=0:
                stack.pop()
                
            elif logs[i] == './' or logs[i] == '../' and len(stack)==0:
                continue
            else:
                stack.append(logs[i])
            
        return len(stack)

        