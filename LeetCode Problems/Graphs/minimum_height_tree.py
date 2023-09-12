class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # Create an adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        degrees = [0] * n  # To keep track of the degrees of nodes

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        leaves = [i for i in range(n) if degrees[i] == 1]

        while n > 2:
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)
                n -= 1
            leaves = new_leaves

        return leaves

# example usage
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
print(Solution().findMinHeightTrees(n, edges))  # Output: [1]

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(Solution().findMinHeightTrees(n, edges))  # Output: [3, 4]