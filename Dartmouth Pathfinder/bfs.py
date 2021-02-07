# name: Stephen Wang
# date: November 16, 2020
# purpose: Breadth first search algorithm

from collections import deque

def bfs(start, goal): # adapted from Project Python Ch.18
    queue = deque() # nodes to visit next
    queue.append(start)
    backpointers = {start: None} # keep track of route
    path_vertices = []
    
    while len(queue) != 0:
        # remove first node from queue
        current_node = queue.popleft()
        
        # add all adjacent vertices to frontier
        for adj in current_node.adj: 
            # if goal is found
            if adj == goal: 
                path_vertices.append(goal)
                backpointers[goal] = current_node
                path_vertices.append(backpointers[goal])
                # back-tracking
                while current_node != start:
                    path_vertices.append(backpointers[current_node])
                    current_node = backpointers[current_node]
                return path_vertices
                
            # if vertex not visited yet
            elif adj not in backpointers: 
                backpointers[adj] = current_node
                queue.append(adj)