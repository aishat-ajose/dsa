class Node:
    def __init__(self, homepage):
        self.url = homepage
        self.next = None
        self.prev = None
    


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = newNode


    def back(self, steps: int) -> str:
        while(steps > 0 and curr.prev is not None):
            curr = curr.prev
            steps -= 1
        return self.curr.url


    def forward(self, steps: int) -> str:
        while(steps > 0 and curr.next is not None):
            curr = curr.next
            steps -= 1
        return self.curr.url