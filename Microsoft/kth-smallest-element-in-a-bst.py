# https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def func(root):
            nonlocal k
            if not root:
                return None
            l = func(root.left)
            if l:
                return l
            k-=1
            if k==0:
                return root
            return func(root.right)
        return func(root).val