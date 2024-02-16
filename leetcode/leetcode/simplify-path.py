class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path = path.split('/')
        
        for dr in path:
            if dr == '.'or dr == '' or dr == '..' and len(stack) == 0:
                continue
            elif dr == '..' and len(stack) != 0:
                stack.pop()

            else:
                stack.append("/"+dr)
        if len(stack) == 0:
            stack.append('/')
            
        return ''.join(stack)

