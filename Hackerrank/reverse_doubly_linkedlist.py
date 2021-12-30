def reverse(llist):
    prev = None
    curr = llist
    
    while(curr):
        tmpNext = curr.next
        curr.next = prev
        prev = curr
        if(prev):
            prev.prev = curr
        curr = tmpNext
        
        
    return prev 