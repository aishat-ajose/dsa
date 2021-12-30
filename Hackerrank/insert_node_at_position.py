class SinglyLinkedList():
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    prev = llist
    count = 1
    
    while(count < position):
        prev = prev.next
        count += 1
        
    tmpNext = prev.next
    newNode = SinglyLinkedList(data, tmpNext)
    prev.next = newNode
    
    return llist