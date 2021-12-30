class DoublyLinkedListNode():
    def __init__(self, data, next, prev) -> None:
        self.data = data
        self.next = next
        self.prev = prev


def sortedInsert(llist, data):
    # Write your code here
    
    dummyNode = DoublyLinkedListNode(None, llist, None)
    llist.prev = dummyNode
   
    prev = None
    curr = dummyNode
    newNode = DoublyLinkedListNode(data, None, None)

    while (curr):
        if(curr.data != None):
            if(data < curr.data):
                newNodePrev = curr.prev
                newNodePrev.next = newNode
                newNode.prev = newNodePrev
                newNode.next = curr
                curr.prev = newNode
                
                return dummyNode.next
            
        prev, curr = curr, curr.next
        
    # If the node is greater than the existing nodes
    prev.next = newNode
    newNode.prev = prev
    return dummyNode.next