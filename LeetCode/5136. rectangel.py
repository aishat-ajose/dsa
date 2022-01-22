class Sea:
    def hasShips(self, topRigth, bottomLeft):
        pass

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Solution:
    def countShips(self, topRight, bottomLeft):
        def findShip(self, topRight, bottomLeft):
            if(topRight.x < bottomLeft.x or topRight.Y < bottomLeft.y):
                return 0
            elif(topRight.x == bottomLeft.x and topRight.y == bottomLeft.y):
                return int(Sea.hasShips(topRight, bottomLeft))


            if(not Sea.hasShips(topRight, bottomLeft)):
                return 0
            
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2
            mid = (midX, midY)

            topLeftQ = findShip(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1) )
            topRightQ = findShip(topRight, Point(mid.x +1, mid.y + 1))
            bottomLeftQ = findShip(Point(mid.x, mid.y), bottomLeft)
            bottomRightQ = findShip(Point(topRight.x, mid.y), Point(mid.x, bottomLeft.y))


            return topLeftQ + topRightQ + bottomLeftQ + bottomRightQ

        
        return findShip(topRight, bottomLeft)