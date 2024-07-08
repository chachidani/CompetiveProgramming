# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp = []
        kal = celsius +273.15
        far = (celsius*1.80) +32.00
        temp.append(kal)
        temp.append(far)
        return temp