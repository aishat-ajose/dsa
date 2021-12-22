# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while(curr):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            
        return prev
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        tail = result = ListNode(0)
        
        while(carry or l1 or l2):
            add = (carry if carry else 0) + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry, res = divmod(add, 10)
            
            new_node = ListNode(res)
            tail.next = new_node
            tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return self.reverseList(result.next)
            
        
        