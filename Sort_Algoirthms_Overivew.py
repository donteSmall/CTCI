from random import randint
import unittest

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = left
        self.right = right

def create_array(size = 10, max= 50):

    return [randint(0,max) for _ in range(size)]
def swap(s1, s2):

    return s2,s1

def merge(list1,list2):
    merge_list = []
    #Set to zero because ends of both list will start at the beging due to sorting
    list1_idx, list2_indx = 0,0
    while list1_idx < len(list1) and list2_indx < len(list2):
        #compare elements at the top of each array
        if list1[list1_idx] < list2[list2_indx]:
            merge_list.append(list1[list1_idx])
            list1_idx +=1
        else:
            #append whatever is smaller
            merge_list.append(list2[list2_indx])
            list2_indx +=1

    if list1_idx == len(list1):
        merge_list.extend(list2[list2_indx:])
    else:
        merge_list.extend(list1[list1_idx:])
    return merge_list

def merge_sort(input):
    if len(input) <= 1:
        return input
    left = merge_sort(input[:len(input)/2])
    right = merge_sort(input[len(input)/2:])

    return merge(left,right)


def bubble_SORT(input):
    for idx in range (0,len(input) - 1):

        for j in range(0, len(input) - 1 - idx):
            if input[j] > input[j+1]:
                #Swapping values based on condition.

                input[j], input[j + 1]  = input[j + 1],input[j]

                #Issue with swap function !!!
                #swap(input[j],input[j + 1])

                # Why does this break if assigned differently ??
    return input

def insert_SORT(input):
    #O(n^2) Not really good because of nested loop untilization
    for idx_rht in range( 1 ,len(input)):
        #moves left through list
        for idx_lft in range(idx_rht -1 ,0, -1):
            if input[idx_lft] > input[idx_lft + 1]:
                input[idx_lft], input[idx_lft + 1]  = input[idx_lft + 1],input[idx_lft]
            else:
                break
    return input

def insert_SORTOptimized(input):
    #O(n^2) Not really good because of nested loop untilization
    for idx_rht in range( 1 ,len(input)):
        #copy currrent value into temp var
        curNum = input[idx_rht]
        #moves left through list
        for idx_lft in range(idx_rht - 1 ,0, -1):
            if input[idx_lft] > curNum:
                 input[idx_lft + 1]  = input[idx_lft]
            else:
                #If not place curNum back where it belongs
                input[idx_lft + 1] = curNum
                break
    return input

'''
 This is faster as swapping requires three opertions :
 temp = x
 x = y
 y = temp
 Instead we cut that down by swapping two value into a Curnum, then we do
 comparision of values where we write over the lesser value. This save us a lot of swapping.
 '''

def selection_SORT(input):
    #O(n2) Not fast because of nested looping
    lastIndx = len(input) - 1
    for idx in range(0,lastIndxs):
        min_Idx = idx

        for idx_j in range (idx + 1,len(input)):

            if input[idx_j] < input[min_Idx]:
                min_Idx = idx_j

        if min_Idx != idx:
            input[idx],input[min_Idx] = input[min_Idx],input[idx]

    return input

quick_TEMP= [1,4,5,7,0,6,2,8,9,3]


def quick_SORT(list_SORT,low_idx,high_idx):
    #When the indexs are the same

    if((high_idx - low_idx) > 0):
        #contine
        seperator = partition(list_SORT,low_idx,high_idx)
        #Produces two more list to sort

        #sort the lower portion of the list
        quick_SORT(list_SORT,low_idx,seperator - 1)

        #sort the higher portion of the list
        quick_SORT(list_SORT,seperator + 1,high_idx)
        #when it gets down to the last element, it returns

#O(n) n,the size of the list, operations to iter list
# The list is partition for every element. However if the list randomized we would have to iter every element.
# We would only need to perform it (log n) times as that is how deep the recursion tree will be.
def partition(list_SORT,low_idx,high_idx):
    list_DIVIDER = low_idx
    pivot = high_idx


    for val in range(low_idx,high_idx):
        #compare to every element in list
        if (list_SORT[val] < list_SORT[pivot]):

            list_SORT[val], list_SORT[list_DIVIDER] = list_SORT[list_DIVIDER],list_SORT[val]
            #increment to next element in the list
            list_DIVIDER +=1

    list_SORT[pivot], list_SORT[list_DIVIDER] = list_SORT[list_DIVIDER],list_SORT[pivot]

    #where pivot val resides
    return list_DIVIDER
#O(n log n)


ex = merge_sort(create_array())
print(ex)

class Test(unittest.TestCase):
    def setUp(self):
        self.list1 = [1,3,5]
        self.list2 = [2,4,6]

    def test_Merge(self):
        result = merge(self.list1,self.list2)
        expected = [1,2,3,4,5,6]
        self.assertEqual(result, expected)


    def test_bubble_SORT(self):
        data = ['b','d','f','a','c','e']
        result = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(bubble_SORT(data), result)

    def test_insert_SORT(self):
        data = [1,3,5,7,2,1,2,1,6,9,9,7,6,55,99]
        expected = [1, 1, 1, 2, 2, 3, 5, 6, 6, 7, 7, 9, 9, 55, 99]
        self.assertEqual(insert_SORT(data),expected)

    def test_selection_SORT(self):
        data = [1,3,5,7,2,2,1,6,9,9,6,55]
        expected = [1, 1, 2, 2, 3, 5, 6, 6, 7, 9, 9, 55]
        self.assertEqual(insert_SORT(data),expected)

    def test_quick_SORT(self):
        data = [1,0,2,3,4,6,5,8,9,7]
        quick_SORT(data,0,9)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(data,expected)



if __name__=="__main__":
    unittest.main()
