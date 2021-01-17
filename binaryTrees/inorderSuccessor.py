from pprint import pprint
import unittest

class Node(object):
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None



'''
Given a binary search tree and a node in it, 
find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, returnnull.
 
 DURING THE TRAVERSAL
    IF NODE GOES TO LEFT Side of Tree:
        Store the node as Successor before doing so
'''
def inOrderSuccessor(root,hasASuccessor):
    successor = None
    while root:
        if hasASuccessor.value < root.value:
            successor = root
            root = root.left
        else:
            root = root.right
    if successor is not None:
        return successor.value
    return successor

class Test(unittest.TestCase):
    def test_inOrderSuccessorTrue(self):
        tree = Node(2)
        tree.left = Node(1)
        tree.right = Node(3)
        self.assertEquals(inOrderSuccessor(tree,Node(1)),2)

    def test_inOrderSuccessorFalse(self):
        tree = Node(5)
        tree.left = Node(3)
        tree.right= Node(6)
        tree.left.left = Node(2)
        tree.left.left.right = Node(4)
        tree.left.left.left = Node(2)
        self.assertEquals(inOrderSuccessor(tree,Node(6)), None)
        

  
if __name__ == "__main__":
    unittest.main()