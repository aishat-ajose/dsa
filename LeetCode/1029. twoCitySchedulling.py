class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs.sort(key = lambda x: x[1] - x[0], reverse=True)

        result = 0
        n = len(costs)
        for i in range(n):
            if(i < (n//2)):
                result += costs[i][0]
            else:
                result += costs[i][1]
        print(result)
        


# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# [[10,20],[30,200],[400,50],[30,20]]
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
solution = Solution()
solution.twoCitySchedCost(costs= costs)


# T = int(input())

# while(T):
#     inp = input()
#     lst = inp.split(' ')
#     N = int(lst[0])
#     x = int(lst[1])
#     y = int(lst[2])

#     T -= 1