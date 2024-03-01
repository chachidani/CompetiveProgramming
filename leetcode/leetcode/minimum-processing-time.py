class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        pTime = 0
        tTask  = 0
        def calculate(n,arr):
            count = float('-inf')
            for i in arr:
                count = max(n+i,count)
            return count
        maxncount = float('-inf')
        while tTask < len(tasks) and pTime < len(processorTime) :
           
            maxncount = max(maxncount,calculate(processorTime[pTime],tasks[tTask:tTask+4]))

            tTask +=4
            pTime +=1

        return maxncount   


                

        