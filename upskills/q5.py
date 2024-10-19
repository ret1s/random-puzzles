class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def getMaxDept(self, node=None):
        if node == None:
            node = self.root
            
        if self.node == None:
            return 0
        
        lh = self.getMaxDept(node.left)
        rh = self.getMaxDept(node.right)
        
        return max(lh, rh) + 1