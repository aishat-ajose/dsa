class Solution:
    def dfs(self, graph, start, end, product, visited):
        answer = float(-1)
        visited.add(start)
        neigbors = graph[start]
        
        if end in neigbors:
            return product * neigbors[end]
        else:
            for neighbor, value in neigbors.items():
                if(neighbor not in visited):
                    answer = self.dfs(graph, neighbor, end, product*value, visited)
                if(answer != float(-1)):
                    break
        
        return answer
    
    def calcEquation(self, equations, queries):
        # 1. Create graph
        graph = {}
        
        for element in equations:
            num = element[0]
            den = element[1]
            value = element[2]
            
            if (num not in graph):
                graph[num] = {}

            graph[num][den] = value

            if(den not in graph):
                graph[den] = {}
            graph[den][num] = 1/value

        # 2.Calculations
        result = []
        for num, den in queries:
            if(num not in graph or den not in graph):
                return float(-1)
            elif(num == den):
                return float(1)
            else:
               return self.dfs(graph, num, den, 1, set())


sol = Solution()
Rates = [['USD', 'JPY', 110] ,['USD', 'AUD', 1.45] ,['JPY', 'GBP', 0.0070]]
currency= [['GBP', 'AUD']]
res = sol.calcEquation(Rates, currency)
print(res)
# Output: 1.89
