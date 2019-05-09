import unittest

def paths_with_sum(binary_TREE, target_SUM):
    partial_PATHS = ListDict({target_SUM:[[]]})
    return path_with_partial_sum(binary_TREE,target_SUM, partial_PATHS)

def path_with_partial_sum(node,target_SUM, partial_PATHS):
    if not node: return []
    result = []
    nxt_PARTIAL = ListDict({target_SUM:[[]]})
    for sums,paths, in partial_PATHS.items():
        for path in paths:
            nxt_PARTIAL[sums- node.value] = [path+[node.name]]
    result = nxt_PARTIAL[0]
    for child in [node.left, node.right]:
        result += (path_with_partial_sum(child,target_SUM,nxt_PARTIAL))
    return result

class Node():
    def __init__(self, name, value, left = None, right= None):
        self.name, self.value, self.left, self.right, = name, value, left, right
class ListDict(dict):
    def __missing__(self, key):
        return []

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt= Node("A",4,Node("B",-2, Node("D",7),Node("E", 4)),
        Node("C", 7,Node("F",-1, Node("H",-1),Node("I",2,Node("K",1))),
        Node("G", 0, None, Node("J", -2))))
    self.assertEqual(paths_with_sum(bt, 2), [["A", "B"], ["B", "E"], ["I"],["F", "I", "K"]])
    self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
    self.assertEqual(paths_with_sum(bt, 9), [["A","B","D"], ["A","C","F","H"],["C","F","I","K"], ["A","C","G","J"]])

if __name__ == "__main__":
  unittest.main()
