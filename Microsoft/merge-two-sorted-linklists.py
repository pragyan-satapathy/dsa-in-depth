# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/2063533726/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Dummy head + two-pointer merge
# Use a dummy sentinel node so we never have to special-case an empty result list.
# At each step, pick the smaller head from list1/list2, attach it to curr, and advance.
# When one list is exhausted, append the remainder of the other (already sorted).
# Time: O(m+n)  Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = root = ListNode()   # dummy sentinel; result starts at root.next

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1   # pick from list1
                list1 = list1.next
            else:
                curr.next = list2   # pick from list2
                list2 = list2.next
            curr = curr.next        # advance the merge pointer

        # attach whichever list still has remaining nodes
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return root.next   # skip the dummy head