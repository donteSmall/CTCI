#!/usr/bin/env python3

import unittest
import itertools

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def binary_search_insert(root, new_value):
    if new_value < root.value:
        if root.left is None:
            root.left = Node(new_value)
        else:
            binary_search_insert(root.left, new_value)
    else:
        if root.right is None:
            root.right = Node(new_value)
        else:
            binary_search_insert(root.right, new_value)

def recursive_list_of_depths(root):
    this_depth = [[root.value]]
    if root.left and root.right:
        for pair in zip(list_of_depths(root.left), list_of_depths(root.right)):
            this_depth.append(pair[0] + pair[1])
        return this_depth
    elif root.left:
        return this_depth + list_of_depths(root.left)
    elif root.right:
        return this_depth + list_of_depths(root.right)
    else:
        return this_depth

def refactored_recursive_lod(root):
    this_depth = [[root.value]]
    left = []
    right = []

    if root.left:
        left = list_of_depths(root.left)
    if root.right:
        right = list_of_depths(root.right)

    for pair in itertools.zip_longest(left, right):
        # The ors here are just to handle None, which is how zip_longest pads the shorter iterable
        this_depth.append((pair[0] or []) + (pair[1] or []))

    return this_depth

def in_order_map_reduce(root, map_fn, reduce_fn):
    """Given a root note and a map and reduce function

    map_fn is passed a node's value to map
    reduce_fn is passed a list of [left_subtrees_reduction, this mapping, right_subtree_reduction]
              and expected to return a new reduction"""
    results = []

    if root.left:

        results.append(in_order_map_reduce(root.left, map_fn, reduce_fn))
    else:
        results.append(None)

# map_fn call
    results.append(map_fn(root.value))

    if root.right:
        results.append(in_order_map_reduce(root.right, map_fn, reduce_fn))
    else:
        results.append(None)
# [left-result, mapped-value, right-result]
    return reduce_fn(results)

def map_reduce_lod(root):
    def lod_map(value):
        """A single node's lod value is a list of one list containing this value"""
        return [[value]]

    def lod_reduce(left_this_right):
        """To combine the left and right subtrees with this value, we combine left and right's lists and append them to this value"""
        left, this, right = left_this_right
        for pair in itertools.zip_longest(left or [], right or []):
            this.append((pair[0] or []) + (pair[1] or []))
        return this

    return in_order_map_reduce(root, lod_map, lod_reduce)
'''
Write an ‘each’ which calls a function with each item in a collection
'''
def call_TOEACHFUNC(value):


    def each__(root):
        result = []
        if root.value:
            result.append(root.value)
        else:
            return None
        if root.left and root.right is not None:
            for pair in itertools.zip_longest((map_reduce_lod(root.left)+ map_reduce_lod(root.right))):
                for items in pair:
                    result.append(items[0])
            return result
    '''
    A ‘map’ function, which calls a function for each item in a
    collection and returns all of the results in a list.
    '''
    def map_TOEACHITEM(da_list):
        #import pdb; pdb.set_trace()
        result = []
        #addTO = [lambda x: x*x for x in each__(da_list)]
        for x in each__(da_list):
             result.append(int(x) - 2)
        return result
    '''
    A ‘filter’ function, which calls a function for each item in a collection
    and returns all of the items where the function returns a truthy value.
    '''

    def callsEvenNum(func):
        for x in map_TOEACHITEM(func):
            if not(n % 3):
                return False



    return map_TOEACHITEM(value)



varChar = Node(6)
varChar.left = Node(5)
varChar.right = Node(8)
varChar.left.left = Node(4)
varChar.right.right = Node(9)
print(call_TOEACHFUNC(varChar))



# Change which function we're using for tests here
list_of_depths = map_reduce_lod
#list_of_depths = refactored_recursive_lod
#list_of_depths = recursive_list_of_depths

class BinaryTreeTest(unittest.TestCase):
    def test_node_created_with_value_has_that_value(self):
        node = Node(5)
        self.assertEqual(5, node.value)

    def test_node_unable_to_be_created_without_value(self):
        with self.assertRaises(TypeError):
            Node()

    def test_node_has_left_and_right_as_None_when_created(self):
        node = Node(5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_binary_search_insert_with_a_value_less_than_node_goes_left(self):
        root = Node(5)
        binary_search_insert(root, 4)
        self.assertEqual(4, root.left.value)
        self.assertIsNone(root.right)

    def test_binary_search_insert_with_a_value_more_than_node_goes_right(self):
        root = Node(5)
        binary_search_insert(root, 6)
        self.assertEqual(6, root.right.value)
        self.assertIsNone(root.left)

    def test_binary_search_insert_in_either_direction_more_than_once_goes_down_multiple_levels(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        self.assertEqual(3, root.left.left.value)


    def test_list_of_depths_single_level(self):
        root = Node(5)

        #maper =  list_of_depths(root)
        self.assertEqual([[5]], list_of_depths(root))

    def test_list_of_depths_two_levels_one_side(self):
        root = Node(5)
        binary_search_insert(root, 4)
        self.assertEqual([[5], [4]], list_of_depths(root))

    def test_list_of_depths_two_levels_two_sides(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 6)
        self.assertEqual([[5], [4, 6]], list_of_depths(root))

    def test_list_of_depths_multiple_levels(self):
        root = Node(5)
        binary_search_insert(root, 4)
        binary_search_insert(root, 3)
        binary_search_insert(root, 6)
        binary_search_insert(root, 7)

        self.assertEqual([[5], [4,6], [3,7]], list_of_depths(root))




'''
>>> True or False
True
>>> False or True
True
>>> None or 5
5
>>> 5 or None
5
>>> not not None
False
>>> not None
True
>>> None or []
[]
>>> [1,2,3] or []
[1, 2, 3]
>>> not not []
False
>>> import itertools

>>> list(itertools.zip_longest([1,2,3], []))
[(1, None), (2, None), (3, None)]

>>> list(itertools.zip_longest([[1],[2],[3]], []))
[([1], None), ([2], None), ([3], None)]

>>> list(itertools.zip_longest([[1],[2],[3]], [4]))
[([1], 4), ([2], None), ([3], None)]

>>> list(itertools.zip_longest([[1],[2],[3]], [[4]]))
[([1], [4]), ([2], None), ([3], None)]

>>> [1] + [4]
[1, 4]

>>> [2] + [None]
[2, None]

>>> [2] + []
[2]

>>> [1,2,3] + [4,5]

[1, 2, 3, 4, 5]

>>> [1,2,3] + []
[1, 2, 3]



>>> import Kev_Gist
>>> Kev_Gist.in_order_map_reduce

>>> map_reduce = Kev_Gist.in_order_map_reduce
>>> insert = Kev_Gist.binary_search_insert
>>> Node = Kev_Gist.Node


>>> root = Node(5)
>>> root.left = Node(4)
>>> root.right = Node(6)
>>> identity = lambda x: x

>>> def sum_via_reduce(left_this_right):
    left, this, right = left_this_right
    return (left or 0) + this + (right or 0)

>>> product = lambda x: (x[0] or 1) * x[1] * (x[2] or 1)

>>> map_reduce(root, lambda x: x * 2, product)
960

>>> map_reduce(root, lambda x: x, product)
120

>>> 5 * 4 * 6
120

>>> 5  * 4 * 6 * 8
960
'''

if __name__ == '__main__':
    unittest.main()
