class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        rabbits = answers[0]+1
        k = answers[0]
        for i in range(1, len(answers)):
            
            if answers[i] != answers[i-1]:
                rabbits += answers[i]+1
                k = answers[i]
            elif answers[i] == answers[i-1] and k == 0:
                rabbits += answers[i]+1
                k =answers[i] 
            else:
                k -=1

        return rabbits


        