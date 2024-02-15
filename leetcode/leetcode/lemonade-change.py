class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collect = defaultdict(int)
       
        for i in range(len(bills)):
            if bills[i] == 5:
                collect["five"] = collect.get("five", 0)+1
            elif bills[i] == 10 and collect["five"] > 0 :
                collect["five"] -=1
                collect["ten"] = collect.get("ten" , 0)+1
            elif bills[i] == 20 and collect["five"] > 0 and collect["ten"] > 0:
                collect["five"] -=1
                collect["ten"] -=1
                collect["twee"] = collect.get("twee" , 0)+1
            elif bills[i] == 20 and collect["five"] > 2 :
                collect["five"] -=3
                
                collect["twee"] = collect.get("twee" , 0)+1
            
            else: 
                return False
            

            

        return True
                 

        