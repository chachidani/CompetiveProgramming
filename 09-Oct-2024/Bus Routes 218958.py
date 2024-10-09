# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        thebus = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                thebus[stop].append(i)
        
        print(thebus)

        queue = deque([(source, 0)])  
        visited_routes = set()  
        visited_stops = set([source])  

        while queue:
            stop, buses_taken = queue.popleft()

            for route in thebus[stop]:
                if route in visited_routes:
                    continue  
                
                visited_routes.add(route)  
                
                for next_stop in routes[route]:
                    if next_stop == target:
                        return buses_taken + 1  
                    
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        
        return -1  
