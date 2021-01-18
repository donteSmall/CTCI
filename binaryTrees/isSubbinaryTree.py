from pprint import pprint
import unittest

class Node(object):
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None

def isSubtree(t1, t2):
    
    if t1 is None and t2 is None:
        return True
    if t2 is None:
        return True
    if t1 is None and t2 is not None:
        return False
    return isSame(t1,t2) or isSubtree(t1.left,t2) or isSubtree(t1.right,t2) 

def isSame(t1,t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.value == t2.value and isSame(t1.left,t2.left) and isSame(t1.right,t2.right)


class Test(unittest.TestCase):
    def test_isSubtreeTrue(self):
        tree = Node(3)
        tree.left = Node(4)
        tree.right = Node(5)  #right Side
        tree.left.left = Node(1)
        tree.left.right = Node(2)
       
        
        #Second Tree
        tree2 = Node(4)
        tree2.left = Node(1)
        tree2.right = Node(2)
        self.assertTrue(isSubtree(tree, tree2))

    def test_isSubtreeFalse(self):
        tree = Node(3)
        tree.left = Node(4)
        tree.right = Node(5)  #right Side
        tree.left.left = Node(1)
        tree.left.right = Node(2)
        tree.left.right.left = Node(0)
       
        
        #Second Tree
        tree2 = Node(4)
        tree2.left = Node(1)
        tree2.right = Node(2)
        self.assertFalse(isSubtree(tree, tree2))
    

    
    
  
if __name__ == "__main__":
    unittest.main()

