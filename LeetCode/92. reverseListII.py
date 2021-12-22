# # Given the head of a singly linked list and two integers left and right where left <= right, 
# # reverse the nodes of the list from position left to position right, and return the reversed list.

# # Input: head = [1,2,3,4,5], left = 2, right = 4
# # Output: [1,4,3,2,5]

# class Solution:
#     def reverseBetween(self, head, m, n):
#         """
#         :type head: ListNode
#         :type m: int
#         :type n: int
#         :rtype: ListNode
#         """

#         if not head:
#             return None

#         left, right = head, head
#         stop = False

#         def recurseAndReverse(right, m, n):
#             nonlocal left, stop

#             # base case. Don't proceed any further
#             if n == 1:
#                 return

#             # Keep moving the right pointer one step forward until (n == 1)
#             right = right.next

#             # Keep moving left pointer to the right until we reach the proper node
#             # from where the reversal is to start.
#             if m > 1:
#                 left = left.next

#             # Recurse with m and n reduced.
#             recurseAndReverse(right, m - 1, n - 1)

#             # In case both the pointers cross each other or become equal, we
#             # stop i.e. don't swap data any further. We are done reversing at this
#             # point.
#             if left == right or right.next == left:
#                 stop = True

#             # Until the boolean stop is false, swap data between the two pointers     
#             if not stop:
#                 left.val, right.val = right.val, left.val

#                 # Move left one step to the right.
#                 # The right pointer moves one step back via backtracking.
#                 left = left.next           

#         recurseAndReverse(right, m, n)
#         return head


