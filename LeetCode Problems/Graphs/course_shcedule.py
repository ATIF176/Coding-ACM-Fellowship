class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Create an adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # Create an array to keep track of the visited status of nodes
        visited = [0] * numCourses  # 0 represents unvisited, 1 represents visiting, 2 represents visited
        
        def is_cyclic(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False
            
            visited[course] = 1
            for prereq in graph[course]:
                if is_cyclic(prereq):
                    return True
            
            visited[course] = 2
            return False
        
        for course in range(numCourses):
            if visited[course] == 0:
                if is_cyclic(course):
                    return False
        
        return True


# Example usage
print(Solution().canFinish(2, [[1, 0]]))  # Output: True

print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # Output: False

print(Solution().canFinish(3, [[1, 0], [2, 1]]))  # Output: True