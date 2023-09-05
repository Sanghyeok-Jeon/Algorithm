# 풀이 2
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 풀이 1
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     def reverse(node: ListNode, prev: ListNode = None):
#         if not node:
#             return prev
#         next, node.next = node.next, prev
#         return reverse(next, node)
#
#     return reverse(head)