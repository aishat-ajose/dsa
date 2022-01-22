class Stream:
    def __init__(self) -> None:
        self.queue = []
        self.hashMap = {}
        self.head = 0

    def add(self,  num) :
        self.queue.append(num)
        self.hashMap[num] = self.hashMap.get(num, 0) + 1

    def getFirstUnique(self):
        while(self.head < len(self.queue)):
            curr = self.queue[self.head]
            if(self.hashMap[curr] > 1):
                self.head += 1
            else:
                print(self.queue[self.head])
                return
        print(-1)


s = Stream()
s.add(2)
s.getFirstUnique() # 2
s.add(2)
s.getFirstUnique() # null
s.add(3)
s.getFirstUnique() # 3
s.add(4)
s.getFirstUnique() # 3
s.add(3)
s.getFirstUnique() # 4