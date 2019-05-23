#!/usr/bin/env python3

import unittest
import itertools
from functools import reduce

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
    return  list(map(lambda x: x - 2, each__(da_list)))

def map_TOEACHITEMWithNVal(da_list, num):
    return  list(map(lambda x: x + num, each__(da_list)))
'''
A ‘filter’ function, which calls a function for each item in a collection
and returns all of the items where the function returns a truthy value.
'''

def filterModOfNum(func):
    rangeList= range(0,9)
    return list(filter(lambda x: x % 2==0, map_TOEACHITEM(func)))

'''
An “accumulate” function that takes an iterable, a function, and an initial value,
then calls the function with the accumulated value and an item in the iterable.
The passed function returns a new value which is passed next time the function is called
'''
def accumulate(aList):
    addList= reduce((lambda x,y: x + y), map_TOEACHITEMWithNVal(aList,0))
    return addList
'''
Implement find_first, a function that takes an iterable and
a function to apply and runs the first item where the function returns truthy
'''
def findfirst(firstTruthy):

    func =lambda a: "Even Num" if a % 2 == 0 else "Odd Num"
    return func(firstTruthy)




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



    def test_calls_a_func_with_each_item_in_collection(self):
        root = Node(6)
        binary_search_insert(root, 5)
        binary_search_insert(root, 8)
        binary_search_insert(root, 4)
        binary_search_insert(root, 9)
        self.assertEqual([4, 3, 2, 6, 7], map_TOEACHITEM(root))

    def test_calls_a_func_for_each_item_in_collection_and_returns_all_results(self):
        root = Node(6)
        binary_search_insert(root, 5)
        binary_search_insert(root, 8)
        binary_search_insert(root, 4)
        binary_search_insert(root, 9)
        self.assertEqual([4,2, 6,], filterModOfNum(root))

    def test_accumulate_func_with_iterable_and_value(self):
        root = Node(6)
        binary_search_insert(root, 5)
        binary_search_insert(root, 8)
        binary_search_insert(root, 4)
        binary_search_insert(root, 9)
        self.assertEqual(32, accumulate(root))

    def test_find_first_truthy_val(self):
        self.assertEqual("Even Num", findfirst(4))






if __name__ == '__main__':
    unittest.main()
