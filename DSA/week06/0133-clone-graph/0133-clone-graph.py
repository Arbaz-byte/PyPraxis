"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        
        old_to_new = {}

        def dfs(current):
            # if we already clone this node, return the clone
            if current in old_to_new:
                return old_to_new[current]
            
            # create a copy of current node and save it in the map
            copy = Node(current.val)
            old_to_new[current] = copy

            # recursivly colne all neighbours 
            for neighbour in current.neighbors:
                copy.neighbors.append(dfs(neighbour))
            
            return copy
        
        return dfs(node)

        