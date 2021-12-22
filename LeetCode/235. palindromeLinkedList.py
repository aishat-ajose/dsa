# Given the head of a singly linked list, return true if it is a palindrome.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def midOfaLinkedList(head: ListNode):
    slow = fast = head

    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
    return slow

def revereseLinkedList(head: ListNode):
    prev_node = None
    current_node = head

    while(current_node):
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


def palindromeLinkedList(head):
    first = head
    second = midOfaLinkedList(head)
    while(second): 
        if (first.val == second.val):
            first = first.next
            second = second.next
        else:
            return False
    
    return True

