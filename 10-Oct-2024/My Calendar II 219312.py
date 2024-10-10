# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.single = []  
        self.double_booked = []  #

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_booked:
            if max(start, s) < min(end, e):
                return False  
        
        for s, e in self.single:
            if max(start, s) < min(end, e):
                self.double_booked.append((max(start, s), min(end, e)))
        
        self.single.append((start, end))
        return True