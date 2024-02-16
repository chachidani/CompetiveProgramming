class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        count = {"T":0, "F": 0}
        max_len = 0
        left = 0
        for right in range(len(answerKey)):

            count[answerKey[right]] += 1

            while min(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left+=1

            max_len = max(max_len, right-left+1)
        return max_len




        