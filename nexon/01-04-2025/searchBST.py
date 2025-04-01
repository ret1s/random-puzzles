# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        tmp = root
        while tmp and tmp.val != val:
            if val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return tmp
        