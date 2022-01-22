'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


Iterate rows, col
    if land:
        if its in set , increment islands
        bfs(1) to put all connecting lands to seen set.

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

seen = [(0,0), (0, 1), (1,0), (0, 2), (1,2)]
island = 0, 1

queue = [1,2), (1,1), (2,0), (0,3)]

'''
# seen = set()
# queue = []

# 3,3 => x, y+1 or x, y-1 or x+1, y or x-1

# def bfs((r,c)):
#     directions = [
#         [r+1, c], [r-1, c], [r, c+1], [r, c-1]
#     ]
    
#     queue = [(r, c)]

#     while queue:
#         current = 

#     for direction in directions:
#         r = direction[0]
#         c = direction[1]
#         if(r < 0 or r == m or c == 0 or c == n or direction in seen or grid[r][c] == 0): continue
#         queue.append([r,c]))
#         seen.add((r, c))


# count = 0
# for r in range(m):
#     for c in range(n):
#         curr = (r, c)
#         if(grid[r][c] == 1 and curr not in seen):
#             count +=1 
#             seen.add(curr)
#             bfs(curr)
