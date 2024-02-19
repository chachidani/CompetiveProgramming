class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
              days[stack[-1]] = i - stack[-1]
              stack.pop()
            stack.append(i)
        return days
                
                

        