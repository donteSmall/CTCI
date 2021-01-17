from pprint import pprint
import unittest

class Node(object):
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None

def isValidBSTSubtree(root):
    return helper(root, float("-inf"),float("inf"))

def helper(root,minVal,maxVal):
    if root is None:
        return True

    if root.value <= minVal or root.value >= maxVal:
        return False

    validLeft = helper(root.left, minVal, root.value)
    validRight = helper(root.right, root.value, maxVal)
    return validLeft and validRight

class Test(unittest.TestCase):
    def test_isBalancedTreeTrue(self):
        tree = Node(2)
        tree.left = Node(1)
        tree.right = Node(3)
        self.assertTrue(isValidBSTSubtree(tree))

    def test_isBalancedTreeFalse(self):
        tree = Node(5)
        tree.left = Node(1)
        tree.right= Node(4)
        tree.right.left = Node(3)
        tree.right.right = Node(6)
        self.assertFalse(isValidBSTSubtree(tree))
        


#Time O(n)
# Space O(1)
# WORST CASE: O(n)
#Best Case: ()
  
if __name__ == "__main__":
    unittest.main()