# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/reverse-linked-list-ii/submissions/2063887234/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Locate, reverse in-place, reconnect
# Split the list conceptually into three parts:
#   [head ... firstEnd] → [left ... right] → [curr ...]
#                  ^           ^                  ^
#               firstEnd   secondStart          rest
# 1. Walk to the node just before position `left` (firstEnd).
# 2. Reverse exactly (right-left+1) nodes starting from firstEnd.next.
# 3. Reconnect: firstEnd → new head of reversed segment (prev)
#               old head of segment (secondStart) → first node after segment (curr)
# Dummy node handles the edge case where left == 1 (no node before the segment).
# Time: O(n)  Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        firstEnd = dummy          # will end up at the node just before position `left`
        count = right - left + 1  # number of nodes to reverse

        # step 1: advance firstEnd to the node just before `left`
        while firstEnd and left > 1:
            firstEnd = firstEnd.next
            left -= 1

        curr = firstEnd.next   # first node of the segment to reverse
        secondStart = curr     # remember it — it becomes the tail after reversal
        prev = None

        # step 2: reverse `count` nodes in-place
        while curr and count:
            nxt = curr.next
            curr.next = prev   # reverse the pointer
            prev = curr
            curr = nxt
            count -= 1

        # step 3: reconnect the three parts
        firstEnd.next = prev       # firstEnd → new head of reversed segment
        secondStart.next = curr    # old head (now tail) → rest of the list
        return dummy.next
        