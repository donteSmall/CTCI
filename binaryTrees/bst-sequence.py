
import unittest

class Node(object):
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None

def bst_sequences(bst):
    return sequences_partial([],[bst])

def sequences_partial(partial, subtrees):
    if not subtrees:
        return [partial]

    sequence = []

    for index, node in enumerate(subtrees):
        nxtPartial = partial + [node.value]
        nxtSubtree = subtrees[:index] + subtrees[index+1:]

        if node.left:
            nxtSubtree.append(node.left)
        if node.right:
            nxtSubtree.append(node.right)
        sequence += sequences_partial(nxtPartial,nxtSubtree)

    return sequence

class Test(unittest.TestCase):
    def test_bst_sequences(self):
        tree = Node(2)
        tree.left = Node(1)
        tree.right = Node(3) 
        self.assertEqual(bst_sequences(tree),[[2,1,3],[2,3,1]])

    def test_Bst_Sequences_With_Four_Num(self):
        tree = Node(7)
        tree.left = Node(4)
        tree.left.right = Node(5)
        tree.right = Node(9) 
        self.assertEquals(bst_sequences(tree), [[7, 4, 9, 5],[7, 4, 5, 9],[7, 9, 4, 5]])
  
if __name__ == "__main__":
    unittest.main()