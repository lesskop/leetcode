class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# Traverse the linked list to create a list, then create a new linked list from the reversed list
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = []
#         curr = head
#
#         while curr:
#             temp.append(curr.val)
#             curr = curr.next
#
#         temp = temp[::-1]
#
#         if not temp:
#             return None
#
#         head = ListNode(temp[0])
#         curr = head
#
#         for data in temp[1:]:
#             new_node = ListNode(data)
#             curr.next = new_node
#             curr = new_node
#
#         return head
