# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        # A dictionary to map original nodes to their corresponding copies
        node_map = {}
        
        def dfs(original_node):
            # If we've already created a copy of this node, return it
            if original_node in node_map:
                return node_map[original_node]
            
            # Create a new copy of the node
            copy_node = Node(original_node.val)
            
            # Add the copy to the mapping
            node_map[original_node] = copy_node
            
            # Recursively clone the neighbors
            for neighbor in original_node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            
            return copy_node
        
        return dfs(node)

# Example usage
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]

node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

clone = Solution().cloneGraph(node1)
print(clone.val)  # Output: 1
print(clone.neighbors[0].val)  # Output: 2
print(clone.neighbors[1].val)  # Output: 4
print(clone.neighbors[0].neighbors[0].val)  # Output: 1
print(clone.neighbors[0].neighbors[1].val)  # Output: 3
print(clone.neighbors[1].neighbors[0].val)  # Output: 1
