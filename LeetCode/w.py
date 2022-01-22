# Depth of a String
# find string at highest depth.
# //example 
# input: "((AB)(((CD))))" 
# depth = 4


# '''
# Array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 US is equal to 0.77 GBP an array containing a 'from' currency and a 'to' currency. Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency. Your return value should be a number
# // Example:
# You are given the following parameters:
# Rates: ['USD', 'JPY', 110] ['USD', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
# To/From currency: ['GBP', 'AUD']
# Output: 1.89
# '''
# rates = [['USD', 'JPY', 110] ,['USD', 'AUD', 1.45] ,['JPY', 'GBP', 0.0070]]
# from itertools import permutations
# graph = defaultdict(defaultdict)
# for src,dest,val in rates:
#     graph[src][dest] = val
#     graph[src][src] = graph[dest][dest] = 1
#     # graph[dest][src] = 1/val

# # usd jpy aud
# for i,j,k in permutations(graph,3):
#     if i in graph[j] and k in graph[i]:
#         graph[j][k] = graph[j][i] * graph[i][k]

# print(graph)
# print(graph['GBP'].get('AUD')) 



# '''
# I had my onsite a few days ago. They started off with introductions which took 20 mins and then I gave my introduction. Opened link to hackerrank and saw a non leetcode question.
# You have flights e.g.
# A->B
# B-> C,D
# C-E
# D-E

# result = [[A,B,C,E], [A, B, D, E]]


# Had to implement 2 methods. One was to add a new start and end location. 

# The other was to print all locations from a starting point to a destination e.g. print all possible travel methods from A to E.

# Follow up: How to make your solution more efficient if you knew that an airport was not going to get you to your desination


# '''
# # class FlightTravel:
# #     def __init__(self):
# #         self.routes = {
# #             'A': ["B", 'C'],
# #             'B': ['A','C', 'D'],
# #             'C': [],
# #             'D': ['E']
# #         }
# #         # defaultdict(list)

# #     def addRoute(self,start, dest):
# #         self.routes[start].append(dest)
    
# #     def allRoute(self, start, target):
        
# #         def dfs(source, curr_path, result, forbidden):
# #             if(source == target):
# #                 result.append(curr_path)
# #             else:
# #                 paths = self.routes[source]
# #                 if(len(paths) == 0):
# #                     forbidden.add(source)
# #                 for path in paths:
# #                     if(path in curr_path or path in forbidden):
# #                         continue
# #                     dfs(path, curr_path + [path] , result, forbidden)

# #         result = []
# #         forbidden = set()
# #         dfs('A', ['A'], result, forbidden)
# #         return result


# # flightTravel = FlightTravel()
# # solution = flightTravel.allRoute('A', 'E')
# # print(solution)






from itertools import permutations



