class Solution:
    def dfs(self, source, graph, result, curr_path):
        print(curr_path)
        if(source == len(graph)-1):
            result.append(curr_path)
            
        for node in graph[source]:
            self.dfs(node, graph, result, curr_path + [node])
        
    def allPathsSourceTarget(self, graph):
        result = []
        self.dfs(0, graph, result, [0])
        return result
        


graph = [[1,2],[3],[3],[]]
# [[4,3,1],[3,2,4],[3],[4],[]]
# 
solution = Solution()
result = solution.allPathsSourceTarget(graph)
print(result)
