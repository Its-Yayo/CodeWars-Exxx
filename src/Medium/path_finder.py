#!/usr/bin/python3

"""
Instructions:
Source: 

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions 
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked ..
Walls are marked W.
Start and exit positions are empty in all test cases.


"""

from collections import deque


def path_finder(maze: list[list[str]]) -> bool:
    """ I'll use BFS as a fast approach to find the shortest path 
        in order to exit position [N-1, N-1] 
        
        To avoid an unhashable type error, I'm tracking a new list with visited cells """
    
    start = [0, 0]
    maze = maze.split("\n")
    r, c = len(maze), len(maze[0])
    visited = [[False for _ in range(c)] for _ in range(r)]
    queue = deque([start])
    
    while queue:
        cell = queue.popleft()
        visited[cell[0]][cell[1]] = True
        
        if cell == [r - 1, c - 1]:
            return True
        
        north = [cell[0], cell[1] + 1]
        south = [cell[0], cell[1] - 1]
        east = [cell[0] + 1, cell[1]]
        west = [cell[0] - 1, cell[1]]

        
        for next in [north, south, east, west]:
            if not visited[next[0]][next[1]] and maze[next[0]][next[1]] != 'W' and 0 <= next[0] < r and 0 <= next[1] < c:
                visited[next[0]][next[1]] = True 
                queue.append(next)
                
                if next[0] == r - 1 and maze[next[0]][next[1]] != 'W':
                    return True


    return False

