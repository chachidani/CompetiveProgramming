# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    
        redgraph = defaultdict(list)
        bluegraph = defaultdict(list)


        for a, b in redEdges:
            redgraph[a].append(b)

        for u, v in blueEdges:
            bluegraph[u].append(v)

        blue = 'B'
        red = 'R'

        answer = []
        for destination in range(n):

            visted = set()
            queue = deque()

            queue.append((0, 0, blue))
            queue.append((0, 0, red))

            found = False
            while queue and not found:
                
                size = len(queue)
                for i in range(size):

                    node, distance, color = queue.popleft()
                    visted.add((node, color))

                    if node == destination:
                        found = True
                        break

                    if color == red:
                        for nbs in bluegraph[node]:

                            if (nbs, blue) not in visted:
                                queue.append((nbs, distance + 1, blue))
                    else:
                        for nbs in redgraph[node]:

                            if (nbs, red) not in visted:
                                queue.append((nbs, distance + 1, red))

            answer.append(distance if found else -1)        

        return answer
