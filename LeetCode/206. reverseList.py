# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
                  
        prev_node = None
        curr_node = head
        
        while(curr_node != None):
            next_node = curr_node.next  
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node